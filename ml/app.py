import streamlit as st
import pandas as pd
from pathlib import Path

# Import prediction function from predict.py
from predict import predict_landslide_risk


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Landslide Risk Monitoring System",
    page_icon="⛰️",
    layout="wide"
)


# ============================================================
# PROTOTYPE LOCATION DATA
# ============================================================
# IMPORTANT:
# These are prototype/demo environmental values.
# They are automatically selected based on the chosen location.
#
# In the future, these values can be replaced by:
# - Live rainfall API
# - DEM/elevation data
# - GIS-derived slope
# - Historical landslide database
# ============================================================

LOCATION_DATA = {

    "Shillong, Meghalaya": {
        "latitude": 25.5788,
        "longitude": 91.8933,
        "rainfall_1day": 55.0,
        "rainfall_3day": 125.0,
        "rainfall_7day": 220.0,
        "elevation": 1496.0,
        "slope": 0.85,
        "previous_landslide": 1
    },

    "Gangtok, Sikkim": {
        "latitude": 27.3389,
        "longitude": 88.6065,
        "rainfall_1day": 75.0,
        "rainfall_3day": 180.0,
        "rainfall_7day": 310.0,
        "elevation": 1650.0,
        "slope": 1.15,
        "previous_landslide": 1
    },

    "Aizawl, Mizoram": {
        "latitude": 23.7271,
        "longitude": 92.7176,
        "rainfall_1day": 68.0,
        "rainfall_3day": 155.0,
        "rainfall_7day": 285.0,
        "elevation": 1100.0,
        "slope": 1.05,
        "previous_landslide": 1
    },

    "Kohima, Nagaland": {
        "latitude": 25.6751,
        "longitude": 94.1086,
        "rainfall_1day": 62.0,
        "rainfall_3day": 145.0,
        "rainfall_7day": 265.0,
        "elevation": 1444.0,
        "slope": 0.95,
        "previous_landslide": 1
    },

    "Itanagar, Arunachal Pradesh": {
        "latitude": 27.0844,
        "longitude": 93.6053,
        "rainfall_1day": 82.0,
        "rainfall_3day": 195.0,
        "rainfall_7day": 340.0,
        "elevation": 750.0,
        "slope": 1.20,
        "previous_landslide": 1
    },

    "Imphal, Manipur": {
        "latitude": 24.8170,
        "longitude": 93.9368,
        "rainfall_1day": 42.0,
        "rainfall_3day": 105.0,
        "rainfall_7day": 185.0,
        "elevation": 790.0,
        "slope": 0.55,
        "previous_landslide": 0
    },

    "Agartala, Tripura": {
        "latitude": 23.8315,
        "longitude": 91.2868,
        "rainfall_1day": 38.0,
        "rainfall_3day": 92.0,
        "rainfall_7day": 165.0,
        "elevation": 25.0,
        "slope": 0.25,
        "previous_landslide": 0
    },

    "Guwahati, Assam": {
        "latitude": 26.1445,
        "longitude": 91.7362,
        "rainfall_1day": 48.0,
        "rainfall_3day": 115.0,
        "rainfall_7day": 205.0,
        "elevation": 55.0,
        "slope": 0.45,
        "previous_landslide": 0
    }
}


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📍 Location Selection")

# ------------------------------------------------------------
# STATE → LOCATIONS
# ------------------------------------------------------------

STATE_LOCATIONS = {
    "Arunachal Pradesh": [
        "Itanagar"
    ],
    "Assam": [
        "Guwahati"
    ],
    "Manipur": [
        "Imphal"
    ],
    "Meghalaya": [
        "Shillong"
    ],
    "Mizoram": [
        "Aizawl"
    ],
    "Nagaland": [
        "Kohima"
    ],
    "Sikkim": [
        "Gangtok"
    ],
    "Tripura": [
        "Agartala"
    ]
}


# ------------------------------------------------------------
# STATE SELECTION
# ------------------------------------------------------------

