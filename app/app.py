import streamlit as st
import pandas as pd
import sql_utils
import plotly.express as px

st.set_page_config(page_title="Dashboard de Vendas", layout="wide")


st.title("📈 Dashboard de Vendas")


####### Querys ######
valorTotalCanalVenda = st.dataframe(pd.DataFrame(sql_utils.execute_query("SELECT * FROM public_raw.raw_valor_total_canal_venda")))

####### Colunas #####

col1, col2, col3, col4, col5 = st.columns(5)

####### Gráficos ####

####### 🔵 Vendas por Canal de Venda 🔵 #######

with col1:
    st.write("📊 Vendas por Canal de Venda")

    # Título do Dashboard
    st.title("Dashboard de Vendas por Canal")

    # Exibindo os dados em formato de tabela
    st.subheader("Dados de Vendas por Canal de Venda")
    st.dataframe(valorTotalCanalVenda)

    # Criando um gráfico de barras para mostrar o total de vendas por canal
    fig = px.bar(valorTotalCanalVenda,
                 x='descricao_canal_venda',
                 y='total',
                 title="Total de Vendas por Canal de Venda",
                 labels={'descricao_canal_venda': 'Canal de Venda', 'total': 'Total de Vendas'},
                 color='total',
                 color_continuous_scale='Viridis')

    # Exibindo o gráfico
    st.plotly_chart(fig)

    # Criando um gráfico de pizza para mostrar a distribuição percentual
    fig_pie = px.pie(valorTotalCanalVenda,
                     names='descricao_canal_venda',
                     values='percentual',
                     title="Distribuição Percentual de Vendas por Canal de Venda",
                     labels={'descricao_canal_venda': 'Canal de Venda', 'percentual': 'Percentual'})

    # Exibindo o gráfico de pizza
    st.plotly_chart(fig_pie)
#########################
