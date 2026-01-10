import numpy as np

MACRO_REGIMES = {
    "GROWTH": {
        "income_growth": 0.08,
        "spend_boost": 0.06,
        "txn_boost": 0.10,
        "dormancy_drop": -0.15
    },
    "INFLATION": {
        "income_growth": 0.04,
        "spend_boost": 0.12,
        "txn_boost": -0.05,
        "dormancy_drop": 0.05
    },
    "STRESS": {
        "income_growth": -0.10,
        "spend_boost": -0.20,
        "txn_boost": -0.25,
        "dormancy_drop": 0.40
    },
    "RECOVERY": {
        "income_growth": 0.06,
        "spend_boost": 0.04,
        "txn_boost": 0.08,
        "dormancy_drop": -0.20
    }
}

def sample_macro_regime(prev=None):
    if prev is None:
        return np.random.choice(list(MACRO_REGIMES.keys()))
    # Markov regime persistence
    if np.random.rand() < 0.7:
        return prev
    return np.random.choice(list(MACRO_REGIMES.keys()))
 
