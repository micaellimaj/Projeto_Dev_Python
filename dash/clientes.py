import pandas as pd
import numpy as np
import streamlit as st
import webbrowser
from datetime import datetime
import plotly.express as px
import dash
from dash import dcc
from dash import html 
import plotly.graph_objs as go

app = dash.Dash(__name__)

caminho_do_arquivo = "datasets\\df.csv"
df = pd.read_csv(caminho_do_arquivo)

# Primeiro gráfico
fig1 = px.scatter(df, x="valor_compra(usd)", y="idade",
                  size="classificação_cliente_compra", color="temporada_compra", hover_name="temporada_compra",
                  log_x=True, size_max=60, color_discrete_sequence=px.colors.qualitative.Plotly)

fig1.update_layout(
    title='Relação valor (USD) de compra por idade durante temporadas',
    xaxis=dict(title='valor da compra (USD)'),
    yaxis=dict(title='idade')
)


# Segundo gráfico

fig2 = px.box(df, x="método_pagamento", y="valor_compra(usd)", color_discrete_sequence=px.colors.qualitative.Prism)

fig2.update_layout(
    title='Método de pagamento por valor de compra(USD)',
    xaxis=dict(title='Método de pagamento', automargin=True),
    yaxis=dict(title='valor da compra (USD)')
)


# Terceiro gráfico

fig3 = go.Figure()

fig3.add_trace(go.Bar(
    x=df['item_comprado'],
    y=df['valor_compra(usd)'],
    marker_color=px.colors.qualitative.Pastel1,
))

# Layout do terceiro gráfico
fig3.update_layout(
    title='Valor de Compra por item',
    xaxis=dict(title='item comprado', automargin=True),
    yaxis=dict(title='valor da compra (USD)')
)


# quarto gráfico
cores = {'Masculino': 'blue', 'Feminino': 'pink'}
labels = df['sexo']
values = df['valor_compra(usd)']

# Mapeando as cores de acordo com o sexo
cores_fatias = [cores[sexo] for sexo in labels]

fig4 = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=cores_fatias))])


# Configurando o layout
fig4.update_layout(
    title='valor da compra(USD) por sexo',
    
)

# Cálculo de valores totais, média e quantidade
total_compras = df['valor_compra(usd)'].sum()
media_avaliacao = df['classificação_cliente_compra'].mean()
media_idade = df['idade'].mean()
media_transacoes = df['transações_concluidas_cliente'].mean()
quantidade_compras = len(df)


# Layout da aplicação com ambos os gráficos
# Layout da aplicação com cartões e gráficos
# Layout da aplicação com cartões e gráficos
app.layout = html.Div([
        # Título do aplicativo
        html.H1('Sales Dash', style={'text-align': 'center'}),
    
        # Divisão para os cartões
        html.Div([
        html.Div([
            html.H3(' Total de Compras '),
            html.H4(f'${total_compras:.2f}')
        ], className='card'),
        html.Div([
            html.H3(' Média de Avaliações '),
            html.H4(f'{media_avaliacao:.2f}')
        ], className='card'),
        html.Div([
            html.H3(' Quantidade de Compras '),
            html.H4(f'{quantidade_compras}')
        ], className='card'),
        html.Div([
            html.H3(' Média de Idade '),
            html.H4(f'{media_idade:.2f}')
        ], className='card'),
        html.Div([
            html.H3(' Média de Transações '),
            html.H4(f'{media_transacoes:.2f}')
        ], className='card'),
    ], className='card-container', style={'display': 'flex' , 'justify-content': 'center'}),
    
    # Divisão para os gráficos
    html.Div([
        html.Div([
            dcc.Graph(id='valor-compra-vs-cliente', figure=fig1),
            dcc.Graph(id='boxplot-metodo-pagamento', figure=fig2),
        ], style={'display': 'flex', 'margin-bottom': '20px'}),
    ]),
    html.Div([
        dcc.Graph(id='barras-sexo-valorcompra', figure=fig3),
        dcc.Graph(id='pizza-sexo-valorcompra', figure=fig4)
    ], style={'display': 'flex'})
], style={'display': 'flex', 'flex-direction': 'column', 'margin-bottom': '20px'})


if __name__ == '__main__':
    app.run_server(debug=True)

