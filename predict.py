import joblib
import pandas as pd
from pathlib import Path


# ============================================================
# MODEL PATH
# ============================================================

MODEL_PATH = Path(__file__).parent / "landslide_random_forest_model.pkl"


# ============================================================
# LOAD MODEL
# ============================================================

def load_model():

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}"
        )

    model_data = joblib.load(MODEL_PATH)

    model = model_data["model"]
    features = model_data["features"]

    return model, features


# ============================================================
# PREDICTION FUNCTION
# ============================================================

def predict_landslide_risk(
    rainfall_1day,
    rainfall_3day,
    rainfall_7day,
    elevation,
    slope,
    previous_landslide
):

    # Load trained Random Forest
    model, features = load_model()


    # --------------------------------------------------------
    # CREATE INPUT DATA
    # --------------------------------------------------------

    input_data = pd.DataFrame([{

        "Rainfall_1day_mm": rainfall_1day,

        "Rainfall_3day_mm": rainfall_3day,

        "Rainfall_7day_mm": rainfall_7day,

        "Elevation_m": elevation,

        "Slope_degrees": slope,

        "Previous_Landslide": previous_landslide

    }])


    # --------------------------------------------------------
    # ENSURE EXACT TRAINING FEATURE ORDER
    # --------------------------------------------------------

    input_data = input_data[features]


    # --------------------------------------------------------
    # MODEL PREDICTION
    # --------------------------------------------------------

    prediction = int(
        model.predict(input_data)[0]
    )


    # --------------------------------------------------------
    # PREDICT PROBABILITY
    # --------------------------------------------------------

    probability = float(
        model.predict_proba(input_data)[0][1]
    )


    # --------------------------------------------------------
    # CONVERT TO RISK SCORE
    # --------------------------------------------------------

    risk_score = probability * 100


    # --------------------------------------------------------
    # RISK LEVEL
    # --------------------------------------------------------

    if risk_score <= 30:

        risk_level = "LOW"

    elif risk_score <= 60:

        risk_level = "MEDIUM"

    elif risk_score <= 80:

        risk_level = "HIGH"

    else:

        risk_level = "CRITICAL"


    # --------------------------------------------------------
    # RETURN RESULTS
    # --------------------------------------------------------

    return {

        "prediction": prediction,

        "probability": probability,

        "risk_score": risk_score,

        "risk_level": risk_level

    }


# ============================================================
# TEST WHEN RUN DIRECTLY
# ============================================================

if __name__ == "__main__":

    result = predict_landslide_risk(

        rainfall_1day=55.0,

        rainfall_3day=125.0,

        rainfall_7day=220.0,

        elevation=1496.0,

        slope=0.85,

        previous_landslide=1

    )

    print("\nLandslide Prediction Test")
    print("--------------------------")

    print(
        f"Prediction: {result['prediction']}"
    )

    print(
        f"Probability: {result['probability']:.4f}"
    )

    print(
        f"Risk Score: {result['risk_score']:.2f}/100"
    )

    print(
        f"Risk Level: {result['risk_level']}"
    )