# Importando as Bibliotecas
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.write("Análise de vendas")

df_data = pd.read_csv("datasets/df.csv")
st.session_state["data"] = df_data

# Divisão da tela

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Fig 1 (Teste)
fig_1 = px.bar(df_data, x = "item_comprado", y="valor_compra(usd)", title="valor comprado por item")
st.plotly_chart(fig_1, use_container_width=True)



# Carregando o arquivo de mapeamento (substitua 'path/to/state-codes.csv' pelo caminho real do arquivo)
map_df = pd.read_csv('datasets/state-codes.csv')

# Função para mapear nomes de estados para códigos FIPS
def state_to_fips(state_name):
    mapped_state = map_df[map_df['name'] == state_name.upper()]['code']
    if not mapped_state.empty:
        return mapped_state.iloc[0]
    else:
        print(f"Estado {state_name} não encontrado.")
        return None

# Aplicando a função de mapeamento
df_data['location_code'] = df_data['localização'].apply(state_to_fips)


# Criação do gráfico de mapa de calor
fig2 = px.choropleth(
    data_frame=df_data,
    locationmode='USA-states',  # Define que estamos usando códigos de estado dos EUA
    locations='localização',  # Coluna que contém os códigos de estado
    scope="usa",  # Limita o mapa aos Estados Unidos
    color='valor_compra(usd)',  # Coluna usada para a escala de cores
    hover_data=['localização', 'valor_compra(usd)'],  # Dados adicionais mostrados ao passar o mouse
    color_continuous_scale=px.colors.sequential.YlOrRd,  # Escolha da paleta de cores
    labels={'valor_compra(usd)': '% of Value Purchased'},  # Renomeia a legenda
    template='plotly_dark'  # Escolha do tema visual
)

# Exibição do gráfico no Streamlit
st.plotly_chart(fig2, use_container_width=True)