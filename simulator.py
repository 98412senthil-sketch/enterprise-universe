import pandas as pd
from customers import generate_enterprise_population
from evolve import evolve_snapshot

df = generate_enterprise_population(120_000)
df.to_csv("snapshots/enterprise_snapshot_t0.csv", index=False)

macro = None

for t in range(1,6):
    df, macro = evolve_snapshot(df, macro)
    df.to_csv(f"snapshots/enterprise_snapshot_t{t}.csv", index=False)
    print(f"t{t} macro regime: {macro}")
