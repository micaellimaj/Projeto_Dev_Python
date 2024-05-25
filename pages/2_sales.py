# Importando a biblioteca Streamlit para criar a aplicação web
import streamlit as st
# Importando Pandas para manipulação de dados
import pandas as pd
# Importando NumPy para operações numéricas
import numpy as np
# Importando Matplotlib para gráficos estáticos
#import matplotlib.pyplot as plt

# Importando Seaborn para gráficos mais sofisticados
#import seaborn as sns


st.write("Análise de vendas")

df_data = pd.read_csv("datasets/df.csv")
st.session_state["data"] = df_data

# Divisão da tela

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Fig 1 (Teste)
fig_1 = px.bar(df_data, x = "item_comprado", y="valor_compra(usd)", title="valor comprado por item")
col1.ploty_chart(fig_1, use_container_width=True)