"""
backend/data_service.py
------------------------
Owner: Member 4 (Backend)

Responsibility:
    Fetch location data (rainfall, slope, elevation, previous_landslide,
    coordinates, etc.) for a given location name, sourced from
    data/processed/landslide_data.csv (produced by Member 1).

    This is the ONLY module that should read the processed dataset on
    behalf of the backend pipeline.

NOTE: Placeholder only. No fake/random data is generated here.
"""

import os

# TODO (Member 4): import what you actually need once implementing, e.g.
# import pandas as pd

PROCESSED_DATA_PATH = os.path.join("data", "processed", "landslide_data.csv")


def get_location_data(location: str) -> dict:
    """
    Fetch feature data for a given location.

    Args:
        location: Name of the location to look up (must match an entry
                  in the processed dataset).

    Returns:
        A dictionary of raw feature data for the location, e.g.:
        {
            "location": "",
            "latitude": 0,
            "longitude": 0,
            "rainfall": 0,
            "slope": 0,
            "elevation": 0,
            "previous_landslide": 0,
        }

    TODO (Member 4):
        - Load data/processed/landslide_data.csv (likely via pandas).
        - Look up the row matching `location`.
        - Return its fields as a dictionary.
        - Handle the case where the location is not found.
    """
    raise NotImplementedError(
        "TODO: implement lookup of location data from the processed CSV."
    )


def list_available_locations() -> list:
    """
    Return the list of all location names available in the processed dataset.

    Used by the frontend to populate a location selection dropdown.

    TODO (Member 4): Implement by reading the processed CSV and
    returning the unique list of location names.
    """
    raise NotImplementedError(
        "TODO: implement listing of available locations from the processed CSV."
    )
