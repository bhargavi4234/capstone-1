import requests
import pandas as pd
import os

# Create raw folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# Mutual Fund Scheme Codes
funds = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

print("\nFetching Live NAV Data...\n")

for fund_name, scheme_code in funds.items():

    try:

        url = f"https://api.mfapi.in/mf/{scheme_code}"

        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        print("=" * 60)
        print(f"Fund: {fund_name}")
        print(f"Scheme Code: {scheme_code}")

        # Display scheme name
        if "meta" in data:
            print(
                "Scheme Name:",
                data["meta"].get(
                    "scheme_name",
                    "Not Available"
                )
            )

        # NAV History
        nav_df = pd.DataFrame(data["data"])

        print(
            f"NAV Records: {len(nav_df)}"
        )

        # Save CSV
        file_name = (
            f"data/raw/{fund_name}_NAV.csv"
        )

        nav_df.to_csv(
            file_name,
            index=False
        )

        print(
            f"Saved: {file_name}"
        )

    except Exception as e:

        print(
            f"Error fetching "
            f"{fund_name}: {e}"
        )

print("\nAll NAV downloads completed.")