"""
backend/result_service.py
---------------------------
Owner: Member 4 (Backend)

Responsibility:
    The single public entry point of the backend package. Orchestrates:

        data_service (location data) -> prediction_service (risk score)
            -> risk_logic (level / recommendation / alert) -> Final Result dict

    The frontend (frontend/dashboard.py) and the map module
    (map/map_service.py) should ONLY consume the dictionary returned by
    this module's public function -- they must never call data_service,
    prediction_service, or ml/ directly.

STEP 1 NOTE:
    data_service and prediction_service currently use TEMPORARY/MOCK data
    and logic (clearly marked in their own files). This module simply
    wires them together; it doesn't know or care that they're mocked.

STEP 5 NOTE -- STABLE RESULT CONTRACT:
    This step stabilizes the final result contract so future frontend,
    map, and alert code can depend on it without surprises:

    - Success:
        {
            "location": str,
            "latitude": float,
            "longitude": float,
            "risk_score": float,
            "risk_level": str,
            "rainfall": float,
            "slope": float,
            "elevation": float,
            "previous_landslide": int,
            "recommendation": str,
            "alert": bool,
        }

    - Unknown location (clean, non-crashing error result):
        {
            "location": str,
            "error": str,
        }

    - Invalid input (e.g. None, or a non-string location): raises
      ValueError. This is a caller/programming error, not a normal
      "location not found" case, so it is not swallowed into a result
      dict.

    This module remains a pure orchestrator: it does not compute the ML
    score, duplicate risk thresholds, or reimplement any classification
    logic. All of that stays in data_service, prediction_service, and
    risk_logic.
"""

from backend.data_service import get_location_data
from backend.prediction_service import predict_risk
from backend.risk_logic import get_risk_level, get_recommendation, is_alert_required


def get_risk_result(location: str) -> dict:
    """
    Generate the full risk-assessment result for a given location.

    Pipeline:
        location
           -> get_location_data()
           -> predict_risk()
           -> get_risk_level() / get_recommendation() / is_alert_required()
           -> final result dictionary

    Args:
        location: Name of the location to assess.

    Returns:
        A dictionary with the stable structure:
        {
            "location": str,
            "latitude": float,
            "longitude": float,
            "risk_score": float,
            "risk_level": str,
            "rainfall": float,
            "slope": float,
            "elevation": float,
            "previous_landslide": int,
            "recommendation": str,
            "alert": bool,
        }

        If the location is unknown, returns an error result instead of
        raising, so callers (frontend/map) can handle it cleanly:
        {
            "location": str,
            "error": str,
        }

    Raises:
        ValueError: If `location` is clearly invalid input (e.g. None or
            a non-string value). This is distinct from an unknown
            location, which is handled as a clean error result above.
    """
    if location is None or not isinstance(location, str):
        raise ValueError(
            "location must be a non-empty string, "
            f"got {type(location).__name__!r} instead."
        )

    try:
        location_data = get_location_data(location)
    except ValueError as exc:
        # Unknown/not-found location: handled cleanly instead of an
        # obscure crash, so frontend/map can display it gracefully.
        return {
            "location": location,
            "error": str(exc),
        }

    risk_score = predict_risk(location_data)

    risk_level = get_risk_level(risk_score)
    recommendation = get_recommendation(risk_score)
    alert = is_alert_required(risk_score)

    return {
        "location": location_data["location"],
        "latitude": location_data["latitude"],
        "longitude": location_data["longitude"],
        "risk_score": risk_score,
        "risk_level": risk_level,
        "rainfall": location_data["rainfall"],
        "slope": location_data["slope"],
        "elevation": location_data["elevation"],
        "previous_landslide": location_data["previous_landslide"],
        "recommendation": recommendation,
        "alert": alert,
    }


# Alias kept for compatibility with the name referenced elsewhere in the
# project scaffold (frontend/dashboard.py, map/map_service.py, README.md).
generate_result = get_risk_result


if __name__ == "__main__":
    # Small manual smoke test (not a full test framework).
    import json

    sample = get_risk_result("Shillong")
    print(json.dumps(sample, indent=2))

    unknown = get_risk_result("Nowhere")
    print(json.dumps(unknown, indent=2))
