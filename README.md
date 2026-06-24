# capstone project 1- Mutual Fund Data Analytics

## Project Overview

This project focuses on mutual fund data analysis using Python, Pandas, and live NAV data from MFAPI. The objective is to build a complete data ingestion and validation pipeline for mutual fund datasets and prepare the data for analytics and dashboard development.

## Project Structure

capstone-1/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── reports/
├── dashboard/
├── notebooks/
├── sql/
│
├── data_ingestion.py
├── live_nav_fetch.py
├── requirements.txt
├── README.md
└── .gitignore

## Dataset Files

* 01_fund_master.csv
* 02_nav_history.csv
* 03_aum_by_fund_house.csv
* 04_monthly_sip_inflows.csv
* 05_category_inflows.csv
* 06_industry_folio_count.csv
* 07_scheme_performance.csv
* 08_investor_transactions.csv
* 09_portfolio_holdings.csv
* 10_benchmark_indices.csv

## Features

### Data Ingestion

The `data_ingestion.py` script:

* Loads all 10 CSV datasets
* Prints shape, data types, and sample records
* Detects missing values
* Detects duplicate records
* Explores fund master data
* Validates AMFI scheme codes
* Generates data quality reports

### Live NAV Fetching

The `live_nav_fetch.py` script:

* Fetches NAV data from MFAPI
* Downloads NAV history for selected mutual funds
* Stores NAV data as CSV files

## Technologies Used

* Python
* Pandas
* NumPy
* Requests
* Matplotlib
* Seaborn
* Plotly
* SQLAlchemy
* SciPy
* Jupyter Notebook
* Git
* GitHub

## How to Run

Install dependencies:

pip install -r requirements.txt

Run data ingestion:

python data_ingestion.py

Fetch live NAV data:

python live_nav_fetch.py

