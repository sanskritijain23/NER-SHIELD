"""
backend/data_service.py
------------------------
Owner: Member 4 (Backend)

Responsibility:
    Fetch location data (rainfall, slope, elevation, previous_landslide,
    coordinates, etc.) for a given location name.

    This is the ONLY module that should read the processed dataset on
    behalf of the backend pipeline. Its job is strictly:

        Location -> Environmental Data

    It does NOT train/load ML models, compute risk scores, classify
    risk, generate alerts, or render maps.

======================== STEP 6 — REAL DATASET READY ============================
As of Step 6, this module is ready for the real processed dataset at:

    data/processed/landslide_data.csv

If that file exists, it is loaded (once, then cached) and used as the
active data source. Column names are matched flexibly (see
_CSV_COLUMN_ALIASES below) so small naming differences from the real
dataset (e.g. "lat" instead of "latitude") don't require touching this
file's core logic -- just the alias list.

If the CSV does NOT exist (still the case right now, per Member 1's
work-in-progress), this module transparently falls back to the same
IN-CODE MOCK DATASET (_MOCK_LOCATIONS) used since Step 1, so the rest of
the backend (prediction_service, risk_logic, result_service) keeps
working unchanged either way.

Real data and mock data are never combined for the same lookup: once the
real CSV is active, only the real CSV is consulted, even if a requested
location happens to share a name with a mock entry.

TODO (Member 4, later step, once Member 1's real CSV is finalized):
    - Confirm the CSV's actual column names match (or are covered by)
      _CSV_COLUMN_ALIASES below; add any new variants you see.
    - Nothing else in data_service.py (or any other backend file) needs
      to change; get_location_data() and list_available_locations()
      keep the same public behavior either way.
==================================================================================
"""

import os

# --- TEMPORARY / MOCK DATA (fallback, used while no real CSV exists) --------
# 2-3 sample locations, standing in for the real processed dataset.
# Values are illustrative/prototype-level only, NOT real measurements.
_MOCK_LOCATIONS = {
    "shillong": {
        "location": "Shillong",
        "latitude": 25.5788,
        "longitude": 91.8933,
        "rainfall": 320.5,       # mm (mock)
        "slope": 28.0,           # degrees (mock)
        "elevation": 1496.0,     # meters (mock)
        "previous_landslide": 1, # 1 = yes, 0 = no (mock)
    },
    "gangtok": {
        "location": "Gangtok",
        "latitude": 27.3389,
        "longitude": 88.6065,
        "rainfall": 410.2,
        "slope": 34.5,
        "elevation": 1650.0,
        "previous_landslide": 1,
    },
    "aizawl": {
        "location": "Aizawl",
        "latitude": 23.7271,
        "longitude": 92.7176,
        "rainfall": 180.0,
        "slope": 15.0,
        "elevation": 1132.0,
        "previous_landslide": 0,
    },
}

# Path to the real processed dataset, resolved relative to this file so it
# works no matter what directory the app is launched from.
_BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_BACKEND_DIR)
_CSV_PATH = os.path.join(_PROJECT_ROOT, "data", "processed", "landslide_data.csv")

# The fields the rest of the backend contract expects (when available).
_REQUIRED_FIELDS = [
    "location",
    "latitude",
    "longitude",
    "rainfall",
    "slope",
    "elevation",
    "previous_landslide",
]

# Fields that must be numeric once loaded (everything except "location").
_NUMERIC_FIELDS = [f for f in _REQUIRED_FIELDS if f != "location"]

# If the real CSV's column names differ from ours, list the accepted
# variants here instead of touching the CSV itself. Matching is
# case-insensitive. Only columns that actually exist in the CSV get
# mapped -- nothing here invents data that isn't present.
_CSV_COLUMN_ALIASES = {
    "location": ["location", "place", "location_name", "name"],
    "latitude": ["latitude", "lat"],
    "longitude": ["longitude", "lon", "long", "lng"],
    "rainfall": ["rainfall", "rain"],
    "slope": ["slope", "slope_degree", "slope_deg"],
    "elevation": ["elevation", "elev"],
    "previous_landslide": ["previous_landslide", "landslide"],
}

# Module-level cache so the CSV (if present) is only read from disk once
# per process, not on every get_location_data() call.
_csv_cache = None  # None = not loaded yet; {} = loaded but unusable/absent


def _normalize_name(name: str) -> str:
    """Normalize a location name for lookup/comparison purposes only."""
    return " ".join(str(name).strip().lower().split())


def _resolve_column_map(columns) -> dict:
    """
    Given the CSV's actual column names, figure out which canonical
    field (location, latitude, ...) each one corresponds to, using
    _CSV_COLUMN_ALIASES. Only fields that actually exist in the CSV are
    included in the result -- missing fields are simply left out rather
    than invented.
    """
    lower_to_actual = {str(col).strip().lower(): col for col in columns}

    resolved = {}
    for field, aliases in _CSV_COLUMN_ALIASES.items():
        for alias in aliases:
            if alias in lower_to_actual:
                resolved[field] = lower_to_actual[alias]
                break
    return resolved


