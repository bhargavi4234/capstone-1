import pandas as pd

performance = pd.read_csv("data/processed/07_scheme_performance_clean.csv")

print("\nAvailable Risk Grades:")
print(performance["risk_grade"].unique())

risk = input("\nEnter Risk Appetite: ").strip()

recommendations = (
    performance[
        performance["risk_grade"].str.lower() == risk.lower()
    ]
    .sort_values("sharpe_ratio", ascending=False)
    .head(3)
)

if recommendations.empty:
    print("\nNo funds found for this risk grade.")
else:
    print("\nTop 3 Recommended Funds:\n")
    print(
        recommendations[
            [
                "scheme_name",
                "fund_house",
                "risk_grade",
                "sharpe_ratio",
                "return_3yr_pct",
                "return_5yr_pct",
            ]
        ]
    )