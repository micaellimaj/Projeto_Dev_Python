import pandas as pd
import numpy as np
import streamlit as st
import webbrowser
from datetime import datetime, date
import plotly.express as px
import dash
from dash import dcc
from dash import html 
from dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import os


# -------------------- LAYOUT ----------------------- #
layout = dbc.Col([
    html.H1("MyBudget", className="text-primary"),
    html.P("By Unifavip Students", className="text-info")
    html.Hr(),

    # SEÇÃO PERFIL 

    dbc.Button(id='botão_avatar',
               children=[html.Img(src='/assests/img_hom.png', id='avatar_change', alt='Avatar',className='perfil_avatar')], style={'background-color': 'transparent','border-color': 'transparent'}
               )
    
 ---------------------   # SEÇÃO NOVO ----------------------------------------------
"""
    dbc.Row([
        dbc.Col([
            dbc.button(color='sucess', id='open-novo-receita',
                       children=['+Receita'])
        ], width=6),
            dbc.Col([
                dbc.Button(color='danger', id='open-novo-despesa', 
                           children=['-Despesas'])
            ], width=6)
        ])

        # Modal Receita 
        dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle('Adicionar receita')),
            dbc.ModalBody([

            ])
        ], id='modal-novo-receita'),
        # Modal despesa
        dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle('Adicionar despesa')),
            dbc.ModalBody([

            ])
        ], id='modal-novo-despesa'),
        """

# SEÇÃO NAV --------------------------------------------------
    html.Hr()
    dbc.Nav(
    [
        dbc.NavLink("Dashboards", href="/dashboards", active="exact"),
        dbc.NavLink("Pagina", href="/pagina", active="exact"),
    ], vertical=True, pills=True, id='nav_buttons', style={"margin-bottom":"50px"}),

    ], id='sidebar_completa')
    



## -------------------------------------- callbacks --------------------- ##

# pop-up receita

"""
@app.callback(
    Output('modal-novo-receita','is_open'),
    Input('open-novo-receita','n_clicks'),
    State('modal-novo-receita', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    
# pop-up despesa
@app.callback(
    Output('modal-novo-despesa','is_open'),
    Input('open-novo-despesa','n_clicks'),
    State('modal-novo-despesa', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    """