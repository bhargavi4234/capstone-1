# 📊 Mutual Fund Analytics Platform

## Capstone Project – Bluestock Fintech


# Overview

The **Mutual Fund Analytics Platform** is a data analytics project developed to analyze the performance of Indian mutual funds. The project performs data ingestion, preprocessing, database creation, exploratory data analysis (EDA), performance analytics, advanced analytics, dashboard visualization, and mutual fund recommendation.

The project also includes a **Power BI Dashboard** and a **Streamlit Web Application** that recommends mutual funds based on the user's risk appetite.


# Project Objectives

- Collect mutual fund datasets.
- Clean and preprocess financial data.
- Store processed data in SQLite.
- Perform Exploratory Data Analysis (EDA).
- Calculate financial performance metrics.
- Build an interactive Power BI Dashboard.
- Develop a Streamlit web application.
- Recommend mutual funds based on risk level.


# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- SQLite
- Jupyter Notebook
- Power BI
- Streamlit
- Git & GitHub
- Visual Studio Code


# Project Structure

```
capstone-1/
│
├── dashboard/
│   ├── bluestock_mf_dashboard.pbix
│   └── Dashboard.pdf
│
├── data/
│   ├── db/
│   ├── processed/
│   ├── raw/
│   └── MutualFundAnalysis/
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── reports/
│
├── screenshots/
│
├── scripts/
│   ├── data/
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── sqlite_loader.py
│   ├── live_nav_fetch.py
│   └── recommender.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── app.py
├── data_dictionary.md
├── README.md
├── requirements.txt
└── .gitignore
```


# Features

## Data Ingestion

- Reads multiple mutual fund datasets.
- Imports raw CSV files.

## Data Cleaning

- Handles missing values.
- Removes duplicate records.
- Standardizes data formats.

## SQLite Database

- Stores cleaned datasets.
- Supports efficient querying.

## Exploratory Data Analysis

- NAV Trend Analysis
- AUM Analysis
- SIP Inflow Analysis
- Category-wise Analysis
- Investor Analytics

## Performance Analytics

- Daily Returns
- CAGR
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown

## Advanced Analytics

- Value at Risk (VaR)
- Conditional VaR (CVaR)
- Rolling Sharpe Ratio
- Monte Carlo Simulation
- Mutual Fund Recommendation

## Power BI Dashboard

The dashboard contains:

- Industry Overview
- Fund Performance
- Investor Analytics
- SIP & Market Trends

## Streamlit Web Application

The Streamlit application allows users to:

- Select their risk appetite.
- Receive mutual fund recommendations.
- View recommended funds interactively.


# How to Run the Project

## Step 1: Clone Repository

```bash
git clone https://github.com/bhargavi4234/capstone-1.git
```

```bash
cd capstone-1
```

## Step 2: Install Required Packages

```bash
pip install -r requirements.txt
```

## Step 3: Run Data Ingestion

```bash
python scripts/data_ingestion.py
```

## Step 4: Run Data Cleaning

```bash
python scripts/data_cleaning.py
```

## Step 5: Load Data into SQLite

```bash
python scripts/sqlite_loader.py
```

## Step 6: Fetch Live NAV

```bash
python scripts/live_nav_fetch.py
```

## Step 7: Run Mutual Fund Recommender

```bash
python scripts/recommender.py
```

## Step 8: Launch Streamlit Application

```bash
streamlit run app.py
```

## Step 9: View Power BI Dashboard

Open:

```
dashboard/bluestock_mf_dashboard.pbix
```

or

```
dashboard/Dashboard.pdf
```

# Screenshots

## Power BI Dashboard

- Industry Overview
- Fund Performance
- Investor Analytics
- SIP & Market Trends

## Streamlit Web Application

### B1 – Home Screen

### B2 – Recommendation Screen


# Results

- Successfully collected mutual fund datasets.
- Cleaned and processed financial data.
- Stored data in SQLite.
- Performed Exploratory Data Analysis.
- Calculated key financial metrics.
- Developed an interactive Power BI Dashboard.
- Built a Streamlit application.
- Generated mutual fund recommendations based on risk appetite.


# Future Enhancements

- Live market updates
- Machine Learning based predictions
- Portfolio optimization
- Personalized recommendations
- Mobile application


# References

1. AMFI India – https://www.amfiindia.com
2. MFAPI – https://www.mfapi.in
3. Python Documentation – https://www.python.org
4. Pandas Documentation – https://pandas.pydata.org
5. NumPy Documentation – https://numpy.org
6. Matplotlib Documentation – https://matplotlib.org
7. SQLite Documentation – https://www.sqlite.org
8. Microsoft Power BI Documentation – https://learn.microsoft.com/power-bi/
9. Streamlit Documentation – https://docs.streamlit.io
10. GitHub Documentation – https://docs.github.com


# Author

**Bhargavi**

**Bluestock Fintech – Mutual Fund Analytics Platform Capstone Project**