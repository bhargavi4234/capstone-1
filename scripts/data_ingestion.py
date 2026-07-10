import pandas as pd
import os

DATA_FOLDER = "data/raw"

csv_files = sorted(
    [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]
)

print(f"\nFound {len(csv_files)} CSV files\n")

# ===============================
# LOAD ALL DATASETS
# ===============================

for file in csv_files:

    print("\n" + "=" * 70)
    print(f"DATASET: {file}")
    print("=" * 70)

    path = os.path.join(DATA_FOLDER, file)

    try:

        df = pd.read_csv(path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file}: {e}")

# ===============================
# STEP 13 - EXPLORE FUND MASTER
# ===============================

print("\n" + "=" * 70)
print("STEP 13: FUND MASTER ANALYSIS")
print("=" * 70)

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

print("\nColumns:")
print(fund_master.columns.tolist())

if "fund_house" in fund_master.columns:
    print("\nFund Houses")
    print(fund_master["fund_house"].unique())

if "category" in fund_master.columns:
    print("\nCategories")
    print(fund_master["category"].unique())

if "subcategory" in fund_master.columns:
    print("\nSub Categories")
    print(fund_master["subcategory"].unique())

if "risk_grade" in fund_master.columns:
    print("\nRisk Grades")
    print(fund_master["risk_grade"].unique())

# ===============================
# STEP 14 - AMFI SCHEME CODES
# ===============================

print("\n" + "=" * 70)
print("STEP 14: AMFI SCHEME CODES")
print("=" * 70)

if "scheme_code" in fund_master.columns:

    print("\nSample AMFI Scheme Codes:")
    print(
        fund_master["scheme_code"]
        .drop_duplicates()
        .head(20)
        .tolist()
    )

# ===============================
# STEP 15 - VALIDATE AMFI CODES
# ===============================

print("\n" + "=" * 70)
print("STEP 15: VALIDATE AMFI CODES")
print("=" * 70)

try:

    nav_history = pd.read_csv(
        "data/raw/02_nav_history.csv"
    )

    if (
        "scheme_code" in fund_master.columns
        and
        "scheme_code" in nav_history.columns
    ):

        master_codes = set(
            fund_master["scheme_code"]
            .dropna()
        )

        nav_codes = set(
            nav_history["scheme_code"]
            .dropna()
        )

        missing_codes = master_codes - nav_codes

        print(
            "Total Fund Master Codes:",
            len(master_codes)
        )

        print(
            "Total NAV Codes:",
            len(nav_codes)
        )

        print(
            "Missing Codes:",
            len(missing_codes)
        )

    else:
        print(
            "scheme_code column not found."
        )

except Exception as e:
    print(e)

# ===============================
# STEP 16 - DATA QUALITY SUMMARY
# ===============================

print("\n" + "=" * 70)
print("STEP 16: DATA QUALITY SUMMARY")
print("=" * 70)

summary = []

summary.append(
    "DATA QUALITY SUMMARY\n"
)

summary.append(
    f"Total scheme codes in fund_master: "
    f"{len(master_codes) if 'master_codes' in locals() else 0}\n"
)

summary.append(
    f"Total scheme codes in nav_history: "
    f"{len(nav_codes) if 'nav_codes' in locals() else 0}\n"
)

summary.append(
    f"Missing scheme codes: "
    f"{len(missing_codes) if 'missing_codes' in locals() else 0}\n"
)

summary.append(
    "\nConclusion:\n"
)

summary.append(
    "Dataset loaded successfully. "
    "Review missing values and duplicates "
    "for detailed quality assessment."
)

os.makedirs("reports", exist_ok=True)

with open(
    "reports/data_quality_summary.txt",
    "w"
) as f:

    f.writelines(summary)

print(
    "Summary saved to "
    "reports/data_quality_summary.txt"
)