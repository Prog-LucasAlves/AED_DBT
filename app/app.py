import streamlit as st
import pandas as pd
import dbt_utils
import sql_utils

st.set_page_config(page_title="DBT & SQL App", layout="wide")

tab1, tab2 = st.tabs(["⚙️ DBT Executor", "📊 SQL Query"])

# ====================== 🟢 ABA DBT EXECUTOR ======================
with tab1:
    st.title("DBT Executor")

    st.subheader("📌 Modelos DBT Disponíveis")
    models = dbt_utils.list_dbt_models()

# ====================== 🔵 ABA SQL QUERY ==========================
with tab2:
    st.title("📊 SQL Query Executor")

    if st.button("🔄 Testar Conexão"):
        st.write(sql_utils.test_connection())
