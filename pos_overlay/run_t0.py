import pandas as pd
from regime_discovery import discover_regimes

df = pd.read_csv("../snapshots/enterprise_snapshot_t0.csv")
df_r, model = discover_regimes(df)

print(df_r["Regime"].value_counts())
print(df_r["Belief"].describe())

df_r.to_csv("../snapshots/t0_with_regimes.csv", index=False)
 
