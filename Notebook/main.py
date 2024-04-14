import pandas as pd
import numpy as np
import streamlit as st
import pyarrow


caminho_do_arquivo = r"C:\Users\micae\OneDrive\Documentos\GitHub\Projeto_Dev_Python\archive (2)\df.csv"
dataframe = pd.read_csv(caminho_do_arquivo)


st.set_page_config(
    page_title="Clientes Dashbosrd",
    page_icon= ":bar_chart:",
    layout="wide"
)


st.header(":bar_chart: Perfil de Compras dos Clientes")
st.markdown("#")
st.markdown(""" ___ """)
st.dataframe(dataframe)