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

# Segundo gráfico

fig2 = px.box(df, x="método_pagamento", y="valor_compra(usd)",color="sexo", color_discrete_sequence=px.colors.qualitative.Prism)



# Terceiro gráfico

x = df['item_comprado']
y = df['valor_compra(usd)']

data = [go.Bar(
            x=x,
            y=y,
            marker=dict(color=px.colors.qualitative.Pastel1)
    )]
layout = go.Layout(
    title='Gráfico de Barras',
    xaxis=dict(title='item_comprado'),
    yaxis=dict(title='valor da compra (USD)')
)

fig3 = go.Figure(data=data, layout=layout)

# quarto gráfico
cores = {'Masculino': 'blue', 'Feminino': 'pink'}
labels = df['sexo']
values = df['valor_compra(usd)']

fig4 = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig4.update_traces(marker=dict(colors=px.colors.qualitative.Dark2))

# Configurando o layout
fig4.update_layout(
    title='valor da compra(USD) por sexo'
)



# Layout da aplicação com ambos os gráficos
app.layout = html.Div([
    html.Div([
        dcc.Graph(id='valor-compra-vs-cliente', figure=fig1),
        dcc.Graph(id='boxplot-metodo-pagamento', figure=fig2),
    ], style={'display': 'flex'}),
    html.Div([
        dcc.Graph(id='barras-sexo-valorcompra', figure=fig3),
        dcc.Graph(id='pizza-sexo-valorcompra', figure=fig4)
    ], style={'display': 'flex'})
])


if __name__ == '__main__':
    app.run_server(debug=True)

