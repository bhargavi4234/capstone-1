import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Mutual Fund Recommendation System",
    page_icon="📈",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("📈 Mutual Fund Recommendation System")
st.write("Select your risk appetite to view suitable mutual fund recommendations.")

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/07_scheme_performance_clean.csv")

df = load_data()

# -----------------------------
# Risk Selection
# -----------------------------
risk_options = sorted(df["risk_grade"].dropna().unique())

risk = st.selectbox(
    "Select Risk Appetite",
    risk_options
)

# -----------------------------
# Show Recommendations
# -----------------------------
if st.button("Show Recommendations"):

    result = df[df["risk_grade"] == risk]

    if result.empty:
        st.warning("No mutual funds found for the selected risk appetite.")
    else:

        st.success(f"Found {len(result)} mutual fund(s).")

        display = result[
            [
                "scheme_name",
                "fund_house",
                "category",
                "return_1yr_pct",
                "return_3yr_pct",
                "return_5yr_pct",
                "sharpe_ratio",
                "risk_grade"
            ]
        ].copy()

        display.columns = [
            "Scheme Name",
            "Fund House",
            "Category",
            "1-Year Return (%)",
            "3-Year Return (%)",
            "5-Year Return (%)",
            "Sharpe Ratio",
            "Risk Grade"
        ]

        st.dataframe(display, use_container_width=True)

        st.subheader("Top 5 Recommended Funds")

        top5 = display.sort_values(
            by="3-Year Return (%)",
            ascending=False
        ).head(5)

        st.table(top5)

# -----------------------------
# Dataset Summary
# -----------------------------
st.markdown("---")

st.subheader("Dataset Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Funds", len(df))
col2.metric("Fund Houses", df["fund_house"].nunique())
col3.metric("Risk Categories", df["risk_grade"].nunique())