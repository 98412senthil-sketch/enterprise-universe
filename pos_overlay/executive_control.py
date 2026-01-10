import pandas as pd
import matplotlib.pyplot as plt

def build_dashboard(t):
    df = pd.read_csv(f"../snapshots/enterprise_snapshot_t{t}.csv")

    from regime_discovery import discover_regimes
    from sii_engine import compute_sii
    from health_classifier import classify_health

    df,_ = discover_regimes(df)
    df = compute_sii(df)
    df = classify_health(df)

    # 1. Health State
    df["Health"].value_counts().plot(kind="bar", title=f"Enterprise Health t{t}")
    plt.savefig(f"../snapshots/health_t{t}.png")
    plt.clf()

    # 2. Regime Distribution
    df["Regime"].value_counts().plot(kind="bar", title=f"Regime Distribution t{t}")
    plt.savefig(f"../snapshots/regimes_t{t}.png")
    plt.clf()

    # 3. Collapse Funnel
    df.groupby("Regime")["Health"].value_counts(normalize=True).unstack().plot(kind="bar", stacked=True)
    plt.title(f"Collapse Funnel by Regime t{t}")
    plt.savefig(f"../snapshots/collapse_funnel_t{t}.png")
    plt.clf()

