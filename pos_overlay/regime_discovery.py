import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture

FEATURES = ["Monthly_Spend","Txn_Count","Avg_Ticket","Dormancy_Days","Debt"]

def discover_regimes(df, n_regimes=3):
    df = df.copy()

    # Structural singularity governance
    df["Avg_Ticket"] = df["Avg_Ticket"].replace([np.inf, -np.inf], np.nan)
    df.loc[df["Txn_Count"] == 0, "Avg_Ticket"] = 0
    df.loc[df["Txn_Count"] == 0, "Monthly_Spend"] = 0
    df["Avg_Ticket"] = df["Avg_Ticket"].fillna(0)

    X = df[FEATURES]
    X = X.replace([np.inf, -np.inf], np.nan).fillna(0)

    Xs = StandardScaler().fit_transform(X)

    gmm = GaussianMixture(n_components=n_regimes, random_state=42)
    regimes = gmm.fit_predict(Xs)
    probs = gmm.predict_proba(Xs)

    df["Regime"] = regimes
    df["Belief"] = probs.max(axis=1)

    return df, gmm

