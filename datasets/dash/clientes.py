import pandas as pd
import numpy as np
import streamlit as st
import webbrowser
from datetime import datetime
import plotly.express as px
import dash
from dash import dcc
from dash import html 

import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

caminho_do_arquivo = "datasets\\df.csv"
df = pd.read_csv(caminho_do_arquivo)

# Primeiro gráfico
fig1 = px.scatter(df, x="valor_compra(usd)", y="idade",
                  size="classificação_cliente_compra", color="temporada_compra", hover_name="temporada_compra",
                  log_x=True, size_max=60)

# Segundo gráfico

fig2 = px.box(df, x="método_pagamento", y="valor_compra(usd)",color="sexo")

# Terceiro gráfico



# Layout da aplicação com ambos os gráficos
app.layout = html.Div([
    dcc.Graph(id='valor-compra-vs-cliente', figure=fig1),
    dcc.Graph(id='boxplot-metodo-pagamento', figure=fig2),
    dcc.Graph(id='heatmap-tamanho-valorcompra', figure=fig3)
])

if __name__ == '__main__':
    app.run_server(debug=True)

