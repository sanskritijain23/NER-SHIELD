# Module 3 — GIS / Interactive Risk Map

Owner: Member 3.

Renders an interactive Folium map (OpenStreetMap tiles) of monitored
landslide-risk locations in the North Eastern Region (NER) of India, with
risk-colored markers, popups, and a legend.

## Files

| File                          | Purpose                                                              |
|--------------------------------|-----------------------------------------------------------------------|
| `map_service.py`               | Public API: dataset loading, risk classification, marker/legend/map construction. Framework-agnostic (no Streamlit imports). |
| `demo_app.py`                  | Standalone Streamlit demo (`streamlit run map/demo_app.py`) for building/testing/presenting this module on its own. |
| `data/prototype_locations.csv` | **Prototype / Historical-Simulated Dataset** — 10 NER locations with simulated rainfall, slope, previous-landslide status, and a pre-computed risk score/level/action. |

## Run the demo

```bash
pip install -r requirements.txt
streamlit run map/demo_app.py
```

## Run the tests

```bash
pytest tests/test_map_service.py
```

## Public API

```python
from map.map_service import (
    load_location_data,   # -> pd.DataFrame (bundled CSV by default)
    list_states,           # df -> list[str]
    filter_locations,      # df, state, location -> pd.DataFrame
    get_risk_level,        # score (0-100) -> "LOW" | "MEDIUM" | "HIGH" | "CRITICAL" | "UNKNOWN"
    get_risk_color,        # risk_level -> hex color string
    create_risk_map,       # data -> folium.Map (adds markers + legend)
    add_risk_marker,       # (folium.Map, record) -> bool
    get_dataset_label,     # -> "Prototype / Historical-Simulated Dataset"
)
```

## Future ML/backend integration

`create_risk_map()` and `add_risk_marker()` accept either a pandas
DataFrame (the bundled CSV shape, `Title_Case` columns) **or** a list of
plain dictionaries shaped like `backend.result_service.RESULT_TEMPLATE`
(`lower_snake_case` keys: `location`, `latitude`, `longitude`,
`risk_score`, `risk_level`, `rainfall`, `slope`, `previous_landslide`,
`recommended_action`). Both key styles are recognized automatically, so
once Member 4's backend is implemented, `frontend/dashboard.py` can call:

```python
from backend.data_service import list_available_locations
from backend.result_service import generate_result
from map.map_service import create_risk_map

results = [generate_result(name) for name in list_available_locations()]
risk_map = create_risk_map(results)
```

with no changes needed in `map_service.py`.

## Error handling

`load_location_data()` never crashes the app on bad data:

- Missing file / missing required column(s) -> raises `map_service.MapDataError`
  with a clear message (catch it and show `st.error(...)`).
- A row with missing/invalid latitude or longitude is dropped (it cannot
  be placed on a map).
- A row with an invalid/missing risk score is kept but classified as
  `"UNKNOWN"` (rendered as a gray marker) instead of raising.
