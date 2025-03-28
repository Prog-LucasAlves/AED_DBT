import streamlit as st
import pandas as pd
import sql_utils
import plotly.express as px

st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

st.markdown("<h1 style='text-align: center;'>📈 Dashboard de Vendas</h1>", unsafe_allow_html=True)

####### Query ######
valorTotalCanalVenda = pd.DataFrame(sql_utils.execute_query("SELECT * FROM public_raw.raw_valor_total_canal_venda"))
valorTotalFormaPagamento = pd.DataFrame(sql_utils.execute_query("SELECT * FROM public_raw.raw_valor_total_forma_pagamento"))

####### Colunas #####
col1, col2, col3 = st.columns(3)

####### 🔵 Vendas por Canal de Venda 🔵 #######
with col1:

    # Exibindo os dados em formato de tabela
    st.markdown("<h2 style='font-size:22px;'>📊 Dados de Vendas por Canal de Venda</h2>", unsafe_allow_html=True)
    st.dataframe(valorTotalCanalVenda)

    # Criando um gráfico de barras para mostrar o total de vendas por canal
    fig = px.bar(valorTotalCanalVenda,
                 x='descricao_canal_venda',
                 y='total_formatado',
                 title="Total de Vendas por Canal de Venda",
                 labels={'descricao_canal_venda': 'Canal de Venda', 'total_formatado': 'Total de Vendas'},
                 color='total_formatado',
                 color_continuous_scale='Viridis')
    fig.update_layout(title_font_size=22)

    # Exibindo o gráfico
    st.plotly_chart(fig)

    # Verifica se a coluna 'percentual' existe antes de criar o gráfico de pizza
    if 'percentual' in valorTotalCanalVenda.columns:
        fig_pie = px.pie(valorTotalCanalVenda,
                         names='descricao_canal_venda',
                         values='percentual',
                         title="Distribuição Percentual de Vendas por Canal de Venda",
                         labels={'descricao_canal_venda': 'Canal de Venda', 'percentual': 'Percentual'})
        fig_pie.update_layout(title_font_size=22)

        # Exibindo o gráfico de pizza dentro do mesmo bloco
        st.plotly_chart(fig_pie)
    else:
        st.warning("A coluna 'percentual' não foi encontrada no banco de dados.")

####### 🔵 Vendas por Forma de Pagamento 🔵 #######

with col2:

    # Exibindo os dados em formato de tabela
    st.markdown("<h2 style='font-size:22px;'>📊 Dados de Vendas por Forma de Pagamento</h2>", unsafe_allow_html=True)
    st.dataframe(valorTotalFormaPagamento)

    # Criando um gráfico de barras para mostrar o total de vendas por canal
    fig = px.bar(valorTotalFormaPagamento,
                 x='descricao_metodo_pagamento',
                 y='total_formatado',
                 title="Total de Vendas por Canal de Venda",
                 labels={'descricao_metodo_pagameto': 'Canal de Venda', 'total_formatado': 'Total de Vendas'},
                 color='total_formatado',
                 color_continuous_scale='Viridis')
    fig.update_layout(title_font_size=22)

    # Exibindo o gráfico
    st.plotly_chart(fig)

    # Verifica se a coluna 'percentual' existe antes de criar o gráfico de pizza
    if 'percentual' in valorTotalFormaPagamento.columns:
        fig_pie = px.pie(valorTotalFormaPagamento,
                         names='descricao_metodo_pagamento',
                         values='percentual',
                         title="Distribuição Percentual de Vendas por Canal de Venda",
                         labels={'descricao_metodo_pagamento': 'Canal de Venda', 'percentual': 'Percentual'})
        fig_pie.update_layout(title_font_size=22)

        # Exibindo o gráfico de pizza dentro do mesmo bloco
        st.plotly_chart(fig_pie)
    else:
        st.warning("A coluna 'percentual' não foi encontrada no banco de dados.")
