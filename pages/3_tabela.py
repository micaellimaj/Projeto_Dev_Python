# Importando as Bibliotecas:
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image

st.set_page_config(page_title="Clothing Store -  Clientes", page_icon=":bar_chart:", layout="wide")


#if "data" not in st.session_state:
df_data = pd.read_csv("datasets/df.csv")
st.session_state["data"] = df_data



# SIDEBAR --------------------------------------------------
with st.sidebar:
    logo_teste = Image.open("imagem/logo.jpeg")
    st.image(logo_teste, use_column_width=True)
    st.subheader('Seleção de filtros:')
    
    # Adicione a opção "Todos" como a primeira opção para cada filtro
    fCategoria = st.selectbox(
        "Categoria do Cliente:",
        options=['Todos'] + list(df_data['categoria'].unique())
    )
    fSexo = st.selectbox(
        "Sexo do Cliente:",
        options=['Todos', 'Masculino', 'Feminino']  # Adicione 'Todos' e outras opções de sexo
    )
    fAssinatura = st.selectbox(
        "Cliente Assinante:",
        options=['Todos', 'Sim', 'Não']  # Adicione 'Todos' e outras opções de assinatura
    )
    fDesconto = st.selectbox(
        "Desconto na Compra:",
        options=['Todos'] + list(df_data['desconto_compra'].unique())
    )
    fCodigo = st.selectbox(
        "Código Promocional:",
        options=['Todos'] + list(df_data['código_promocional'].unique())
    )

# Aplicar filtros apenas se não for selecionada a opção 'Todos'
if fCategoria != 'Todos':
    df_data = df_data[df_data['categoria'] == fCategoria]
if fSexo != 'Todos':
    df_data = df_data[df_data['sexo'] == fSexo]
if fAssinatura != 'Todos':
    df_data = df_data[df_data['assinatura_cliente'] == fAssinatura]
if fDesconto != 'Todos':
    df_data = df_data[df_data['desconto_compra'] == fDesconto]
if fCodigo != 'Todos':
    df_data = df_data[df_data['código_promocional'] == fCodigo]




# ----------------- MAINPAGE -----------------

st.title(":bar_chart: Clothing Store - Clientes")
st.markdown("##")



# TOP KPI'S
total_compras = int(df_data["valor_compra(usd)"].sum())
total_clientes = int(df_data["id_cliente"].count())
media_avaliacao = round(df_data["classificação_cliente_compra"].mean(),1)
star_avaliacao = ":star:" * int(round(media_avaliacao, 0))
total_transacoes = int(df_data["transações_concluidas_cliente"].sum())
media_idade = round(df_data["idade"].mean(),1)


left_column,  middle_left_column, middle_column, middle_right_column, right_column = st.columns(5, gap='large')
with left_column:
    st.info("📊 Total Vendas:")
    st.subheader(f"US $ {total_compras:,}")
with middle_left_column:
    st.info("📊 Transações Concluídas")
    st.subheader(f"{total_transacoes}")
with middle_column:
    st.info("📊 Média de Avaliação:")
    st.subheader(f"{star_avaliacao}")
with middle_right_column:
    st.info("📊 Média de idade: ")
    st.subheader(f"{media_idade:,}")
with right_column:
    st.info("📊 Total Clientes: ")
    st.subheader(f"{total_clientes:,}")

st.markdown("---")

# ------------------ STREAMLIT STYLE ------------- 

hide_st_style = """
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            header {visibility:hidden;}
            </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

