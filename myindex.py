import pandas as pd
import numpy as np
import streamlit as st
import webbrowser
from datetime import datetime
import plotly.express as px
import dash
from dash import dcc
from dash import html 
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash.dependencies import Input, Output

from app import*
from components import sidebar, dashboards, pagina


# -------------------- LAYOUT ----------------------- #
content = html.Div(id="page-content")

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id='url'),
            sidebar
        ], md=2, style={'background-color': 'red', 'height': '1080px'}),
        dbc.Col([
            content
        ], md=10, style={'background-color': 'red', 'height': '1080px'})
    ])
], fluid=True)

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def render_page(pathname):
    if pathname == '/' or pathname == '/dashboards':
            return dashboards.layout
    if pathname == '/pagina':
            return pagina.layout



if __name__ == '__main__':
    app.run_server(port=8051, debug = True)