def _load_csv_locations() -> dict:
    """
    Load and cache the real processed dataset, if present.

    Returns:
        A dict keyed by normalized location name, where each value is a
        dict of the *raw* (not yet type-converted) field values found in
        the CSV for that row -- only for fields whose columns actually
        exist. Returns {} if the CSV file doesn't exist, has no usable
        "location" column, or is otherwise not readable.

    NOTE: This function intentionally does NOT convert values to numeric
    types yet, and does not silently drop malformed rows. That happens
    per-lookup in get_location_data(), so a bad value somewhere in the
    CSV only raises an error if/when that specific location is actually
    requested, and so the failure message stays specific and honest
    about what went wrong rather than about the whole dataset.
    """
    global _csv_cache
    if _csv_cache is not None:
        return _csv_cache

    if not os.path.isfile(_CSV_PATH):
        _csv_cache = {}
        return _csv_cache

    import pandas as pd

    try:
        df = pd.read_csv(_CSV_PATH)
    except Exception as exc:
        # The file exists but genuinely can't be read (e.g. corrupt/empty
        # file). This is a real problem worth knowing about, not a
        # "no dataset yet" situation -- but we still don't want a broken
        # CSV to take down the whole app, so we fall back to mock data
        # and surface the reason via the exception message if needed by
        # a caller inspecting logs.
        raise RuntimeError(
            f"Found {_CSV_PATH} but could not read it as CSV: {exc}"
        ) from exc

    column_map = _resolve_column_map(df.columns)

    if "location" not in column_map:
        # Without a location column we have no way to key/look up rows,
        # so the real dataset can't be used at all.
        _csv_cache = {}
        return _csv_cache

    locations = {}
    loc_col = column_map["location"]
    for _, row in df.iterrows():
        raw_name = row[loc_col]
        name = "" if raw_name is None else str(raw_name).strip()
        if not name:
            continue

        entry = {"location": name}
        for field, actual_col in column_map.items():
            if field == "location":
                continue
            entry[field] = row[actual_col]

        locations[_normalize_name(name)] = entry

    _csv_cache = locations
    return _csv_cache


def _coerce_numeric(location: str, field: str, value) -> float:
    """
    Convert a raw CSV value for `field` to a numeric type, raising a
    clear, specific error (distinguishable from "unknown location") if
    the value is missing/unparseable rather than making up a number.
    """
    if value is None or (isinstance(value, float) and value != value):  # NaN check
        raise ValueError(
            f"Malformed data for location '{location}': "
            f"field '{field}' is missing a value in the dataset."
        )
    try:
        return float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(
            f"Malformed data for location '{location}': "
            f"field '{field}' has a non-numeric value ({value!r})."
        ) from exc


def _build_result_from_csv_entry(location: str, raw_entry: dict) -> dict:
    """
    Turn a raw (string/whatever) CSV row entry into the clean, typed
    dictionary the backend contract expects, converting only the fields
    that are actually present -- never inventing missing ones.
    """
    result = {"location": raw_entry["location"]}
    for field in _NUMERIC_FIELDS:
        if field not in raw_entry:
            continue  # column didn't exist in the CSV at all -- skip, don't invent
        numeric_value = _coerce_numeric(location, field, raw_entry[field])
        if field == "previous_landslide":
            result[field] = int(numeric_value)
        else:
            result[field] = numeric_value
    return result


def get_location_data(location: str) -> dict:
    """
    Fetch feature data for a given location.

    Args:
        location: Name of the location to look up. Matching is a simple
            normalized string match (trimmed, case-insensitive, extra
            inner whitespace collapsed) -- e.g. "Shillong", "shillong",
            and " SHILLONG " are all treated as the same location.

    Returns:
        A dictionary of feature data for the location. When available,
        it includes:
        {
            "location": str,
            "latitude": float,
            "longitude": float,
            "rainfall": float,
            "slope": float,
            "elevation": float,
            "previous_landslide": int,
        }

    Raises:
        ValueError: If `location` is invalid input, if the location is
            not found in the active dataset, or if the active dataset's
            data for that location is malformed (missing/non-numeric
            values) -- these are distinct, clearly-worded error cases.

    NOTE: Backed by the real CSV (data/processed/landslide_data.csv) when
    it exists and has a usable "location" column; otherwise falls back
    to _MOCK_LOCATIONS. The two sources are never mixed for a single
    lookup -- if the real CSV is active, an unmatched location is
    reported as unknown rather than silently pulled from mock data.
    """
    if not location or not isinstance(location, str):
        raise ValueError("A non-empty location name (string) is required.")

    key = _normalize_name(location)
    csv_locations = _load_csv_locations()

    if csv_locations:
        raw_entry = csv_locations.get(key)
        if raw_entry is None:
            raise ValueError(
                f"Unknown location: '{location}'. "
                f"Available locations: {list_available_locations()}"
            )
        return _build_result_from_csv_entry(raw_entry["location"], raw_entry)

    # No usable real dataset -- fall back to the mock dataset.
    data = _MOCK_LOCATIONS.get(key)
    if data is None:
        raise ValueError(
            f"Unknown location: '{location}'. "
            f"Available locations: {list_available_locations()}"
        )
    return dict(data)


def list_available_locations() -> list:
    """
    Return the list of all location names available in the current
    dataset.

    NOTE: Reflects whichever data source is currently active -- the real
    CSV (if present and usable) or the mock fallback dataset otherwise.
    """
    csv_locations = _load_csv_locations()
    if csv_locations:
        return [entry["location"] for entry in csv_locations.values()]
    return [entry["location"] for entry in _MOCK_LOCATIONS.values()]
