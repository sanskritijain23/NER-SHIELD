"""
backend/risk_logic.py
----------------------
Owner: Member 4 (Backend)

Responsibility:
    Convert a raw numeric risk score (from the ML model) into a
    human-readable risk level, an alert flag, and a recommended action.

NOTE: Placeholder only. Thresholds/logic below are NOT implemented yet
(no arbitrary/fake thresholds have been chosen) — this needs to be
decided deliberately, ideally in coordination with Member 2 (ML) so
the score scale (e.g. 0-1 vs 0-100) is understood.
"""


def get_risk_level(score: float) -> str:
    """
    Convert a numeric risk score into a categorical risk level.

    Args:
        score: Risk score/probability returned by the ML model
               (scale to be confirmed with Member 2, e.g. 0.0-1.0).

    Returns:
        A risk level string, e.g. one of: "Low", "Moderate", "High", "Severe".

    TODO (Member 4):
        - Decide on the score scale together with Member 2.
        - Define clear thresholds mapping score ranges to risk levels.
        - Document the chosen thresholds here in the docstring.
    """
    raise NotImplementedError("TODO: implement score -> risk level mapping.")


def should_alert(risk_level: str) -> bool:
    """
    Decide whether an alert should be raised for the given risk level.

    Args:
        risk_level: The risk level string from get_risk_level().

    Returns:
        True if an alert should be shown/raised, False otherwise.

    TODO (Member 4): Implement the alerting rule, e.g. alert=True for
    "High" and "Severe" risk levels.
    """
    raise NotImplementedError("TODO: implement alert decision logic.")


def get_recommended_action(risk_level: str) -> str:
    """
    Provide a recommended action/message for the given risk level.

    Args:
        risk_level: The risk level string from get_risk_level().

    Returns:
        A short human-readable recommended action string.

    TODO (Member 4): Define recommended actions per risk level
    (e.g. "Monitor conditions", "Prepare for evacuation", etc.),
    ideally reviewed with domain-knowledge sources for the NER region.
    """
    raise NotImplementedError("TODO: implement recommended action mapping.")
