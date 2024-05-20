import pandas as pd
import numpy as np
import streamlit as st
import webbrowser
from datetime import datetime
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go 

app = dash.Dash(__name__)

caminho_do_arquivo = "datasets\\df.csv"
df = pd.read_csv(caminho_do_arquivo)

# conexão entre as páginas



# fig1 
"""
fig = px.scatter(df,x = "valor_compra(usd)", y = "idade",
                 size = "classificação_cliente_compra", color = "localização", hover_name="localização",
                 log_x = True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id = 'valor-compra-vs-cliente',
        figure = fig
    )                      
])
1
app.run_server(debug=True)
"""
app.layout = html.Div([
    dcc.Graph(id='valor-compra-vs-cliente')
])

# Callback para atualizar o gráfico
@app.callback(
    dash.dependencies.Output('valor-compra-vs-cliente', 'figure'),
    [dash.dependencies.Input('input-data-date-picker', 'date')])
def update_graph(selected_date):
    filtered_df = df[df['data'] == selected_date]  # Supondo que 'data' seja uma coluna de datas
    fig = go.Figure(data=[go.Scatter(x=filtered_df['valor_compra(usd)'], y=filtered_df['idade'],
                                     mode='markers',
                                     marker=dict(size=filtered_df['classificação_cliente_compra']*10,
                                                  color=filtered_df['localização']))])
    fig.update_layout(title='Valor Compra vs Idade',
                      xaxis_title='Valor Compra (USD)',
                      yaxis_title='Idade')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)







