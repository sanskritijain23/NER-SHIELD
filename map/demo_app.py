"""
map/demo_app.py
-----------------
Owner: Member 3 (Map / GIS)

Purpose:
    A small, self-contained Streamlit demo for the GIS / Interactive Risk
    Map module (map/map_service.py). It lets Member 3 build, test and
    present the map independently of the ML (ml/) and backend
    (backend/) modules, which are still being implemented by other
    team members.

    It reads the bundled prototype dataset (map/data/prototype_locations.csv)
    directly. Once backend/result_service.py is implemented, the real
    frontend/dashboard.py will instead loop over
    backend.data_service.list_available_locations(), call
    backend.result_service.generate_result(location) for each one, and
    pass those result dictionaries straight into map.map_service.create_risk_map()
    — the map module already accepts that shape (see map_service.py).

How to run:
    streamlit run map/demo_app.py
"""

import os
import sys

import streamlit as st
from streamlit_folium import st_folium

# Allow running this file directly (streamlit run map/demo_app.py) by making
# sure the project root is on sys.path so `import map.map_service` resolves.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from map import map_service  # noqa: E402


def _risk_badge(risk_level: str) -> str:
    color = map_service.get_risk_color(risk_level)
    return (
        f'<span style="background-color:{color}; color:#111; padding:4px 14px; '
        f'border-radius:14px; font-weight:bold;">{risk_level}</span>'
    )


def main() -> None:
    st.set_page_config(page_title="NER-SHIELD | Risk Map", layout="wide")

    st.title("AI-Based Landslide Risk Monitoring System")
    st.caption("Northeast Region — GIS / Interactive Risk Map module (Member 3 demo)")

    try:
        locations_df = map_service.load_location_data()
    except map_service.MapDataError as error:
        st.error(f"Could not load the location dataset: {error}")
        st.stop()

    if locations_df.empty:
        st.warning("The location dataset is empty — no locations to display.")
        st.stop()

    st.info(f"Dataset: **{map_service.get_dataset_label()}** — values are simulated for prototype purposes only.")

    # ---------------------------------------------------------------- Sidebar
    st.sidebar.header("Filters")

    states = ["All"] + map_service.list_states(locations_df)
    selected_state = st.sidebar.selectbox("Select State", states)

    locations_in_state = map_service.filter_locations(locations_df, state=selected_state)
    location_names = ["All"] + sorted(locations_in_state["Location"].unique().tolist())
    selected_location = st.sidebar.selectbox("Select Location", location_names)

    analyze_clicked = st.sidebar.button("Analyze Risk", use_container_width=True)

    filtered_df = map_service.filter_locations(locations_df, state=selected_state, location=selected_location)
    if filtered_df.empty:
        filtered_df = locations_in_state if not locations_in_state.empty else locations_df

    # ------------------------------------------------------------ Main layout
    map_col, info_col = st.columns([2, 1])

    with info_col:
        st.subheader("Risk Summary")

        focus_row = None
        if selected_location != "All" and not filtered_df.empty:
            focus_row = filtered_df.iloc[0]
        elif analyze_clicked and not filtered_df.empty:
            focus_row = filtered_df.iloc[0]

        if focus_row is not None:
            st.markdown(f"**Location:** {focus_row['Location']} ({focus_row['District']}, {focus_row['State']})")
            st.markdown(_risk_badge(focus_row["Risk_Level"]), unsafe_allow_html=True)
            st.metric("Risk Score", f"{focus_row['Risk_Score']:.0f} / 100")

            st.markdown("**Risk Factors**")
            st.write(f"- Rainfall (24h): {focus_row['Rainfall_24h_mm']:.0f} mm")
            st.write(f"- Rainfall (3-day): {focus_row['Rainfall_3day_mm']:.0f} mm")
            st.write(f"- Slope: {focus_row['Slope_degree']:.0f}°")
            st.write(f"- Previous Landslide: {focus_row['Previous_Landslide']}")

            st.markdown("**Recommended Action**")
            st.warning(focus_row["Recommended_Action"])
        else:
            st.write("Select a state and location in the sidebar, then click **Analyze Risk** "
                     "for a detailed summary. All monitored locations are shown on the map.")

        st.divider()
        st.subheader("Legend")
        for level in map_service.RISK_LEVELS:
            st.markdown(f"{_risk_badge(level)} &nbsp; {level.title()}", unsafe_allow_html=True)

    with map_col:
        st.subheader("Interactive Risk Map")
        risk_map = map_service.create_risk_map(filtered_df)
        st_folium(risk_map, height=560, use_container_width=True, returned_objects=[])

    st.divider()
    with st.expander("View raw monitored-location data"):
        st.dataframe(locations_df, use_container_width=True)


if __name__ == "__main__":
    main()
