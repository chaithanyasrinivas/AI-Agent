from dotenv import load_dotenv
load_dotenv()  

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
    response = model.generate_content([prompt[0], question])
    return response.text

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
    except Exception as e:
        rows = [("SQL ERROR: " + str(e),)]
    conn.close()
    return rows

prompt = ["""
You are an expert in converting English business questions to SQL queries!
The SQL database file is ecommerce.db and it has these tables:

PRODUCT_LEVEL_AD_SALES_METRICS (date TEXT, item_id INTEGER, ad_sales REAL, impressions INTEGER, ad_spend REAL, clicks INTEGER, units_sold INTEGER)
PRODUCT_LEVEL_TOTAL_SALES_METRICS (date TEXT, item_id INTEGER, total_sales REAL, total_units_ordered INTEGER)
PRODUCT_LEVEL_ELIGIBILITY (eligibility_datetime_utc TEXT, item_id INTEGER, eligibility TEXT, message TEXT)

Always generate valid SQLite SQL. Do NOT include the word 'SQL:' in your answer. Do not use ```
"""]

st.set_page_config(page_title="AI Agent for E-commerce SQL Q&A")
st.header("E-commerce Gemini SQL App")

question = st.text_input("Ask a business question about the data:")
submit = st.button("Ask")

if submit and question:
    sql_query = get_gemini_response(question, prompt)
    st.subheader("Generated SQL Query:")
    st.code(sql_query)
    results = read_sql_query(sql_query, "ecommerce.db")
    st.subheader("Result:")
    for row in results:
        st.write(row)