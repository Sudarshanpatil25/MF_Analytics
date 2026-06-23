CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY,
    scheme_code TEXT,
    scheme_name TEXT,
    amc_name TEXT,
    category TEXT,
    sub_category TEXT
);

CREATE TABLE fact_nav (
    id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    nav_date DATE,
    nav_value REAL,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id)
);

CREATE TABLE fact_aum (
    id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    month DATE,
    aum_crores REAL,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id)
);

CREATE TABLE fact_sip (
    id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    month DATE,
    sip_inflow REAL,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id)
);

CREATE TABLE fact_transactions (
    id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    txn_date DATE,
    txn_type TEXT,
    amount REAL,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id)
);