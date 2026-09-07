"""
map package
------------
Owner: Member 3 (Map / GIS)

Renders the interactive Folium/OpenStreetMap risk map for NER-SHIELD.

Modules:
    map_service.py - dataset loading, risk classification, marker/legend
                      construction, and folium.Map creation.
    demo_app.py     - standalone Streamlit demo (`streamlit run map/demo_app.py`)
                      used to build/test this module independently of the
                      ML and backend modules.

Public entry point: map.map_service.create_risk_map().
"""
