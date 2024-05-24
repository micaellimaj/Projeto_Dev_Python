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

#st.set_page_config(layout="wide")


if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/df.csv")
    st.session_state["data"] = df_data

st.write("Análise de dados")

# página --------------------------------------------------



# Lista de páginas disponíveis




# Divisão da tela

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)