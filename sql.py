import pandas as pd
import sqlite3

ad_sales = "Product-Level Ad Sales and Metrics (mapped) - Product-Level Ad Sales and Metrics (mapped).csv"
total_sales = "Product-Level Total Sales and Metrics (mapped) - Product-Level Total Sales and Metrics (mapped).csv"
eligibility = "Product-Level Eligibility Table (mapped) - Product-Level Eligibility Table (mapped).csv"

df_ad_sales = pd.read_csv(ad_sales)
df_total_sales = pd.read_csv(total_sales)
df_eligibility = pd.read_csv(eligibility)

conn = sqlite3.connect("ecommerce.db")

df_ad_sales.to_sql("PRODUCT_LEVEL_AD_SALES_METRICS", conn, if_exists="replace", index=False)
df_total_sales.to_sql("PRODUCT_LEVEL_TOTAL_SALES_METRICS", conn, if_exists="replace", index=False)
df_eligibility.to_sql("PRODUCT_LEVEL_ELIGIBILITY", conn, if_exists="replace", index=False)

conn.close()
print("All tables created successfully in ecommerce.db.")