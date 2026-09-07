"""
backend/risk_logic.py
----------------------
Owner: Member 4 (Backend)

Responsibility:
    Convert a raw numeric risk score (0-100) into a human-readable risk
    level, a recommendation message, and an alert flag.

Thresholds (Step 1 prototype, subject to review with Member 2 once the
real model's score distribution is known):

    0  - 30   -> LOW
    31 - 60   -> MEDIUM
    61 - 80   -> HIGH
    81 - 100  -> CRITICAL
"""

import math

_LOW_MAX = 30
_MEDIUM_MAX = 60
_HIGH_MAX = 80


def _validate_score(score: float) -> float:
    """Ensure the score is a real, finite number within the valid 0-100 range."""
    try:
        score = float(score)
    except (TypeError, ValueError):
        raise ValueError(f"Risk score must be a number, got: {score!r}")

    if math.isnan(score) or math.isinf(score):
        raise ValueError(f"Risk score must be a finite number, got: {score}")

    if score < 0 or score > 100:
        raise ValueError(f"Risk score must be between 0 and 100, got: {score}")

    return score


def get_risk_level(score: float) -> str:
    """
    Convert a numeric risk score (0-100) into a categorical risk level.

    Returns:
        One of: "LOW", "MEDIUM", "HIGH", "CRITICAL".
    """
    score = _validate_score(score)

    if score <= _LOW_MAX:
        return "LOW"
    elif score <= _MEDIUM_MAX:
        return "MEDIUM"
    elif score <= _HIGH_MAX:
        return "HIGH"
    else:
        return "CRITICAL"


def get_recommendation(score: float) -> str:
    """
    Provide a simple prototype-level recommendation message for the
    given risk score.
    """
    level = get_risk_level(score)

    messages = {
        "LOW": "Normal monitoring recommended",
        "MEDIUM": "Increased monitoring recommended",
        "HIGH": "Field inspection recommended",
        "CRITICAL": "Immediate attention recommended",
    }
    return messages[level]


def is_alert_required(score: float) -> bool:
    """
    Decide whether an alert should be raised for the given risk score.

    Returns:
        False for LOW/MEDIUM, True for HIGH/CRITICAL.
    """
    level = get_risk_level(score)
    return level in ("HIGH", "CRITICAL")
