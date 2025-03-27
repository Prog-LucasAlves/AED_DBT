import streamlit as st
import pandas as pd
import dbt_utils
import sql_utils

st.set_page_config(page_title="DBT & SQL App", layout="wide")

tab1, tab2, tab3 = st.tabs(["⚙️ DBT Executor", "📊 SQL Query", "📈 Visualizações"])

# ====================== 🟢 ABA DBT EXECUTOR ======================
with tab1:
    st.title("⚙️ DBT Executor")

    st.subheader("📌 Modelos DBT Disponíveis")
    models = dbt_utils.list_dbt_models()

    if isinstance(models, list):
        selected_model = st.selectbox("Selecione um modelo:", models)
    else:
        st.error("❌ Erro ao listar modelos do dbt.")

    if st.button("🚀 Rodar Modelo"):
        result = dbt_utils.run_dbt_model(selected_model)
        st.text_area("📜 Resultado", result, height=300)


# ====================== 🔵 ABA SQL QUERY ==========================
with tab2:
    st.title("📊 SQL Query Executor")

    if st.button("🔄 Testar Conexão"):
        st.write(sql_utils.test_connection())

# ====================== 🔴 ABA VISUALIZAÇÕES ======================
with tab3:
    st.header("📈 Visualizações de Dados")

    if st.button("🔄 Carregar Dados do Banco"):
        df = sql_utils.execute_query("SELECT * FROM tb_cliente")
        if isinstance(df, pd.DataFrame):
            st.dataframe(df)
        else:
            st.error("❌ Erro ao carregar dados do banco de dados.")