state = st.sidebar.selectbox(
    "Select State",
    list(STATE_LOCATIONS.keys())
)


# ------------------------------------------------------------
# LOCATION SELECTION
# ------------------------------------------------------------

available_locations = STATE_LOCATIONS[state]

selected_city = st.sidebar.selectbox(
    "Select Location",
    available_locations
)


# ------------------------------------------------------------
# CREATE FULL LOCATION NAME
# ------------------------------------------------------------

location = f"{selected_city}, {state}"


# ------------------------------------------------------------
# GET ENVIRONMENTAL DATA
# ------------------------------------------------------------

data = LOCATION_DATA[location]


# ============================================================
# HEADER
# ============================================================

st.title("⛰️ AI-Based Landslide Risk Monitoring System")

st.subheader("Northeast India — Early Warning Prototype")

st.info(
    "Select a location. The system automatically uses the prototype "
    "environmental conditions for that location and sends them to "
    "the trained Random Forest model."
)


# ============================================================
# LOCATION INFORMATION
# ============================================================

st.header(f"📍 {location}")

location_col1, location_col2 = st.columns(2)

with location_col1:
    st.metric(
        "Latitude",
        f"{data['latitude']:.4f}"
    )

with location_col2:
    st.metric(
        "Longitude",
        f"{data['longitude']:.4f}"
    )


st.divider()


# ============================================================
# AUTOMATIC ENVIRONMENTAL DATA
# ============================================================

st.header("🌧️ Environmental Conditions")

st.caption(
    "Automatically selected for the chosen location — "
    "the user does not manually enter these values."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Rainfall — 24 Hours",
        f"{data['rainfall_1day']:.1f} mm"
    )

with col2:
    st.metric(
        "Rainfall — 3 Days",
        f"{data['rainfall_3day']:.1f} mm"
    )

with col3:
    st.metric(
        "Rainfall — 7 Days",
        f"{data['rainfall_7day']:.1f} mm"
    )


col4, col5, col6 = st.columns(3)

with col4:
    st.metric(
        "Elevation",
        f"{data['elevation']:.0f} m"
    )

with col5:
    st.metric(
        "Slope",
        f"{data['slope']:.2f}°"
    )

with col6:
    previous_text = (
        "Yes"
        if data["previous_landslide"] == 1
        else "No"
    )

    st.metric(
        "Previous Landslide",
        previous_text
    )


st.divider()


# ============================================================
# ANALYZE BUTTON
# ============================================================

