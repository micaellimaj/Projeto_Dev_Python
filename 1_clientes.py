# Importando as Bibliotecas:
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title="Clothing Store - Clientes", page_icon=":bar_chart:", layout="wide")


#if "data" not in st.session_state:
df_data = pd.read_csv("datasets/df.csv")
st.session_state["data"] = df_data



# SIDEBAR --------------------------------------------------
st.sidebar.image("imagem/logo.jpeg", caption="Online Clothing Store")

st.sidebar.markdown("Desenvolvido por Estudantes Unifavip")


st.sidebar.header("Selecione um filtro : ")
sexo = st.sidebar.multiselect(
    "Selecione o Sexo: ",
    options= df_data["sexo"].unique(),
    default= df_data["sexo"].unique()
)

assinatura_cliente = st.sidebar.multiselect(
    "O Cliente possui assinatura : ",
    options= df_data["assinatura_cliente"].unique(),
    default= df_data["assinatura_cliente"].unique()
)

desconto_compra = st.sidebar.multiselect(
    "O Cliente possui desconto: ",
    options= df_data["desconto_compra"].unique(),
    default= df_data["desconto_compra"].unique()
)

código_promocional = st.sidebar.multiselect(
    "O Cliente possui código Promocional: ",
    options= df_data["código_promocional"].unique(),
    default= df_data["código_promocional"].unique()
)

df_data_selection = df_data.query(
    "sexo == @sexo & assinatura_cliente == @assinatura_cliente & desconto_compra == @desconto_compra & código_promocional == @código_promocional"
)

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

# Divisão da tela (Gráficos)

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)	

df_id = df_data.groupby(["codigo_regiao", "localização","categoria","tamanho_item","cor_item","item_comprado","método_pagamento","tipo_envio_cliente","frequência_compras_cliente","temporada_compra"])["id_cliente"].count().reset_index()

fig1 = px.treemap(df_id, path=['categoria','item_comprado'], values='id_cliente', title='Total de Clientes por categoria e itens')
col1.plotly_chart(fig1, use_container_width=True)

# Gráfico 2

fig2 = px.bar(df_id,x="frequência_compras_cliente", y="id_cliente", title="Total de Clientes por Frequência de Compra")
fig2.update_layout(
    xaxis_title="Frequência de Compras",
    yaxis_title="Clientes"
)
col2.plotly_chart(fig2, use_container_width=True)

# Fig 3

df_3 = df_id.groupby(["codigo_regiao","localização"])["id_cliente"].count().reset_index()

fig3 = px.choropleth(df_3,
                    locations='codigo_regiao', # Usando os códigos de região como localização
                    locationmode='USA-states', # Ou 'region codes', dependendo do seu conjunto de dados
                    color='id_cliente', # Variável de cor baseada na contagem de id_cliente
                    hover_name='localização', # Nome da coluna para mostrar ao passar o mouse
                    title='Total de Clientes por Localização',
                    color_continuous_scale='Viridis',
                    scope='usa'
                    )
col3.plotly_chart(fig3, use_container_width=True)
# Gráfico 4


fig4 = px.pie(df_id,values="id_cliente", names="temporada_compra", title="Total de Clientes por tipo de envio")
fig4.update_traces(textinfo='percent+label')
fig4.update_layout(
    legend_title="Temporada Compra",
    showlegend=True
)
col4.plotly_chart(fig4, use_container_width=True)

# Gráfico 4 

fig5 = px.bar(df_id,x="método_pagamento", y="id_cliente", title="Total de Clientes por Método de Pagamento")
fig5.update_layout(
    xaxis_title="Método de Pagamento",
    yaxis_title="Clientes"
)
col5.plotly_chart(fig5, use_container_width=True)


# Gráfico 6

fig6 = px.bar(df_id,x="tipo_envio_cliente", y="id_cliente", title="Total de Clientes por Tipo de Envio")
fig6.update_layout(
    xaxis_title="Tipo de Envio",
    yaxis_title="Clientes"
)
col6.plotly_chart(fig6, use_container_width=True)
