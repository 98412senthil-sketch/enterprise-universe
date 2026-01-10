import pandas as pd
from regime_discovery import discover_regimes
from sii_engine import compute_sii
from health_classifier import classify_health
from decision_governor import govern_decision

df = pd.read_csv("../snapshots/enterprise_snapshot_t1.csv")
df,_ = discover_regimes(df)
df = compute_sii(df)
df = classify_health(df)

df["Decision_State"] = df.apply(lambda r: govern_decision(r["Regime"], r["Health"]).state, axis=1)
df["Owner"] = df.apply(lambda r: govern_decision(r["Regime"], r["Health"]).owner, axis=1)
df["Escalate"] = df.apply(lambda r: govern_decision(r["Regime"], r["Health"]).escalation_required, axis=1)

print(df["Decision_State"].value_counts())
print(df["Owner"].value_counts())
print("Escalations:", df["Escalate"].sum())
 
