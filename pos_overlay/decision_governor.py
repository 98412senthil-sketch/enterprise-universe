from dataclasses import dataclass

@dataclass
class DecisionState:
    regime: int
    health: str
    state: str
    allowed_actions: list
    forbidden_actions: list
    escalation_required: bool
    owner: str


def govern_decision(regime, health):
    # RED ZONE — Collapse trajectory
    if health == "RED":
        return DecisionState(
            regime=regime,
            health=health,
            state="COLLAPSE",
            allowed_actions=["Recovery","Hard_Stop","Restructure"],
            forbidden_actions=["Marketing","New_Credit","Upsell"],
            escalation_required=True,
            owner="CRO"
        )

    # AMBER ZONE — Early warning
    elif health == "AMBER":
        return DecisionState(
            regime=regime,
            health=health,
            state="WARNING",
            allowed_actions=["Soft_Nudge","Monitoring","Retention"],
            forbidden_actions=["Aggressive_Credit"],
            escalation_required=False,
            owner="Risk_Manager"
        )

    # GREEN ZONE — Normal operations
    else:
        return DecisionState(
            regime=regime,
            health=health,
            state="STABLE",
            allowed_actions=["Normal_Ops","Upsell","Cross_Sell"],
            forbidden_actions=["Collections"],
            escalation_required=False,
            owner="Portfolio_Head"
        )
 
