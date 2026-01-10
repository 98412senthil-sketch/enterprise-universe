import pandas as pd
from regime_discovery import discover_regimes
from sii_engine import compute_sii
from health_classifier import classify_health

df = pd.read_csv("../snapshots/enterprise_snapshot_t1.csv")
df,_ = discover_regimes(df)
df = compute_sii(df)
df = classify_health(df)

print(df["Health"].value_counts())
print(df.groupby("Regime")["Health"].value_counts(normalize=True))
 
