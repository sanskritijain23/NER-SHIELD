"""
ml/predict.py
-------------
Owner: Member 2 (ML)

Responsibility:
    Load the trained model (models/landslide_model.pkl) and expose a
    function that returns a risk probability/score for a given set of
    location features. This module is called by
    backend/prediction_service.py — it should NOT be called directly
    by the frontend or the map module.

NOTE: Placeholder only. No fake/random predictions are implemented.
"""

import os

# TODO (Member 2): import what you actually need once implementing, e.g.
# import joblib
# import numpy as np

MODEL_PATH = os.path.join("models", "landslide_model.pkl")

# Module-level cache for the loaded model so it isn't reloaded on every call.
_model = None


def load_model(model_path: str = MODEL_PATH):
    """
    Load the trained Scikit-learn model from disk.

    Args:
        model_path: Path to the saved model file
                    (default: models/landslide_model.pkl).

    Returns:
        The loaded Scikit-learn model object.

    TODO (Member 2): Implement using joblib.load(model_path).
    Consider caching the loaded model in the module-level `_model`
    variable so it is only loaded once per app run.
    """
    raise NotImplementedError("TODO: implement model loading with joblib.")


def predict_risk_score(features: dict) -> float:
    """
    Predict a landslide risk score/probability for a given location.

    Args:
        features: A dictionary of input features expected by the model,
                  e.g. {
                      "rainfall": 0,
                      "slope": 0,
                      "elevation": 0,
                      "previous_landslide": 0,
                  }

    Returns:
        A float risk score (e.g. probability between 0 and 1, or a
        0-100 scale — to be decided and documented by Member 2 and
        aligned with backend/risk_logic.py).

    TODO (Member 2):
        - Load the model (via load_model()) if not already loaded.
        - Convert `features` into the correct input shape/order for the model.
        - Run model.predict() / model.predict_proba().
        - Return a single numeric risk score.
    """
    raise NotImplementedError("TODO: implement real model-based prediction.")


if __name__ == "__main__":
    # PLACEHOLDER — manual smoke test entry point for Member 2 during development.
    print("ml/predict.py: prediction logic not implemented yet.")
