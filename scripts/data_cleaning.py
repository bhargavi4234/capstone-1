import pandas as pd

# =====================================
# 1. CLEAN NAV HISTORY
# =====================================

# Load NAV history
nav_df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date to datetime
nav_df["date"] = pd.to_datetime(
    nav_df["date"],
    errors="coerce"
)

# Remove invalid dates
nav_df = nav_df.dropna(subset=["date"])

# Sort by fund and date
nav_df = nav_df.sort_values(
    by=["amfi_code", "date"]
)

# Forward fill missing NAV values
nav_df["nav"] = nav_df.groupby(
    "amfi_code"
)["nav"].ffill()

# Remove duplicates
nav_df = nav_df.drop_duplicates(
    subset=["amfi_code", "date"]
)

# Validate NAV > 0
nav_df = nav_df[
    nav_df["nav"] > 0
]

# Save cleaned NAV file
nav_df.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("02_nav_history cleaned successfully!")
print("Rows:", len(nav_df))


# =====================================
# 2. CLEAN INVESTOR TRANSACTIONS
# =====================================

# Load investor transactions
txn_df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Convert transaction date
txn_df["transaction_date"] = pd.to_datetime(
    txn_df["transaction_date"],
    errors="coerce"
)

# Remove invalid dates
txn_df = txn_df.dropna(
    subset=["transaction_date"]
)

# Standardize transaction types
txn_df["transaction_type"] = (
    txn_df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.upper()
)

# Keep only valid transaction types
valid_txn = [
    "SIP",
    "LUMPSUM",
    "REDEMPTION"
]

txn_df = txn_df[
    txn_df["transaction_type"].isin(valid_txn)
]

# Validate amount > 0
txn_df = txn_df[
    txn_df["amount_inr"] > 0
]

# Standardize KYC status
txn_df["kyc_status"] = (
    txn_df["kyc_status"]
    .astype(str)
    .str.strip()
    .str.upper()
)

# Keep only valid KYC statuses
valid_kyc = [
    "VERIFIED",
    "PENDING",
    "REJECTED"
]

txn_df = txn_df[
    txn_df["kyc_status"].isin(valid_kyc)
]

# Remove duplicates
txn_df = txn_df.drop_duplicates()

# Save cleaned transactions file
txn_df.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("\n08_investor_transactions cleaned successfully!")
print("Rows:", len(txn_df))



# =====================================
# 3. CLEAN SCHEME PERFORMANCE
# =====================================

# Load scheme performance data
perf_df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

# Columns that should be numeric
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct",
    "morningstar_rating"
]

# Convert to numeric
for col in numeric_cols:
    perf_df[col] = pd.to_numeric(
        perf_df[col],
        errors="coerce"
    )

# Remove rows with missing numeric values
perf_df = perf_df.dropna(
    subset=numeric_cols
)

# Expense ratio validation
perf_df = perf_df[
    (perf_df["expense_ratio_pct"] >= 0.1) &
    (perf_df["expense_ratio_pct"] <= 2.5)
]

# Flag anomalies in returns
perf_df["anomaly_flag"] = (
    (perf_df["return_1yr_pct"] > 100) |
    (perf_df["return_1yr_pct"] < -100) |
    (perf_df["return_3yr_pct"] > 100) |
    (perf_df["return_3yr_pct"] < -100) |
    (perf_df["return_5yr_pct"] > 100) |
    (perf_df["return_5yr_pct"] < -100)
)

# Remove duplicate records
perf_df = perf_df.drop_duplicates()

# Save cleaned file
perf_df.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("\n07_scheme_performance cleaned successfully!")
print("Rows:", len(perf_df))
print(
    "Anomalies Found:",
    perf_df["anomaly_flag"].sum()
)


# =====================================
# CLEAN REMAINING DATASETS
# =====================================

remaining_files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in remaining_files:

    df = pd.read_csv(f"data/raw/{file}")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove fully empty rows
    df = df.dropna(how="all")

    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    output_file = file.replace(
        ".csv",
        "_clean.csv"
    )

    df.to_csv(
        f"data/processed/{output_file}",
        index=False
    )

    print(f"{output_file} cleaned successfully!")