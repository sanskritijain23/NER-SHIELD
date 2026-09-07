"""
app.py
------
Entry point of the NER-SHIELD prototype.

Responsibility:
    - This file ONLY coordinates the overall application flow.
    - It should launch/wire the Streamlit frontend.
    - It must NOT contain business logic, ML code, data processing
      code, or map-rendering code directly. All of that belongs to
      the respective modules (backend/, ml/, map/, frontend/).

Team ownership:
    - Shared file. Any member can adjust the wiring here, but please
      coordinate with the team before making structural changes.

How to run (once frontend is implemented):
    streamlit run app.py

How to run the API:
    uvicorn app:app --reload
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend import get_risk_result


def get_location_risk(location):
    return get_risk_result(location)


# TODO (Member 5 - Frontend / Integration):
#   Import and call the main dashboard render function from
#   frontend/dashboard.py once it is implemented, e.g.:
#
#   from frontend.dashboard import run_dashboard
#
#   if __name__ == "__main__":
#       run_dashboard()

# TODO (Member 4 - Backend):
#   If any startup/bootstrap logic is needed (e.g. loading config),
#   expose a simple function from backend/ and call it here — do not
#   inline backend logic in this file.


app = FastAPI(title="NER-SHIELD API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/api/risk/{location}")
def read_risk(location: str):
    try:
        return get_location_risk(location)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


def main():
    """
    Placeholder main function.

    Future implementation should:
        1. Initialize any required app-wide configuration.
        2. Launch the Streamlit dashboard defined in frontend/dashboard.py.

    Currently a no-op placeholder since the application is not built yet.
    """
    # PLACEHOLDER: Replace with a call to frontend.dashboard.run_dashboard()
    print("NER-SHIELD prototype scaffold. Frontend not yet implemented.")


if __name__ == "__main__":
    main()
