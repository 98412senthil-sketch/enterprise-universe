 
import numpy as np

FEATURES = ["Monthly_Spend","Txn_Count","Avg_Ticket","Dormancy_Days","Debt"]

# Collapse direction vector (risk gravity)
w = np.array([
        -0.5,   # spend down
        -0.7,   # txn collapse
        -0.3,   # ticket stress
        +0.8,   # dormancy explosion
        +0.9    # debt burden
    ])

def compute_sii(df):
    # Normalize structural axes
    X = df[FEATURES]
    X = (X - X.mean()) / X.std()
    sii = np.abs(X.values @ w)
    df["SII"] = sii
    return df
