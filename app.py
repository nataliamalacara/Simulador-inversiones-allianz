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

# Función para obtener datos del ETF
def obtener_datos_etf(etf_simbolo, periodo="1y"):
    # Descargar los datos del ETF usando yfinance
    datos = yf.download(etf_simbolo, period=periodo)
    
    # Comprobar si los datos no están vacíos
    if datos.empty:
        st.error(f"No se encontraron datos para el símbolo {etf_simbolo}. Revisa el símbolo o intenta con otro período.")
        return None
    return datos

# Función principal para la app
def mostrar_informacion_etf():
    # Selección de ETF
    etf_seleccionado = st.selectbox("Selecciona un ETF", list(ETFs_Data.keys()))
    
    # Seleccionar el periodo
    periodo = st.selectbox("Selecciona el período de tiempo", ["1mo", "3mo", "6mo", "1y", "2y", "5y"])
    
    # Mostrar la descripción del ETF seleccionado
    st.write(f"Descripción de {etf_seleccionado}:")
    
    # Obtener el símbolo del ETF seleccionado
    etf_simbolo = ETFs_Data[etf_seleccionado]
    
    # Descargar y mostrar datos del ETF seleccionado
    datos_etf = obtener_datos_etf(etf_simbolo, periodo)
    
    if datos_etf is not None:
        # Mostrar los datos del ETF
        st.write(datos_etf.tail())
        
        # Cálculos básicos de rendimiento
        st.write("Cálculos básicos del ETF:")
        rendimiento = (datos_etf['Adj Close'][-1] - datos_etf['Adj Close'][0]) / datos_etf['Adj Close'][0] * 100
        st.write(f"Rendimiento en el período seleccionado: {rendimiento:.2f}%")

# Ejecutar la app
if __name__ == "__main__":
    st.title("Simulador de ETFs")
    mostrar_informacion_etf()










