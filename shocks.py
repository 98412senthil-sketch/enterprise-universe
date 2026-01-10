import numpy as np

def apply_macro_shock(df, macro):
    df = df.copy()

    df["Income"] *= (1 + macro["income_growth"] + np.random.normal(0,0.02,len(df)))
    df["Monthly_Spend"] *= (1 + macro["spend_boost"] + np.random.normal(0,0.03,len(df)))
    df["Txn_Count"] = (df["Txn_Count"] * (1 + macro["txn_boost"] + np.random.normal(0,0.05,len(df)))).clip(0).round()
    df["Dormancy_Days"] *= (1 + macro["dormancy_drop"] + np.random.normal(0,0.05,len(df)))

    df["Avg_Ticket"] = (df["Monthly_Spend"] / df["Txn_Count"].replace(0, np.nan)).fillna(df["Avg_Ticket"])

    return df
 
