# NER-SHIELD

**AI-Based Early Warning and Landslide Risk Monitoring System for the North Eastern Region of India.**

Zero-budget software prototype built with Python, Streamlit, Scikit-learn, and Folium/OpenStreetMap.

> ⚠️ Status: **Project structure / scaffold only.** No business logic has been implemented yet.
> Every module contains placeholder functions and docstrings marking what needs to be built.

---

## 1. Tech Stack

| Layer      | Technology                     |
|------------|---------------------------------|
| Frontend   | Streamlit                       |
| Backend    | Plain Python (service modules)  |
| ML         | Scikit-learn                    |
| Map / GIS  | Folium + OpenStreetMap          |
| Data       | CSV files (`data/`)             |

---

## 2. Project Structure

```
NER-SHIELD/
│
├── app.py                     # Coordinates frontend + app flow ONLY
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── raw/                   # Untouched source data (Member 1)
│   └── processed/             # Cleaned dataset -> landslide_data.csv
│
├── models/                    # Saved trained ML model(s) (Member 2)
│
├── ml/
│   ├── train_model.py         # Trains model on processed data (Member 2)
│   └── predict.py             # Loads model, returns risk score (Member 2)
│
├── backend/
│   ├── __init__.py
│   ├── data_service.py        # Fetches location data (Member 4)
│   ├── prediction_service.py  # Calls ml/predict.py (Member 4)
│   ├── risk_logic.py          # Converts score -> risk level/alert (Member 4)
│   └── result_service.py      # Builds final result dictionary (Member 4)
│
├── frontend/
│   └── dashboard.py           # Streamlit UI (Member 5)
│
├── map/
│   └── map_service.py         # Folium map rendering (Member 3)
│
└── tests/                     # Testing & integration (Member 6)
```

---

## 3. Architecture Rules (please follow strictly)

1. Keep modules independent and loosely coupled.
2. Do **not** put all code inside `app.py`. It only coordinates the frontend/app flow.
3. The frontend must **not** directly read ML models — it must go through the backend.
4. The map must **not** directly call the ML model — it only receives data from the backend.
5. All data must flow through the backend: `Dataset → ML Model → Risk Logic → Final Result`.
6. Use clean, relative Python imports and project-relative paths (no hardcoded absolute paths).
7. Add comments / docstrings for placeholder code so teammates know what's pending.
8. No fake/mocked ML predictions or randomly generated data — leave a clear `TODO` instead.

### Data flow (target architecture)

```
data/processed/landslide_data.csv
        │
        ▼
   ml/train_model.py  ──►  models/landslide_model.pkl
        │
        ▼
   ml/predict.py  (loads model, returns risk score)
        │
        ▼
backend/prediction_service.py
        │
        ▼
backend/risk_logic.py  (score -> risk level, alert, action)
        │
        ▼
backend/result_service.py  (builds final result dict)
        │
        ▼
frontend/dashboard.py  ◄──►  map/map_service.py
   (both consume the backend's result dictionary — never the raw model)
```

---

## 4. Team Responsibilities

### Member 1 — Data
- Owns: `data/`
- Deliverable: `data/processed/landslide_data.csv`

### Member 2 — ML
- Owns: `ml/`, `models/`
- Input: `data/processed/landslide_data.csv`
- Output: `models/landslide_model.pkl`
- Must expose a risk probability/score for the backend to consume.

### Member 3 — Map / GIS
- Owns: `map/`
- Uses Folium + OpenStreetMap.
- Expects backend-provided fields: `location`, `latitude`, `longitude`, `risk_score`,
  `risk_level`, `rainfall`, `slope`, `elevation`.

### Member 4 — Backend
- Owns: `backend/`
- Connects Dataset → ML Model → Risk Logic → Final Result.
- Final result dictionary format:

```python
{
    "location": "",
    "latitude": 0,
    "longitude": 0,
    "rainfall": 0,
    "slope": 0,
    "elevation": 0,
    "previous_landslide": 0,
    "risk_score": 0,
    "risk_level": "",
    "alert": False,
    "recommended_action": ""
}
```

### Member 5 — Frontend
- Owns: `frontend/`
- Uses Streamlit to: select a location, call the backend, and display
  risk score, risk level, rainfall/slope/elevation, alert, recommended
  action, and the map.

### Member 6 — Testing & Integration
- Owns: `tests/`
- Responsible for integration checks between modules and overall QA.

---

## 5. Getting Started

```bash
# 1. Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app (once frontend is implemented)
streamlit run app.py
```

## 6. Next Steps

This repository currently contains **only the folder structure and placeholder
modules**. Each member should:
1. Pick up their assigned module(s) above.
2. Implement the functions marked with `TODO` / `NotImplementedError`.
3. Keep interfaces (function names & the result dictionary format) unchanged
   so other members' modules keep working.
4. Coordinate through `tests/` for integration checks.
