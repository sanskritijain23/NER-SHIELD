"""
backend/prediction_service.py
------------------------------
Owner: Member 4 (Backend)

Responsibility:
    Bridge between the backend and the ML module. Calls ml/predict.py
    to get a risk score for a given location's feature data. This is
    the ONLY module in the backend that should import from ml/.

NOTE: Placeholder only. No fake/random predictions are implemented.
"""

# TODO (Member 4): once ml/predict.py is implemented, import it, e.g.
# from ml.predict import predict_risk_score


def predict_risk(location_data: dict) -> float:
    """
    Get a risk score for the given location data by delegating to the
    ML module.

    Args:
        location_data: Dictionary of location features as returned by
                        backend.data_service.get_location_data(), e.g.
                        {
                            "rainfall": 0,
                            "slope": 0,
                            "elevation": 0,
                            "previous_landslide": 0,
                            ...
                        }

    Returns:
        A float risk score, to be interpreted by backend/risk_logic.py.

    TODO (Member 4):
        - Extract the exact features the ML model expects from
          `location_data`.
        - Call ml.predict.predict_risk_score(features) and return its result.
    """
    raise NotImplementedError(
        "TODO: implement call to ml.predict.predict_risk_score()."
    )
