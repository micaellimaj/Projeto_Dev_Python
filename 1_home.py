# Importando as Bibliotecas:
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Dashboard - Estoque", page_icon=":bar_chart:", layout="wide")


#if "data" not in st.session_state:
df_data = pd.read_csv("datasets/df.csv")
st.session_state["data"] = df_data

st.write("Análise de dados")

# SIDEBAR --------------------------------------------------
st.sidebar.image("imagem/logo.jpeg", caption="Online Analytics")

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

st.title(":bar_chart: Sales Dashboard - Estoque de Produtos")
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
    st.subheader(f"{media_avaliacao} {star_avaliacao}")
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

# Divisão da tela (Gráficos)

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)


# Gráfico 1
df_1 = df_data[["categoria","id_cliente"]].groupby("categoria").agg("count").reset_index()

fig_1 = px.bar(df_1,y="id_cliente", x="categoria", title="Quantidade de Clientes por Categoria")
col1.plotly_chart(fig_1, use_container_width=True)


# Gráfico 2
df_2 = df_data[["tamanho_item","id_cliente"]].groupby("tamanho_item").agg("count").reset_index()

fig_2 = px.pie(df_2, values='id_cliente', names='tamanho_item', title='Tamanho do item por quantidade de clientes')
col2.plotly_chart(fig_2, use_container_width=True)

# Gráfico 3 

df_3 = df_data[["cor_item","id_cliente"]].groupby("cor_item").agg("count").reset_index()

fig_3 = px.bar(df_3,x="id_cliente", y="cor_item", title="Quantidade de Clientes por Cor do item")
col3.plotly_chart(fig_3, use_container_width=True)

# Gráfico 4 

df_4 = df_data[["item_comprado","id_cliente"]].groupby("item_comprado").agg("count").reset_index()

fig_4 = px.bar(df_4,x="id_cliente", y="item_comprado", title="Quantidade de Clientes por item comprado")
col4.plotly_chart(fig_4, use_container_width=True)

