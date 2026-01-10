import pandas as pd

def compute_population_drift(df_prev, df_new):
    prev_dist = df_prev["Regime"].value_counts(normalize=True).sort_index()
    new_dist = df_new["Regime"].value_counts(normalize=True).sort_index()
    drift = (new_dist - prev_dist).fillna(0)
    return drift
 
