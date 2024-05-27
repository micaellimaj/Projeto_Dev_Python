# Importando as Bibliotecas
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.write("Análise de vendas")

df_data = pd.read_csv("datasets/df.csv")
st.session_state["data"] = df_data

# Divisão da tela

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Fig 1 (Teste)
fig_1 = px.bar(df_data, x = "item_comprado", y="valor_compra(usd)", title="valor comprado por item")
st.plotly_chart(fig_1, use_container_width=True)