if st.button(
    "🔍 ANALYZE LANDSLIDE RISK",
    use_container_width=True,
    type="primary"
):

    try:

        # ----------------------------------------------------
        # SEND AUTOMATIC ENVIRONMENTAL DATA TO MODEL
        # ----------------------------------------------------

        result = predict_landslide_risk(
            rainfall_1day=data["rainfall_1day"],
            rainfall_3day=data["rainfall_3day"],
            rainfall_7day=data["rainfall_7day"],
            elevation=data["elevation"],
            slope=data["slope"],
            previous_landslide=data["previous_landslide"]
        )


        # ----------------------------------------------------
        # READ RESULT
        # ----------------------------------------------------

        prediction = result["prediction"]
        probability = result["probability"]
        risk_score = result["risk_score"]
        risk_level = result["risk_level"]


        # ----------------------------------------------------
        # RECOMMENDATION
        # ----------------------------------------------------

        if risk_level == "CRITICAL":

            recommendation = (
                "Immediate field inspection and emergency "
                "preparedness are recommended."
            )

        elif risk_level == "HIGH":

            recommendation = (
                "Close monitoring and field inspection "
                "are recommended."
            )

        elif risk_level == "MEDIUM":

            recommendation = (
                "Increase monitoring of the area and "
                "observe rainfall and terrain conditions."
            )

        else:

            recommendation = (
                "Normal monitoring is recommended."
            )


        # ====================================================
        # RISK ASSESSMENT
        # ====================================================

        st.header("🚨 Risk Assessment")


        result_col1, result_col2, result_col3 = st.columns(3)


        with result_col1:

            st.metric(
                "Risk Score",
                f"{risk_score:.1f} / 100"
            )


        with result_col2:

            st.metric(
                "Risk Level",
                risk_level
            )


        with result_col3:

            if prediction == 1:

                prediction_text = "LANDSLIDE RISK"

            else:

                prediction_text = "NO LANDSLIDE"


            st.metric(
                "AI Prediction",
                prediction_text
            )


        # ====================================================
        # VISUAL WARNING
        # ====================================================

        if risk_level == "CRITICAL":

            st.error(
                "🚨 CRITICAL LANDSLIDE RISK — "
                "Immediate attention required!"
            )

        elif risk_level == "HIGH":

            st.warning(
                "⚠️ HIGH LANDSLIDE RISK — "
                "Close monitoring recommended."
            )

        elif risk_level == "MEDIUM":

            st.warning(
                "🟡 MEDIUM LANDSLIDE RISK — "
                "Continue monitoring."
            )

        else:

            st.success(
                "🟢 LOW LANDSLIDE RISK — "
                "Normal monitoring."
            )


        # ====================================================
        # RISK SCORE BAR
        # ====================================================

        st.subheader("📊 Risk Indicator")

        st.progress(
            min(max(int(risk_score), 0), 100)
        )


        # ====================================================
        # RECOMMENDED ACTION
        # ====================================================

        st.subheader("📋 Recommended Action")

        st.info(recommendation)


        # ====================================================
        # ANALYSIS FACTORS
        # ====================================================

        st.subheader("🔎 Analysis Factors")


        factor_data = pd.DataFrame({

            "Factor": [
                "Location",
                "Rainfall — 24 Hours",
                "Rainfall — 3 Days",
                "Rainfall — 7 Days",
                "Elevation",
                "Slope",
                "Previous Landslide"
            ],

            "Value": [
                location,
                f"{data['rainfall_1day']:.1f} mm",
                f"{data['rainfall_3day']:.1f} mm",
                f"{data['rainfall_7day']:.1f} mm",
                f"{data['elevation']:.0f} m",
                f"{data['slope']:.2f}°",
                previous_text
            ]
        })


        st.dataframe(
            factor_data,
            use_container_width=True,
            hide_index=True
        )


        # ====================================================
        # MODEL INFORMATION
        # ====================================================

        with st.expander("🤖 AI Model Information"):

            st.write(
                "Model: Random Forest Classifier"
            )

            st.write(
                f"Model probability: {probability:.4f}"
            )

            st.write(
                "The risk score is calculated from the "
                "model's predicted probability for the "
                "landslide class."
            )

            st.caption(
                "Prototype limitation: the current model was "
                "trained using synthetic target labels for "
                "demonstration. It is not a scientifically "
                "validated operational landslide forecasting model."
            )


    except FileNotFoundError:

        st.error(
            "❌ Trained model file not found."
        )

        st.info(
            "Make sure these files are in the same folder:\n\n"
            "app.py\n"
            "predict.py\n"
            "landslide_random_forest_model.pkl"
        )


    except Exception as e:

        st.error(
            f"❌ Prediction error: {e}"
        )

        st.info(
            "Check that predict.py and the trained .pkl model "
            "use the same feature names and prediction interface."
        )


# ============================================================
# FUTURE SCOPE
# ============================================================

st.divider()

with st.expander("🚀 Future Scope"):

    st.write(
        """
        • Live rainfall data integration

        • Satellite imagery integration

        • DEM-based terrain analysis

        • Real-time GIS risk maps

        • Historical landslide database integration

        • SMS and mobile alerts

        • Citizen geo-tagged reports

        • Multilingual notifications

        • Offline/low-network support
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "SIH Prototype | AI-Based Early Warning and Landslide Risk "
    "Monitoring System | Prototype model uses synthetic training "
    "labels for demonstration."
)