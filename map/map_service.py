"""
map/map_service.py
--------------------
Owner: Member 3 (Map / GIS)

Responsibility:
    Render a Folium map (with OpenStreetMap tiles) showing landslide
    risk information for one or more locations.

Input:
    A result dictionary (or list of them) coming from
    backend/result_service.generate_result(), containing at least:
        location, latitude, longitude, risk_score, risk_level,
        rainfall, slope, elevation

IMPORTANT:
    - This module must NOT import from ml/ or call the ML model directly.
    - It only receives already-processed data from the backend.

NOTE: Placeholder only. No map rendering logic is implemented yet.
"""

# TODO (Member 3): once implementing, import what you need, e.g.
# import folium

# Default map center — roughly centered on the North Eastern Region of India.
# TODO (Member 3): adjust/verify this default center & zoom as needed.
DEFAULT_MAP_CENTER = (26.2006, 92.9376)  # approx. center of NE India
DEFAULT_ZOOM_START = 6


def render_map(results, center: tuple = DEFAULT_MAP_CENTER, zoom_start: int = DEFAULT_ZOOM_START):
    """
    Build a Folium map with markers for the given location result(s).

    Args:
        results: A single backend result dictionary, or a list of them
                 (see module docstring for expected keys).
        center: (latitude, longitude) tuple for the initial map view.
        zoom_start: Initial zoom level for the map.

    Returns:
        A folium.Map object ready to be embedded in the Streamlit
        frontend (e.g. via streamlit-folium).

    TODO (Member 3):
        1. Create a folium.Map(location=center, zoom_start=zoom_start)
           using OpenStreetMap tiles (folium's default).
        2. For each result in `results`, add a marker at
           (latitude, longitude) with a popup/tooltip showing:
           location, risk_level, risk_score, rainfall, slope, elevation.
        3. Optionally color-code markers by risk_level
           (e.g. green/yellow/orange/red).
        4. Return the folium.Map object.
    """
    raise NotImplementedError("TODO: implement Folium map rendering.")
