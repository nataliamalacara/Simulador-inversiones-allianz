import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

# Función para calcular rendimiento y riesgo
def calcular_rendimiento_riesgo(datos, tasa_libre_riesgo, sp500):
    # Verificar qué columnas están presentes en los datos
    print(datos.columns)  # Esto te mostrará las columnas en la terminal
    st.write(datos.head())  # Esto mostrará las primeras filas en la app de Streamlit para revisión

    # Verificar si 'Adj Close' o 'Close' están presentes
    if 'Adj Close' in datos.columns:
        # Calcular rendimiento usando 'Adj Close'
        rendimiento = (datos['Adj Close'][-1] - datos['Adj Close'][0]) / datos['Adj Close'][0] * 100
    elif 'Close' in datos.columns:
        # Si 'Adj Close' no está presente, usar 'Close'
        rendimiento = (datos['Close'][-1] - datos['Close'][0]) / datos['Close'][0] * 100
    else:
        # Mostrar error si ninguna columna relevante está presente
        st.error("No se encontraron las columnas 'Adj Close' ni 'Close' en los datos.")
        return None, None, None, None, None

    # Continuar con el cálculo de volatilidad y otros factores de riesgo
    volatilidad = datos['Adj Close'].pct_change().std() * (252**0.5) if 'Adj Close' in datos.columns else datos['Close'].pct_change().std() * (252**0.5)

    # Aquí asumo que ya tienes alguna lógica para calcular beta, max_drawdown y alpha
    beta = calcular_beta(datos, sp500)  # Asegúrate de tener una función para calcular beta
    max_drawdown = calcular_max_drawdown(datos)  # Función para calcular max drawdown
    alpha = calcular_alpha(rendimiento, beta, tasa_libre_riesgo, sp500)  # Función para calcular alpha

    return rendimiento, volatilidad, beta, max_drawdown, alpha

# Funciones auxiliares para calcular beta, max_drawdown y alpha (deberías implementarlas)
def calcular_beta(datos, sp500):
    # Lógica para calcular beta aquí (puedes ajustar según tu necesidad)
    pass

def calcular_max_drawdown(datos):
    # Lógica para calcular max_drawdown aquí (puedes ajustar según tu necesidad)
    pass

def calcular_alpha(rendimiento, beta, tasa_libre_riesgo, sp500):
    # Lógica para calcular alpha aquí (puedes ajustar según tu necesidad)
    pass

# Ejemplo de cómo se llamaría la función principal desde la app
if __name__ == '__main__':
    # Ejemplo de descarga de datos
    ticker = 'AAPL'  # Puedes ajustar esto para el ticker que necesites
    datos = yf.download(ticker, period='1y')
    
    # Ejemplo de tasa libre de riesgo y el índice SP500
    tasa_libre_riesgo = 0.03
    sp500 = yf.download('^GSPC', period='1y')  # Usando el S&P500 como referencia
    
    # Llamada a la función para calcular el rendimiento y riesgo
    rendimiento, volatilidad, beta, max_drawdown, alpha = calcular_rendimiento_riesgo(datos, tasa_libre_riesgo, sp500)

    # Mostrar resultados en Streamlit
    if rendimiento is not None:
        st.write(f"Rendimiento: {rendimiento}%")
        st.write(f"Volatilidad: {volatilidad}%")
        st.write(f"Beta: {beta}")
        st.write(f"Max Drawdown: {max_drawdown}")
        st.write(f"Alpha: {alpha}")










