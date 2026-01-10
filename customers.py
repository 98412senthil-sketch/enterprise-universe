import numpy as np
import pandas as pd

def assign_lifecycle_cohort(df):
    df["Lifecycle"] = pd.cut(
        df["Tenure_Months"],
        bins=[0, 6, 24, 60, 120, 999],
        labels=["New","Early","Core","Mature","Legacy"]
    )
    return df

def assign_enterprise_segment(df):
    conditions = [
        (df["Income"] < 300000),
        (df["Income"].between(300000, 1200000)),
        (df["Income"] > 1200000)
    ]
    segments = ["Mass","Affluent","HNI"]
    df["Segment"] = np.select(conditions, segments)
    return df

def generate_enterprise_population(n=100_000, seed=42):
    np.random.seed(seed)

    income = np.random.lognormal(mean=10.4, sigma=0.6, size=n)
    tenure = np.random.gamma(shape=2.5, scale=18, size=n).clip(1)
    volatility = np.random.beta(2, 5, size=n)

    spend_ratio = np.random.normal(0.18, 0.06, size=n).clip(0.03, 0.6)
    monthly_spend = income * spend_ratio / 12

    txn_count = np.random.poisson(lam=(monthly_spend / 150).clip(1, 120))
    avg_ticket = (monthly_spend / txn_count).clip(50, None)

    debt_ratio = (0.15 + 0.6 * volatility + np.random.normal(0, 0.1, n)).clip(0, 0.9)
    debt = income * debt_ratio

    dormancy = (60 * volatility + np.random.gamma(2, 10, n)).clip(0)

    df = pd.DataFrame({
        "Income": income.round(0),
        "Monthly_Spend": monthly_spend.round(2),
        "Txn_Count": txn_count,
        "Avg_Ticket": avg_ticket.round(2),
        "Debt": debt.round(0),
        "Tenure_Months": tenure.round(1),
        "Volatility": volatility.round(3),
        "Dormancy_Days": dormancy.round(1)
    })

    df = assign_enterprise_segment(df)
    df = assign_lifecycle_cohort(df)

    return df
