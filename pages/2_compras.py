# Importando as Bibliotecas
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px



st.set_page_config(page_title="Clothing Store - Compras", page_icon="💰", layout="wide")


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

st.title("💰 Clothing Store - Compras")
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
    st.info("💰 Total Vendas:")
    st.subheader(f"US $ {total_compras:,}")
with middle_left_column:
    st.info("💰 Transações Concluídas")
    st.subheader(f"{total_transacoes}")
with middle_column:
    st.info("💰 Média de Avaliação:")
    st.subheader(f"{star_avaliacao}")
with middle_right_column:
    st.info("💰 Média de idade: ")
    st.subheader(f"{media_idade:,}")
with right_column:
    st.info("💰 Total Clientes: ")
    st.subheader(f"{total_clientes:,}")

st.markdown("---")

# Divisão da tela

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)	

# Fig 1 

fig1 = px.treemap(df_data, path=['categoria','item_comprado'], values='valor_compra(usd)', title='Valor de Compra(usd) por categoria e itens')
col1.plotly_chart(fig1, use_container_width=True)

# Fig 2

fig2 = px.bar(df_data,x="frequência_compras_cliente", y="valor_compra(usd)", title="Valor da Compra por Frequência de Compra do Cliente")
fig2.update_layout(
    xaxis_title="Frequência de Compras",
    yaxis_title="Clientes"
)
col2.plotly_chart(fig2, use_container_width=True)



# Fig 3
fig3 = px.choropleth(df_data,
                    locations='codigo_regiao', # Substitua 'localização' pelo nome correto da coluna que contém os códigos de localização
                    locationmode='USA-states', # Ou 'region codes', dependendo do seu conjunto de dados
                    color='valor_compra(usd)', # Variável de cor
                    hover_name='localização', # Nome da coluna para mostrar ao passar o mouse
                    title='Valor de Compra por Localização',
                    color_continuous_scale='Viridis',
                    scope='usa'
                    )
col3.plotly_chart(fig3, use_container_width=True)

# fig 4
fig4 = px.pie(df_data,values="valor_compra(usd)", names="temporada_compra", title="Valor da Compra por tipo de envio")
fig4.update_traces(textinfo='percent+label')
fig4.update_layout(
    legend_title="Temporada Compra",
    showlegend=True
)
col4.plotly_chart(fig4, use_container_width=True)

# fig 5 
fig5 = px.bar(df_data,x="método_pagamento", y="valor_compra(usd)", title="Valor da Compra por Método de Pagamento")
fig5.update_layout(
    xaxis_title="Método de Pagamento",
    yaxis_title="Clientes"
)
col5.plotly_chart(fig5, use_container_width=True)

# Fig 6
fig6 = px.bar(df_data,x="tipo_envio_cliente", y="valor_compra(usd)", title="Valor da Compra por Temporada")
fig6.update_layout(
    xaxis_title="Tipo de Envio",
    yaxis_title="Clientes"
)
col6.plotly_chart(fig6, use_container_width=True)



