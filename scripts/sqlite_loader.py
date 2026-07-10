import pandas as pd
from sqlalchemy import create_engine

# =====================================
# CREATE SQLITE DATABASE
# =====================================

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

print("Connected to SQLite database")

# =====================================
# LOAD FUND MASTER
# =====================================

fund_df = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

fund_df.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print("dim_fund loaded")

# =====================================
# LOAD CLEAN NAV HISTORY
# =====================================

nav_df = pd.read_csv(
    "data/processed/02_nav_history_clean.csv"
)

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("fact_nav loaded")

# =====================================
# LOAD CLEAN INVESTOR TRANSACTIONS
# =====================================

txn_df = pd.read_csv(
    "data/processed/08_investor_transactions_clean.csv"
)

txn_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("fact_transactions loaded")

# =====================================
# LOAD CLEAN SCHEME PERFORMANCE
# =====================================

perf_df = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("fact_performance loaded")

# =====================================
# LOAD AUM DATA
# =====================================

aum_df = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

aum_df.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("fact_aum loaded")

# =====================================
# VERIFY ROW COUNTS
# =====================================

print("\n==============================")
print("VERIFYING ROW COUNTS")
print("==============================")

tables = {
    "dim_fund": fund_df,
    "fact_nav": nav_df,
    "fact_transactions": txn_df,
    "fact_performance": perf_df,
    "fact_aum": aum_df
}

all_match = True

for table_name, df in tables.items():

    csv_count = len(df)

    db_count = pd.read_sql(
        f"SELECT COUNT(*) AS cnt FROM {table_name}",
        engine
    )["cnt"][0]

    print(
        f"{table_name}: CSV={csv_count}, DB={db_count}"
    )

    if csv_count == db_count:
        print("✓ Counts Match\n")
    else:
        print("✗ Counts Do Not Match\n")
        all_match = False

# =====================================
# FINAL STATUS
# =====================================

if all_match:
    print("All row counts verified successfully!")
else:
    print("Some row counts do not match!")
