# Importando as Bibliotecas:
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")


#if "data" not in st.session_state:
df_data = pd.read_csv("datasets/df.csv")
st.session_state["data"] = df_data

st.write("Análise de dados")

# SIDEBAR --------------------------------------------------
st.sidebar.markdown("Desenvolvido por Estudantes Unifavip")

st.sidebar.header("Selecione um filtro : ")
sexo = st.sidebar.multiselect(
    "Selecione o Sexo: ",
    options= df_data["sexo"].unique(),
    default= df_data["sexo"].unique()
)

assinatura = st.sidebar.multiselect(
    "O Cliente possui assinatura : ",
    options= df_data["assinatura_cliente"].unique(),
    default= df_data["assinatura_cliente"].unique()
)

desconto = st.sidebar.multiselect(
    "O Cliente possui desconto: ",
    options= df_data["desconto_compra"].unique(),
    default= df_data["desconto_compra"].unique()
)

codigo_promocional = st.sidebar.multiselect(
    "O Cliente possui código Promocional: ",
    options= df_data["código_promocional"].unique(),
    default= df_data["código_promocional"].unique()
)

df_data_selection = df_data.query(
    "sexo == @sexo & assinatura_cliente == @assinatura & desconto_compra == @desconto & código_promocional == @codigo_promocional"
)

# ----------------- MAINPAGE -----------------

st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# TOP KPI'S
total_compras = int(df_data["valor_compra(usd)"].sum())
total_clientes = int(df_data["id_cliente"].count())
media_avaliacao = round(df_data["classificação_cliente_compra"].mean(),1)
star_avaliacao = ":star:" * int(round(media_avaliacao, 0))
total_transacoes = int(df_data["transações_concluidas_cliente"].sum())
media_idade = round(df_data["idade"].mean(),1)

left_column,  middle_left_column, middle_column, middle_right_column, right_column = st.columns(5)
with left_column:
    st.subheader("Total Vendas:")
    st.subheader(f"US $ {total_compras:,}")
with middle_left_column:
    st.subheader("Total Transações Conc:")
    st.subheader(f"{total_transacoes}")
with middle_column:
    st.subheader("Média de Avaliação:")
    st.subheader(f"{media_avaliacao} {star_avaliacao}")
with middle_right_column:
    st.subheader("Média de idade: ")
    st.subheader(f"{media_idade:,}")
with right_column:
    st.subheader("Total Clientes: ")
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

# Divisão da tela (Gráficos)

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)



fig_1 = px.bar(df_data, x = "item_comprado", y="valor_compra(usd)", title="valor comprado por item")
st.plotly_chart(fig_1, use_container_width=True)

