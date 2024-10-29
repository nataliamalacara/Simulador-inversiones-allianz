import streamlit as st
import yfinance as yf

# Datos de los ETFs con nombres, descripciones y símbolos corregidos
ETFs_Data = {
    "AZ China": "ASHR",
    "AZ MSCI TAIWAN INDEX FD": "EWT",
    "AZ RUSSELL 2000": "IWM",
    "AZ Brasil": "EWZ",
    "AZ MSCI UNITED KINGDOM": "EWU",
    "AZ DJ US FINANCIAL SECT": "IYF",
    "AZ BRIC": "BKF",
    "AZ MSCI SOUTH KOREA IND": "EWY",
    "AZ BARCLAYS AGGREGATE": "AGG",
    "AZ Mercados Emergentes": "EEM",
    "AZ MSCI EMU": "EZU",
    "AZ FTSE/XINHUA CHINA 25": "FXI",
    "AZ Oro": "GLD",
    "AZ LATIXX MEX CETETRAC": "MXX",
    "AZ QQQ NASDAQ 100": "QQQ",
    "AZ MSCI ASIA EX-JAPAN": "AAXJ",
    "AZ LATIXX MEX M10TRAC": "M10.MX",
    "AZ BARCLAYS 1-3 YEAR TR": "SHY",
    "AZ MSCI ACWI INDEX FUND": "ACWI",
    "AZ LATIXX MEXICO M5TRAC": "M5TRAC.MX",
    "AZ SILVER TRUST": "SLV",
    "AZ MSCI HONG KONG INDEX": "EWH",
    "AZ LATIXX MEX UDITRAC": "UDITRAC.MX",
    "AZ SPDR S&P 500 ETF TRUST": "SPY",
    "AZ MSCI JAPAN INDEX FD": "EWJ",
    "AZ BG EUR GOVT BOND 1-3": "IBGE.MI",
    "AZ SPDR DJIA TRUST": "DIA",
    "AZ MSCI FRANCE INDEX FD": "EWQ",
    "AZ DJ US OIL & GAS EXPL": "IEO",
    "AZ VANGUARD EMERGING MARKET ETF": "VWO",
    "AZ MSCI AUSTRALIA INDEX": "EWA",
    "AZ IPC LARGE CAP T R TR": "LCT.MX",
    "AZ FINANCIAL SELECT SECTOR SPDR": "XLF",
    "AZ MSCI CANADA": "EWC",
    "AZ S&P LATIN AMERICA 40": "ILF",
    "AZ HEALTH CARE SELECT SECTOR": "XLV",
    "AZ MSCI GERMANY INDEX": "EWG",
    "AZ DJ US HOME CONSTRUCT": "ITB"
}

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





