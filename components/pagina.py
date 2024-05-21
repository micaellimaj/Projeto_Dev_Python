import pandas as pd
import numpy as np
import streamlit as st
import webbrowser
from datetime import datetime, date, timedelta
import plotly.express as px
import calendar
import dash
from dash import dcc
from dash import html 
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from app import app
from dash_bootstrap_components as dbc


# /////////////////// Layout  ///////////////////////// #
layout = dbc.Col([
    dbc.Row([
        html.Legend("Tabela de despesas"),
        html.Div(id="tabela-despesas", className="dbc"),
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='bar-graph', style={"margin-right": "20px"}),
        ], width=9),
        
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H4("Despesas"),
                    html.Legend("R$ -", id="valor_despesa_card", style={'font-size': '60px'}),
                    html.H6("Total de despesas"),
                ], style={'text-align': 'center', 'padding-top': '30px'}))
        ], width=3),
    ]),
], style={"padding": "10px"})



