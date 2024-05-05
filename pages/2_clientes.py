import pandas as pd
import numpy as np
import streamlit as st
import webbrowser
from datetime import datetime
import plotly.express as px
import dash
from dash import dcc, html
from geopy.geocoders import Nominatim

df = st.session_state["data"]

app = dash.Dash(__name__)


fig_6 = px.pie(df, values='valor_compra(usd)', names='categoria', title='Participação de vendas por categoria')
st.plotly_chart(fig_6)


contagem_codigos = df['código_promocional'].value_counts().reset_index()
contagem_codigos.columns = ['código_promocional', 'Contagem']

fig_7 = px.bar(contagem_codigos, x='código_promocional', y='Contagem', title='Contagem de uso de códigos promocionais')
#st.plotly_chart(fig_7, use_container_width=True)



