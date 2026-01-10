import pandas as pd
from regime_discovery import discover_regimes
from drift_engine import compute_population_drift

snapshots = []

for t in range(0,6):
    df = pd.read_csv(f"../snapshots/enterprise_snapshot_t{t}.csv")
    df_r,_ = discover_regimes(df)
    snapshots.append(df_r)

for t in range(1,6):
    drift = compute_population_drift(snapshots[t-1], snapshots[t])
    print(f"\nDrift t{t-1} → t{t}")
    print(drift)

