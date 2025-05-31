import streamlit as st

st.title("Descripción de los datos")
st.markdown("""
Este conjunto de datos representa una una foto fija de las viviendas a la venta en Madrid del portal de Idealista, 
desglosando en campos la descripción indicada por el vendedor. 
Fuente: https://www.kaggle.com/datasets/fjcob1/idealista-madrid.

Campos adaptados a la app:
            
- zona: barrio o distrito de Madrid.
- PrecioActual: Precio de venta actual.
- metros: metros cuadrados.
- habitaciones: número de habitaciones.
- ascensor: si se indica que tenga o no ascensor.
- localización: Interior, exterior,…
- planta: número de planta.
- baños: número de baños.
            """)