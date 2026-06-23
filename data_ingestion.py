import pandas as pd
import os

data_folder = "data/raw"

files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

print(f"\nFound {len(files)} CSV files\n")

total_files = len(files)
empty_files = 0
non_empty_files = 0

for file in files:

    print("\n" + "=" * 60)
    print(f"DATASET: {file}")
    print("=" * 60)

    path = os.path.join(data_folder, file)

    # Check empty files
    if os.path.getsize(path) == 0:
        print("File is empty. Skipping...")
        empty_files += 1
        continue

    non_empty_files += 1

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

        # Special analysis for fund_master.csv
        if file == "fund_master.csv":

            print("\n" + "=" * 30)
            print("FUND MASTER ANALYSIS")
            print("=" * 30)

            if "fund_house" in df.columns:
                print("\nFund Houses:")
                print(df["fund_house"].unique())

            if "category" in df.columns:
                print("\nCategories:")
                print(df["category"].unique())

            if "subcategory" in df.columns:
                print("\nSub Categories:")
                print(df["subcategory"].unique())

            if "risk_grade" in df.columns:
                print("\nRisk Grades:")
                print(df["risk_grade"].unique())

            if "scheme_code" in df.columns:
                print("\nAMFI Scheme Codes:")
                print(df["scheme_code"].unique())

    except Exception as e:
        print(f"Error reading {file}: {e}")

# ==========================
# DATA QUALITY SUMMARY
# ==========================

print("\n" + "=" * 60)
print("DATA QUALITY SUMMARY")
print("=" * 60)

print(f"Total CSV Files      : {total_files}")
print(f"Non-Empty Files      : {non_empty_files}")
print(f"Empty Files          : {empty_files}")

# Save summary to file
os.makedirs("reports", exist_ok=True)

with open("reports/data_quality_summary.txt", "w") as f:
    f.write("DATA QUALITY SUMMARY\n\n")
    f.write(f"Total CSV Files: {total_files}\n")
    f.write(f"Non-Empty Files: {non_empty_files}\n")
    f.write(f"Empty Files: {empty_files}\n\n")

    if empty_files > 0:
        f.write("Observation:\n")
        f.write("Some datasets are empty and require actual data.\n")

print("\nSummary saved to reports/data_quality_summary.txt")