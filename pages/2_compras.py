# Importando as Bibliotecas
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image


st.set_page_config(page_title="Clothing Store -  Compras", page_icon="💰", layout="wide")


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
    flocalizacao = st.selectbox(
        "Localização do Cliente:",
        options=['Todos'] + list(df_data['localização'].unique())
    )
    fSexo = st.selectbox(
        "Sexo do Cliente:",
        options=['Todos', 'Masculino', 'Feminino']  # Adicione 'Todos' e outras opções de sexo
    )
    ftemporada = st.selectbox(
        "Temporada Compra:",
        options=['Todos'] + list(df_data['temporada_compra'].unique())
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
if flocalizacao != 'Todos':
    df_data = df_data[df_data['localização'] == flocalizacao]
if ftemporada != 'Todos':
    df_data = df_data[df_data['temporada_compra'] == ftemporada]


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
    st.subheader(f"{star_avaliacao}({media_avaliacao})")
with middle_right_column:
    st.info("💰 Média de idade: ")
    st.subheader(f"{media_idade:,}")
with right_column:
    st.info("💰 Total Clientes: ")
    st.subheader(f"{total_clientes:,}")

st.markdown("---")

# Divisão da tela


col2, col3 = st.columns(2)
col4, col5, col6 = st.columns(3)	

# Fig 1 

fig1 = px.treemap(df_data, path=['categoria','item_comprado','tamanho_item'], values='valor_compra(usd)', title='Valor de Compra(usd) por categoria , itens comprados e tamanho do item')
st.plotly_chart(fig1, use_container_width=True)


# Fig 2
fig2 = px.choropleth(df_data,
                    locations='codigo_regiao', # Substitua 'localização' pelo nome correto da coluna que contém os códigos de localização
                    locationmode='USA-states', # Ou 'region codes', dependendo do seu conjunto de dados
                    color='valor_compra(usd)', # Variável de cor
                    hover_name='localização', # Nome da coluna para mostrar ao passar o mouse
                    title='Valor de Compra por Localização',
                    color_continuous_scale='Viridis',
                    scope='usa'
                    )
col2.plotly_chart(fig2, use_container_width=True)

# fig 3
fig3 = px.pie(df_data,values="valor_compra(usd)", names="temporada_compra", title="Valor da Compra por temporada")
fig3.update_traces(textinfo='percent+label')
fig3.update_layout(
    legend_title="Temporada Compra",
    showlegend=True
)
col3.plotly_chart(fig3, use_container_width=True)

# fig 4
fig4 = px.bar(df_data,x="método_pagamento", y="valor_compra(usd)", title="Valor da Compra por Método de Pagamento")
fig4.update_layout(
    xaxis_title="Método de Pagamento",
    yaxis_title="Clientes"
)
col4.plotly_chart(fig4, use_container_width=True)

# Fig 5
fig5 = px.bar(df_data,x="tipo_envio_cliente", y="valor_compra(usd)", title="Valor da Compra por tipo de envio")
fig5.update_layout(
    xaxis_title="Tipo de Envio",
    yaxis_title="Clientes"
)
col5.plotly_chart(fig5, use_container_width=True)



fig6 = px.bar(df_data,x="frequência_compras_cliente", y="valor_compra(usd)", title="Valor da Compra por Frequência de Compra do Cliente")
fig6.update_layout(
    xaxis_title="Frequência de Compras",
    yaxis_title="Clientes"
)
col6.plotly_chart(fig6, use_container_width=True)
