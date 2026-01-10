import pandas as pd
from macro import sample_macro_regime, MACRO_REGIMES
from shocks import apply_macro_shock

def evolve_snapshot(df, prev_macro=None):
    macro_name = sample_macro_regime(prev_macro)
    macro = MACRO_REGIMES[macro_name]
    df_new = apply_macro_shock(df, macro)
    return df_new, macro_name
 
