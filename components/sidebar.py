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

    
])