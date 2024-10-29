import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from etfs_info import ETFs_Data
import os
from fpdf import FPDF  # Añadimos la librería FPDF para generar PDF

# Aplicar el estilo de Seaborn a los gráficos
sns.set(style="whitegrid")
sns.set_palette("muted")

# Cargar el logo de Allianz desde un archivo local
if os.path.exists("allianz.svg"):
    st.image("allianz.svg", width=200)
else:
    st.write("Logotipo no disponible")





