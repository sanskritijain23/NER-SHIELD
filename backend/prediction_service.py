"""
backend/prediction_service.py
------------------------------
Owner: Member 4 (Backend)

Responsibility:
    Bridge between the backend and the ML module. This is the ONLY
    module in the backend that should import from ml/, and it is the
    single integration point where the real model gets wired in.

    result_service.py depends only on the public function:

        predict_risk(data) -> float   (0-100)

    Internally, predict_risk() delegates to _run_prediction(), which is
    the swappable boundary between:

        - the temporary mock formula (used right now), and
        - the future real ML implementation in ml/predict.py
          (Member 2's job, not available yet).

======================== STEP 9 — INTEGRATION BOUNDARY (READY) =================
ml/predict.py is still a placeholder (predict_risk_score() raises
NotImplementedError, and no model file exists), so nothing in this file
imports it and nothing here trains or fabricates a model. The scoring
behavior itself is UNCHANGED from Step 1/4 -- still the same
deterministic mock formula -- only the internal structure was tightened
so a real prediction can be dropped in later with a single, well-defined
change.

Structure, front to back:

    predict_risk(data)          <- public contract (unchanged), does
                                    input validation only.
      -> _run_prediction(data)  <- SWAPPABLE INTEGRATION BOUNDARY. This
                                    is the one function whose *body*
                                    changes when Member 2 ships a real
                                    model. Its signature/contract
                                    (dict in, float 0-100 out, raises
                                    ValueError on bad input) must stay
                                    the same either way.
           -> _extract_features(data)  <- pulls + validates the specific
                                           fields the current formula
                                           needs, raising a clean
                                           ValueError for missing/invalid
                                           required inputs.
           -> _mock_predict(...)       <- the actual TEMPORARY MOCK
                                           FORMULA, isolated in its own
                                           function so it's obvious
                                           exactly what gets deleted
                                           when it's replaced.

TODO (Member 4, later step -- once Member 2 ships ml/predict.py):
    Replace the body of _run_prediction() with something like:

        from ml.predict import predict_risk_score
        return predict_risk_score(data)

    predict_risk() itself, and everything in result_service.py /
    risk_logic.py that depends on it, should not need to change at all.
==================================================================================
"""

# Fields the current mock formula depends on. Kept as a single list so
# the "what does the prediction layer require" question has one answer
# in the code, instead of being scattered across the formula body.
_REQUIRED_NUMERIC_FIELDS = ("rainfall", "slope", "previous_landslide")


def predict_risk(data: dict) -> float:
    """
    Get a landslide risk score for the given location data.

    Args:
        data: Dictionary of location features as returned by
              backend.data_service.get_location_data(), e.g.
              {
                  "rainfall": 0,
                  "slope": 0,
                  "elevation": 0,
                  "previous_landslide": 0,
                  ...
              }

    Returns:
        A float risk score between 0 and 100 (inclusive).

    Raises:
        ValueError: If `data` is None, not a dictionary, or is missing/
            contains an invalid value for one of the fields the
            prediction layer requires.

    NOTE: This function's signature and return contract are STABLE.
    result_service.py depends on this exact interface. The scoring logic
    itself currently comes from a TEMPORARY MOCK (see _run_prediction
    below) and will later be swapped for a call into ml/predict.py
    without changing this function.
    """
    if not isinstance(data, dict):
        # Covers both None and any other non-dict input in one check --
        # isinstance(None, dict) is False, so None is already handled here.
        raise ValueError(
            "predict_risk() expects a location data dictionary, "
            f"got {type(data).__name__!r} instead."
        )

    return _run_prediction(data)


def _run_prediction(data: dict) -> float:
    """
    Internal integration boundary between the backend and the ML model.

    This is the ONLY function that should change when Member 2's real
    model becomes available. Right now it validates + extracts the
    features the mock formula needs and runs that formula; later it
    will instead call ml/predict.py's predict_risk_score(data).
    predict_risk() and result_service.py do not need to know which one
    is running -- both are expected to accept a `data` dict and return
    a float risk score in [0, 100], raising ValueError on bad input.

    NOTE: TEMPORARY MOCK LOGIC. This is NOT a trained ML model -- it is a
    simple, deterministic formula used only so the backend pipeline can
    be tested end-to-end.
    """
    features = _extract_features(data)
    return _mock_predict(features)


def _extract_features(data: dict) -> dict:
    """
    Pull the fields the current formula needs out of `data`, validating
    them along the way.

    A field that is simply absent (or explicitly None) is treated as
    "not provided" and defaults to 0, matching the historical mock
    behavior. A field that IS present but holds a value that can't be
    interpreted as a number (e.g. a string like "heavy") is a clean,
    reportable input error, so it raises ValueError rather than being
    silently coerced or left to blow up later as a TypeError inside the
    formula.

    Returns:
        A dict with numeric values for each of _REQUIRED_NUMERIC_FIELDS.

    Raises:
        ValueError: If a required field is present but not a valid number.
    """
    features = {}
    for field in _REQUIRED_NUMERIC_FIELDS:
        value = data.get(field)

        if value is None:
            features[field] = 0.0
            continue

        if isinstance(value, bool):
            # bool is technically an int subclass in Python; treat it as
            # an invalid prediction input rather than silently reading
            # True/False as 1/0.
            raise ValueError(
                f"predict_risk() received an invalid value for "
                f"'{field}': expected a number, got a bool ({value!r})."
            )

        try:
            features[field] = float(value)
        except (TypeError, ValueError):
            raise ValueError(
                f"predict_risk() received an invalid value for "
                f"'{field}': expected a number, got {value!r}."
            )

    return features


def _mock_predict(features: dict) -> float:
    """
    TEMPORARY MOCK FORMULA (placeholder only, not a trained model).

    Weighted, deterministic combination of a few features, scaled to
    0-100. This is the piece that gets deleted (in favor of a real
    ml/predict.py call) once Member 2 ships the actual model --
    everything else in this file stays as-is.
    """
    rainfall = features["rainfall"]
    slope = features["slope"]
    previous_landslide = features["previous_landslide"]

    score = (rainfall * 0.1) + (slope * 1.2) + (previous_landslide * 20)

    score = max(0.0, min(100.0, score))

    return round(score, 2)
