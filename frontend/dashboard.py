"""
frontend/dashboard.py
-----------------------
Owner: Member 5 (Frontend)

Responsibility:
    Streamlit UI for NER-SHIELD. Should:
        - Let the user select a location.
        - Call backend.result_service.generate_result(location) to get
          the full result dictionary.
        - Display: risk score, risk level, rainfall, slope, elevation,
          alert, recommended action.
        - Display the map (via map/map_service.py).

IMPORTANT:
    - This module must NOT import from ml/ or read models/*.pkl directly.
    - It must only go through backend/result_service.py for data + risk info,
      and through map/map_service.py for the map.

NOTE: Placeholder only. No UI logic is implemented yet.
"""

# TODO (Member 5): once implementing, import what you need, e.g.
# import streamlit as st
# from backend.result_service import generate_result
# from backend.data_service import list_available_locations
# from map.map_service import render_map


def run_dashboard():
    """
    Main entry point for the Streamlit dashboard. Called from app.py.

    TODO (Member 5):
        1. Set page config / title (st.set_page_config, st.title).
        2. Get the list of available locations
           (backend.data_service.list_available_locations()) and show a
           st.selectbox for the user to choose one.
        3. On selection, call backend.result_service.generate_result(location).
        4. Display the result fields (risk score, risk level, rainfall,
           slope, elevation, alert banner, recommended action).
        5. Call map.map_service.render_map(result) and embed it
           (e.g. via streamlit-folium's st_folium/folium_static).
    """
    # PLACEHOLDER — replace with real Streamlit UI code.
    raise NotImplementedError("TODO: implement the Streamlit dashboard UI.")


if __name__ == "__main__":
    # Allows running this file directly with: streamlit run frontend/dashboard.py
    run_dashboard()
