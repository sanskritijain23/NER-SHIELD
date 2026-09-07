"""
backend package
----------------
Owner: Member 4 (Backend)

This package connects: Dataset -> ML Model -> Risk Logic -> Final Result.

Modules:
    data_service.py       - fetches raw/processed location data
    prediction_service.py - calls ml/predict.py to get a risk score
    risk_logic.py          - converts a risk score into a risk level/alert/action
    result_service.py      - assembles the final result dictionary

Only backend/result_service.generate_result() should be treated as the
public entry point for the frontend and map modules.
"""
