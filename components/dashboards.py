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
import dash_bootstrap_components as dbc


card_icon = {
    "color": "white",
    "textAlign": "center",
    "fontSize": 30,
    "margin": "auto",
}

# /////////////////// Layout  ///////////////////////// #
layout = dbc.Col([
    dbc.Row([
        # Saldo
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Saldo"),
                    html.H5("R$ -", id="p-saldo-dashboards", style={}),
                ], style={"padding-left": "20px", "padding-top": "10px"}),
                dbc.Card(
                    html.Div(className="fa fa-university", style=card_icon),
                    color="warning",
                    style={"maxWidth": 75, "height": 100, "margin-left": "-10px"},
                )
            ])
        ], width=4),

        # Receita
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Receita"),
                    html.H5("R$ -", id="p-receita-dashboards"),
                ], style={"padding-left": "20px", "padding-top": "10px"}),
                dbc.Card(
                    html.Div(className="fa fa-smile-o", style=card_icon),
                    color="success",
                    style={"maxWidth": 75, "height": 100, "margin-left": "-10px"},
                )
            ])
        ], width=4),

        # Despesa
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Despesas"),
                    html.H5("R$ -", id="p-despesa-dashboards"),
                ], style={"padding-left": "20px", "padding-top": "10px"}),
                dbc.Card(
                    html.Div(className="fa fa-meh-o", style=card_icon),
                    color="danger",
                    style={"maxWidth": 75, "height": 100, "margin-left": "-10px"},
                )
            ])
        ], width=4),
    ], style={"margin": "10px"}),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Legend("Filtrar lançamentos", className="card-title"),
                html.Label("Categorias das receitas"),
                html.Div(
                    dcc.Dropdown(
                        id="dropdown-receita",
                        clearable=False,
                        style={"width": "100%"},
                        persistence=True,
                        persistence_type="session",
                        multi=True
                    )
                ),
                html.Label("Categorias das despesas", style={"margin-top": "10px"}),
                dcc.Dropdown(
                    id="dropdown-despesa",
                    clearable=False,
                    style={"width": "100%"},
                    persistence=True,
                    persistence_type="session",
                    multi=True
                )
            ], style={"height": "100%", "padding": "20px"}),
        ], width=4),

        dbc.Col(
            dbc.Card(dcc.Graph(id="graph1"), style={"height": "100%", "padding": "10px"}),
            width=8
        ),
    ], style={"margin": "10px"}),

    dbc.Row([
        dbc.Col(dbc.Card(dcc.Graph(id="graph2"), style={"padding": "10px"}), width=6),
        dbc.Col(dbc.Card(dcc.Graph(id="graph3"), style={"padding": "10px"}), width=3),
        dbc.Col(dbc.Card(dcc.Graph(id="graph4"), style={"padding": "10px"}), width=3),
    ])
], style={"margin": "10px"})