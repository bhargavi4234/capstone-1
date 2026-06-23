# capstone project 1-Mutual Fund Data Analytics

## Project Overview

This project focuses on mutual fund data analysis using Python, Pandas, and live NAV data from MFAPI. The goal is to build a complete data pipeline for data ingestion, validation, analysis, and dashboard development.

## Day 1 Objectives

* Create project folder structure
* Initialize Git repository
* Configure GitHub repository
* Install required Python libraries
* Create data ingestion pipeline
* Perform basic data quality checks
* Explore mutual fund master data
* Understand AMFI scheme codes
* Generate data quality summary

## Project Structure
capstone-1/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── dashboard/
├── notebooks/
├── reports/
├── sql/
│
├── data_ingestion.py
├── live_nav_fetch.py
├── requirements.txt
├── README.md
└── .gitignore

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SQLAlchemy
* Requests
* SciPy
* Jupyter Notebook
* Git & GitHub

## Data Ingestion

The "data_ingestion.py" script:

* Loads all CSV datasets from `data/raw`
* Prints dataset shape
* Prints data types
* Displays first five records
* Checks missing values
* Checks duplicate records
* Explores fund master data

## Fund Master Analysis

The project analyzes:

* Fund Houses
* Categories
* AMFI Scheme Codes
* Data Quality Metrics

Example AMFI Scheme Codes:

| Scheme Code | Fund Name           |
| ----------- | ------------------- |
| 119551      | SBI Bluechip Fund   |
| 120503      | ICICI Bluechip Fund |
| 125497      | HDFC Top 100 Fund   |


## Live NAV Data

The "live_nav_fetch.py" script fetches NAV data from MFAPI for selected mutual fund schemes and stores the data as CSV files.

## Data Quality Summary

Current Status:

* Total CSV Files: 10
* Non-Empty Files: 1
* Empty Files: 9
* Missing Values: 0 (fund_master.csv)
* Duplicate Records: 0

## How to Run

### Install Dependencies

bash
pip install -r requirements.txt

### Run Data Ingestion

bash
python data_ingestion.py


### Run NAV Fetch

bash
python live_nav_fetch.py


## GitHub Repository

Day 1 deliverables have been successfully completed and pushed to GitHub.

Author: Bhargavi
