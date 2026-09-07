"""
tests/test_map_service.py
---------------------------
Owner: Member 3 (Map / GIS)

Unit tests for map/map_service.py: risk classification, marker/legend
construction, and dataset loading (including error handling for
missing files, missing columns, and malformed row-level values).

Run with:
    pytest tests/test_map_service.py
"""

import os

import folium
import pandas as pd
import pytest

from map import map_service


# --------------------------------------------------------------------- #
# get_risk_level
# --------------------------------------------------------------------- #

@pytest.mark.parametrize(
    "score, expected_level",
    [
        (0, "LOW"),
        (30, "LOW"),
        (31, "MEDIUM"),
        (60, "MEDIUM"),
        (61, "HIGH"),
        (80, "HIGH"),
        (81, "CRITICAL"),
        (100, "CRITICAL"),
    ],
)
def test_get_risk_level_boundaries(score, expected_level):
    assert map_service.get_risk_level(score) == expected_level


def test_get_risk_level_clamps_out_of_range_values():
    assert map_service.get_risk_level(-15) == "LOW"
    assert map_service.get_risk_level(500) == "CRITICAL"


def test_get_risk_level_handles_invalid_values():
    assert map_service.get_risk_level(None) == "UNKNOWN"
    assert map_service.get_risk_level("not-a-number") == "UNKNOWN"
    assert map_service.get_risk_level(float("nan")) == "UNKNOWN"


# --------------------------------------------------------------------- #
# get_risk_color
# --------------------------------------------------------------------- #

def test_get_risk_color_known_levels():
    assert map_service.get_risk_color("LOW") == map_service.RISK_COLORS["LOW"]
    assert map_service.get_risk_color("medium") == map_service.RISK_COLORS["MEDIUM"]
    assert map_service.get_risk_color("High") == map_service.RISK_COLORS["HIGH"]
    assert map_service.get_risk_color("CRITICAL") == map_service.RISK_COLORS["CRITICAL"]


def test_get_risk_color_unknown_level_falls_back_to_gray():
    assert map_service.get_risk_color("not-a-level") == map_service.RISK_COLORS["UNKNOWN"]
    assert map_service.get_risk_color(None) == map_service.RISK_COLORS["UNKNOWN"]


# --------------------------------------------------------------------- #
# load_location_data
# --------------------------------------------------------------------- #

def test_load_location_data_bundled_prototype_csv():
    data_frame = map_service.load_location_data()
    assert not data_frame.empty
    for column in map_service.REQUIRED_COLUMNS:
        assert column in data_frame.columns
    assert set(data_frame["Risk_Level"]).issubset(set(map_service.RISK_LEVELS) | {"UNKNOWN"})


def test_load_location_data_missing_file_raises():
    with pytest.raises(map_service.MapDataError):
        map_service.load_location_data("does/not/exist.csv")


def test_load_location_data_missing_columns_raises(tmp_path):
    bad_csv = tmp_path / "bad.csv"
    bad_csv.write_text("Location,Latitude\nShillong,25.57\n")
    with pytest.raises(map_service.MapDataError):
        map_service.load_location_data(str(bad_csv))


def test_load_location_data_drops_rows_with_missing_coordinates(tmp_path):
    csv_path = tmp_path / "locations.csv"
    csv_path.write_text(
        "Location,District,State,Latitude,Longitude,Rainfall_24h_mm,Rainfall_3day_mm,"
        "Slope_degree,Previous_Landslide,Risk_Score,Risk_Level,Recommended_Action\n"
        "GoodTown,D1,S1,25.5,91.8,50,100,20,No,40,MEDIUM,Monitor\n"
        "NoCoords,D2,S2,,91.8,50,100,20,No,40,MEDIUM,Monitor\n"
    )
    data_frame = map_service.load_location_data(str(csv_path))
    assert len(data_frame) == 1
    assert data_frame.iloc[0]["Location"] == "GoodTown"


def test_load_location_data_handles_invalid_risk_score_without_crashing(tmp_path):
    csv_path = tmp_path / "locations.csv"
    csv_path.write_text(
        "Location,District,State,Latitude,Longitude,Rainfall_24h_mm,Rainfall_3day_mm,"
        "Slope_degree,Previous_Landslide,Risk_Score,Risk_Level,Recommended_Action\n"
        "OddTown,D1,S1,25.5,91.8,50,100,20,No,not-a-number,BOGUS,Monitor\n"
    )
    data_frame = map_service.load_location_data(str(csv_path))
    assert len(data_frame) == 1
    assert data_frame.iloc[0]["Risk_Level"] == "UNKNOWN"


# --------------------------------------------------------------------- #
# create_risk_map / add_risk_marker
# --------------------------------------------------------------------- #

def test_create_risk_map_returns_folium_map_with_expected_marker_count():
    data_frame = map_service.load_location_data()
    risk_map = map_service.create_risk_map(data_frame)
    assert isinstance(risk_map, folium.Map)

    marker_count = sum(
        1 for child in risk_map._children.values() if isinstance(child, folium.CircleMarker)
    )
    assert marker_count == len(data_frame)


def test_create_risk_map_accepts_list_of_dicts_like_future_backend_output():
    records = [
        {
            "location": "TestVille",
            "latitude": 26.0,
            "longitude": 92.0,
            "risk_score": 55,
            "rainfall": 40,
            "slope": 15,
            "previous_landslide": "No",
            "recommended_action": "Monitor conditions.",
        }
    ]
    risk_map = map_service.create_risk_map(records)
    marker_count = sum(
        1 for child in risk_map._children.values() if isinstance(child, folium.CircleMarker)
    )
    assert marker_count == 1


def test_add_risk_marker_skips_record_with_missing_coordinates():
    risk_map = folium.Map(location=map_service.DEFAULT_MAP_CENTER, zoom_start=6)
    added = map_service.add_risk_marker(risk_map, {"location": "Nowhere"})
    assert added is False


def test_add_risk_marker_handles_missing_risk_score_as_unknown():
    risk_map = folium.Map(location=map_service.DEFAULT_MAP_CENTER, zoom_start=6)
    added = map_service.add_risk_marker(risk_map, {"location": "NoScore", "latitude": 25.0, "longitude": 91.0})
    assert added is True


# --------------------------------------------------------------------- #
# filter_locations / list_states
# --------------------------------------------------------------------- #

def test_list_states_and_filter_locations():
    data_frame = map_service.load_location_data()
    states = map_service.list_states(data_frame)
    assert "Meghalaya" in states

    filtered = map_service.filter_locations(data_frame, state="Meghalaya")
    assert not filtered.empty
    assert set(filtered["State"]) == {"Meghalaya"}

    filtered_by_location = map_service.filter_locations(data_frame, location="Shillong")
    assert list(filtered_by_location["Location"]) == ["Shillong"]

    empty_result = map_service.filter_locations(data_frame, state="NoSuchState")
    assert empty_result.empty
