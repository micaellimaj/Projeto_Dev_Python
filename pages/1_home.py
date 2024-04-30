import pandas as pd
import numpy as np
import streamlit as st
import webbrowser
from datetime import datetime


caminho_do_arquivo = r"C:\Users\micae\OneDrive\Documentos\GitHub\Projeto_Dev_Python\datasets\df.csv"
#dataframe = pd.read_csv(caminho_do_arquivo)

if "data" not in st.session_state:
    df_data = pd.read_csv(caminho_do_arquivo, index_col=0)
    st.session_state["data"] = df_data


st.write("# Análise de Perfil de Clientes ")
st.sidebar.markdown("teste")



btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset")

st.markdown(
    """
    Este conjunto de dados abrange vários recursos relacionados às preferências de compra dos clientes, reunindo informações essenciais para empresas que buscam aprimorar o entendimento de sua base de clientes. Os recursos incluem idade do cliente, sexo, valor da compra, métodos de pagamento preferidos, frequência de compras e avaliações de feedback. Além disso, são incluídos dados sobre o tipo de itens adquiridos, frequência de compras, épocas de compras preferidas e interações com ofertas promocionais.

    Com uma coleção de 3.900 registros, esse conjunto de dados serve como base para empresas que buscam aplicar insights baseados em dados para uma melhor tomada de decisões e estratégias centradas no cliente.
    """
)