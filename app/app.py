import streamlit as st
import pandas as pd
import dbt_utils
import sql_utils

st.set_page_config(page_title="DBT & SQL App", layout="wide")

tab1, tab2 = st.tabs(["📊 SQL Query", "📈 Visualizações"])

# ====================== 🔵 ABA SQL QUERY ==========================

with tab1:
    st.title("📊 SQL Query Executor")

    if st.button("🔄 Testar Conexão"):
        st.write(sql_utils.test_connection())

    st.header("📄 Consultas SQL")

    query = st.text_area("Digite sua query SQL:")
    if st.button("Executar Query"):
        if query:
            df = sql_utils.execute_query(query)
            if df is not None:
                st.dataframe(df)
            else:
                st.error("Erro ao executar a query.")
        else:
            st.warning("Digite uma consulta SQL válida.")


# ====================== 🔴 ABA VISUALIZAÇÕES ======================
