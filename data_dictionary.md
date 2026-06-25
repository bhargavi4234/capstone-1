# Data Dictionary – Mutual Fund Analytics Capstone

This document describes all datasets used in the Mutual Fund Analytics Capstone project, including column names, data types, business definitions, and source references.

# 01_fund_master.csv

**Source Reference:** AMFI India (www.amfiindia.com)

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| amfi_code | INTEGER | Unique AMFI code assigned to each mutual fund scheme. |
| fund_house | TEXT | Name of the Asset Management Company (AMC). |
| scheme_name | TEXT | Official name of the mutual fund scheme. |
| category | TEXT | Broad fund category (Equity, Debt, Hybrid, etc.). |
| sub_category | TEXT | Specific fund category (Large Cap, Mid Cap, Small Cap, etc.). |
| plan | TEXT | Investment plan (Direct or Regular). |
| launch_date | DATE | Date when the mutual fund scheme was launched. |
| benchmark | TEXT | Benchmark index used for comparison. |
| expense_ratio_pct | REAL | Annual expense ratio charged by the fund (%). |
| exit_load_pct | REAL | Exit load percentage applicable on redemption. |
| min_sip_amount | INTEGER | Minimum amount required for SIP investment (₹). |
| min_lumpsum_amount | INTEGER | Minimum one-time investment amount (₹). |
| fund_manager | TEXT | Name of the fund manager. |
| risk_category | TEXT | Risk level of the scheme. |
| sebi_category_code | TEXT | SEBI classification code of the scheme. |

# 02_nav_history.csv

**Source Reference:** AMFI India (www.amfiindia.com), mfapi.in (api.mfapi.in/mf/{code})

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| date | DATE | NAV reporting date. |
| amfi_code | INTEGER | Mutual fund identifier. |
| nav | REAL | Net Asset Value per unit. |

# 03_aum_by_fund_house.csv

**Source Reference:** AMFI Industry AUM Reports

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| date | DATE | Reporting date of AUM data. |
| fund_house | TEXT | Asset Management Company name. |
| aum_lakh_crore | REAL | Assets Under Management in lakh crores. |
| aum_crore | REAL | Assets Under Management in crores. |
| num_schemes | INTEGER | Number of schemes managed by the AMC. |

# 04_monthly_sip_inflows.csv

**Source Reference:** AMFI Monthly SIP Reports

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| month | DATE | Reporting month. |
| sip_inflow_crore | REAL | Monthly SIP inflow (₹ Crores). |
| active_sip_accounts_crore | REAL | Active SIP accounts (Crores). |
| new_sip_accounts_lakh | REAL | New SIP accounts opened (Lakhs). |
| sip_aum_lakh_crore | REAL | SIP Assets Under Management (Lakh Crores). |
| yoy_growth_pct | REAL | Year-over-Year SIP growth percentage. |

# 05_category_inflows.csv

**Source Reference:** AMFI Category-wise Flow Reports

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| month | DATE | Reporting month. |
| category | TEXT | Mutual fund category. |
| net_inflow_crore | REAL | Net inflow into the category (₹ Crores). |

# 06_industry_folio_count.csv

**Source Reference:** AMFI Industry Folio Statistics

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| month | DATE | Reporting month. |
| total_folios_crore | REAL | Total investor folios (Crores). |
| equity_folios_crore | REAL | Equity mutual fund folios (Crores). |
| debt_folios_crore | REAL | Debt mutual fund folios (Crores). |
| hybrid_folios_crore | REAL | Hybrid mutual fund folios (Crores). |
| others_folios_crore | REAL | Folios in other fund categories (Crores). |

# 07_scheme_performance.csv

**Source Reference:** AMFI India (www.amfiindia.com), mfdata.in (mfdata.in/api/v1/schemes/)

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| amfi_code | INTEGER | Mutual fund identifier. |
| scheme_name | TEXT | Mutual fund scheme name. |
| fund_house | TEXT | Asset Management Company. |
| category | TEXT | Fund category. |
| plan | TEXT | Investment plan type. |
| return_1yr_pct | REAL | One-year annualized return (%). |
| return_3yr_pct | REAL | Three-year annualized return (%). |
| return_5yr_pct | REAL | Five-year annualized return (%). |
| benchmark_3yr_pct | REAL | Three-year benchmark return (%). |
| alpha | REAL | Risk-adjusted excess return. |
| beta | REAL | Market sensitivity measure. |
| sharpe_ratio | REAL | Risk-adjusted performance ratio. |
| sortino_ratio | REAL | Downside risk-adjusted return ratio. |
| std_dev_ann_pct | REAL | Annualized volatility (%). |
| max_drawdown_pct | REAL | Maximum decline from peak value (%). |
| aum_crore | REAL | Assets Under Management (₹ Crores). |
| expense_ratio_pct | REAL | Annual expense ratio (%). |
| morningstar_rating | INTEGER | Morningstar rating (1–5). |
| risk_grade | TEXT | Overall risk grade of the scheme. |

# 08_investor_transactions.csv

**Source Reference:** Simulated Investor Transaction Dataset (Derived using publicly available mutual fund market data)

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| investor_id | TEXT | Unique investor identifier. |
| transaction_date | DATE | Date of transaction. |
| amfi_code | INTEGER | Mutual fund identifier. |
| transaction_type | TEXT | SIP, Lumpsum, or Redemption. |
| amount_inr | REAL | Transaction amount (₹). |
| state | TEXT | Investor's state. |
| city | TEXT | Investor's city. |
| city_tier | TEXT | City classification (T30/B30). |
| age_group | TEXT | Investor age category. |
| gender | TEXT | Investor gender. |
| annual_income_lakh | REAL | Annual income (Lakhs). |
| payment_mode | TEXT | Mode of payment. |
| kyc_status | TEXT | KYC verification status. |

# 09_portfolio_holdings.csv

**Source Reference:** Mutual Fund Portfolio Disclosure Reports (AMFI / AMC)

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| amfi_code | INTEGER | Mutual fund identifier. |
| stock_symbol | TEXT | NSE/BSE trading symbol. |
| stock_name | TEXT | Company name. |
| sector | TEXT | Industry sector. |
| weight_pct | REAL | Percentage weight of the stock in the portfolio. |
| market_value_cr | REAL | Market value of the holding (₹ Crores). |
| current_price_inr | REAL | Current market price of the stock (₹). |
| portfolio_date | DATE | Portfolio reporting date. |

# 10_benchmark_indices.csv

**Source Reference:** NSE India (www.nseindia.com), BSE India (www.bseindia.com)

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| date | DATE | Trading date. |
| index_name | TEXT | Benchmark index name (e.g., NIFTY50). |
| close_value | REAL | Closing value of the benchmark index. |