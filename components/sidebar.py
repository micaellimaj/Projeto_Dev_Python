import pandas as pd
import numpy as np
import streamlit as st
import webbrowser
from datetime import datetime, date
import plotly.express as px
import dash
from dash import dcc
from dash import html 
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import os


# -------------------- LAYOUT ----------------------- #


layout = dbc.Col([
    html.H1("MyBudget", className="text-primary"),
    html.P("By Unifavip Students", className="text-info"),
    html.Hr(),  # Adicione a vírgula aqui

    # SEÇÃO PERFIL 
    dbc.Button(
        id='botão_avatar',
        children=[
            html.Img(
                src='/assests/img_hom.png',
                id='avatar_change',
                alt='Avatar',
                className='perfil_avatar'
            )
        ],
        style={'background-color': 'transparent', 'border-color': 'transparent'}
    ),

    # SEÇÃO NAV --------------------------------------------------
    html.Hr(),
    dbc.Nav(
        [
            dbc.NavLink("Dashboards", href="/dashboards", active="exact"),
            dbc.NavLink("Pagina", href="/pagina", active="exact"),
        ],
        vertical=True,
        pills=True,
        id='nav_buttons',
        style={"margin-bottom": "50px"}
    )
], id='sidebar_completa')
