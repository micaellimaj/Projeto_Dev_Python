import pandas as pd
import numpy as np
import streamlit as st
import webbrowser
from datetime import datetime
import plotly.express as px
import dash
from dash import dcc, html
from geopy.geocoders import Nominatim


caminho_do_arquivo = "datasets\df.csv"

# conexão entre as páginas

if "data" not in st.session_state:
    df = pd.read_csv(caminho_do_arquivo)
    st.session_state["data"] = df

st.set_page_config(layout="wide")

# Incorporação do Dash
app = dash.Dash(__name__)

st.write("# Análise de Perfil de Clientes ")
st.sidebar.markdown("teste")



btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset")

st.markdown(
    """
    Este conjunto de dados abrange vários recursos relacionados às preferências de compra dos clientes, reunindo informações essenciais para empresas que buscam aprimorar o entendimento de sua base de clientes. Os recursos incluem idade do cliente, sexo, valor da compra, métodos de pagamento preferidos, frequência de compras e avaliações de feedback. Além disso, são incluídos dados sobre o tipo de itens adquiridos, frequência de compras, épocas de compras preferidas e interações com ofertas promocionais.
    """
)



col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_1 = px.bar(df, x="item_comprado", y="valor_compra(usd)", title="Valor de Compra por item")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.bar(df, x="valor_compra(usd)", y="temporada_compra", title="Valor de Compra por Temporada", orientation="h")
col2.plotly_chart(fig_2, use_container_width=True)

localizacao_total = df.groupby("localização")[["valor_compra(usd)"]].sum().reset_index()
fig_3 = px.bar(localizacao_total, x="localização", y="valor_compra(usd)", title="Valor de Compra por Localização")
col3.plotly_chart(fig_3, use_container_width=True)

fig_4 = px.pie(df, values="valor_compra(usd)",names="método_pagamento", title="Valor de Compra por Método de Pagamento")
col4.plotly_chart(fig_4, use_container_width=True)

avaliacao_total = df.groupby("localização")[["classificação_cliente_compra"]].mean().reset_index()
fig_5 = px.bar(avaliacao_total, x="localização", y="classificação_cliente_compra", title="Classificação por Localização")
col5.plotly_chart(fig_5, use_container_width=True)




