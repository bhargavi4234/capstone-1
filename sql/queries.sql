-- =====================================================
-- QUERY 1: Top 5 Funds by AUM
-- =====================================================

SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;


-- =====================================================
-- QUERY 2: Average NAV Per Month
-- =====================================================

SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- =====================================================
-- QUERY 3: Funds with Expense Ratio < 1%
-- =====================================================

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- =====================================================
-- QUERY 4: SIP YoY Growth
-- =====================================================

SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount_inr) AS total_sip_amount
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;


-- =====================================================
-- QUERY 5: Transactions by State
-- =====================================================

SELECT
    state,
    COUNT(*) AS total_transactions,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;


-- =====================================================
-- QUERY 6: Average NAV by Fund
-- =====================================================

SELECT
    amfi_code,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC;


-- =====================================================
-- QUERY 7: Top 10 Performing Funds
-- =====================================================

SELECT
    scheme_name,
    return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;


-- =====================================================
-- QUERY 8: Category-wise Average Return
-- =====================================================

SELECT
    category,
    AVG(return_1yr_pct) AS avg_return
FROM fact_performance
GROUP BY category
ORDER BY avg_return DESC;


-- =====================================================
-- QUERY 9: KYC Status Distribution
-- =====================================================

SELECT
    kyc_status,
    COUNT(*) AS investor_count
FROM fact_transactions
GROUP BY kyc_status
ORDER BY investor_count DESC;


-- =====================================================
-- QUERY 10: Fund House Wise AUM
-- =====================================================

SELECT
    fund_house,
    SUM(aum_crore) AS total_aum
FROM fact_performance
GROUP BY fund_house
ORDER BY total_aum DESC;