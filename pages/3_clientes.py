# Importando as Bibliotecas
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Dashboard - Clientes", page_icon=":bar_chart:", layout="wide")

st.write("Análise de vendas")

df_data = pd.read_csv("datasets/df.csv")
st.session_state["data"] = df_data



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


# Página 2

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

# Divisão da tela

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Gráfico 1 

df_1 = df_data.groupby("categoria")["classificação_cliente_compra"].mean().reset_index()

fig1 = px.bar(df_1, x="categoria", y="classificação_cliente_compra", title="Média da Classificação do Cliente por Categoria")
col1.plotly_chart(fig1, use_container_width=True)

