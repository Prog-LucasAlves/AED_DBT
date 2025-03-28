import streamlit as st
import pandas as pd
import sql_utils
import plotly.express as px

st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

########################
st.write("📊 Vendas por Canal de Venda")
df = st.dataframe(pd.DataFrame(sql_utils.execute_query("SELECT * FROM public_raw.raw_qtd_clientes")))

fig = px.bar(df, x="descricao_canal_venda", y="total", text="total",
             title="Vendas por Canal de Venda", labels={"descricao_canal_venda": "Canal de Venda", "total": "Total de Vendas"},
             color="descricao_canal_venda")

# Criando um gráfico de pizza
fig_pizza = px.pie(df, values='total', names='descricao_canal_venda', title='Distribuição das Vendas')

# Exibindo os gráficos no Streamlit
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig, use_container_width=True)
with col2:
    st.plotly_chart(fig_pizza, use_container_width=True)

# Exibição dos dados
st.subheader("📌 Dados Utilizados")
st.dataframe(df)
#########################
