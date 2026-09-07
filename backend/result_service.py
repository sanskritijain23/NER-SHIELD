"""
backend/result_service.py
---------------------------
Owner: Member 4 (Backend)

Responsibility:
    The single public entry point of the backend package. Orchestrates:

        Dataset (data_service) -> ML Model (prediction_service)
            -> Risk Logic (risk_logic) -> Final Result dictionary

    The frontend (frontend/dashboard.py) and the map module
    (map/map_service.py) should ONLY consume the dictionary returned by
    generate_result() — they must never call data_service,
    prediction_service, or ml/ directly.

NOTE: Placeholder only. No fake/random results are generated.
"""

# TODO (Member 4): once the other backend modules are implemented, import them, e.g.
# from backend.data_service import get_location_data
# from backend.prediction_service import predict_risk
# from backend.risk_logic import get_risk_level, should_alert, get_recommended_action


def generate_result(location: str) -> dict:
    """
    Generate the full risk-assessment result for a given location.

    Args:
        location: Name of the location to assess.

    Returns:
        A dictionary following this exact format (see README.md):
        {
            "location": "",
            "latitude": 0,
            "longitude": 0,
            "rainfall": 0,
            "slope": 0,
            "elevation": 0,
            "previous_landslide": 0,
            "risk_score": 0,
            "risk_level": "",
            "alert": False,
            "recommended_action": "",
        }

    TODO (Member 4):
        1. Call data_service.get_location_data(location) to get raw features.
        2. Call prediction_service.predict_risk(location_data) to get a risk_score.
        3. Call risk_logic.get_risk_level(risk_score) to get a risk_level.
        4. Call risk_logic.should_alert(risk_level) to get an alert flag.
        5. Call risk_logic.get_recommended_action(risk_level) for the action text.
        6. Merge everything into the result dictionary above and return it.
    """
    raise NotImplementedError(
        "TODO: implement full pipeline orchestration and return the "
        "result dictionary in the documented format."
    )


# PLACEHOLDER: reference of the exact result dictionary shape, kept here
# for quick reference by other team members (frontend, map).
RESULT_TEMPLATE = {
    "location": "",
    "latitude": 0,
    "longitude": 0,
    "rainfall": 0,
    "slope": 0,
    "elevation": 0,
    "previous_landslide": 0,
    "risk_score": 0,
    "risk_level": "",
    "alert": False,
    "recommended_action": "",
}
