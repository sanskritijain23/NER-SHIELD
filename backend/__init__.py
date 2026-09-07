"""
backend package
----------------
Owner: Member 4 (Backend)

This package connects: Dataset -> ML Model -> Risk Logic -> Final Result.

Modules:
    data_service.py       - fetches location data
    prediction_service.py - calls ml/predict.py to get a risk score
    risk_logic.py          - converts a risk score into a risk level/alert/action
    result_service.py      - assembles the final result dictionary

Only backend/result_service.get_risk_result() (aliased as generate_result())
should be treated as the public entry point for the frontend and map modules.

STEP 1 STATUS: Foundation only. data_service and prediction_service use
clearly-marked TEMPORARY mock data/logic so the pipeline can be tested
end-to-end before Member 1's dataset and Member 2's trained model exist.

STEP 8 NOTE: Re-exports the existing public entry point so consumers can
use `from backend import get_risk_result` in addition to the previously
supported `from backend.result_service import get_risk_result`. This is
a pure re-export -- no logic lives here.
"""

from backend.result_service import get_risk_result

__all__ = ["get_risk_result"]
