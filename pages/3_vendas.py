import pandas as pd
import numpy as np
import streamlit as st
import webbrowser
from datetime import datetime
import plotly.express as px
import dash

df = st.session_state["data"]
