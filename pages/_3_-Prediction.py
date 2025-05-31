
import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Cargar el modelo entrenado
with open("models/modelo_entrenado.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🔮 Predicción del Precio de un Piso en Madrid")

st.write("Introduce los datos del piso para obtener una estimación de su precio actual.")

# Inputs del usuario
zona = st.selectbox("Zona", [
    "zona_barajas", "zona_barrio-de-salamanca", "zona_carabanchel", "zona_centro",
    "zona_chamartin", "zona_chamberi", "zona_ciudad-lineal", "zona_fuencarral",
    "zona_hortaleza", "zona_latina", "zona_moncloa", "zona_moratalaz",
    "zona_puente-de-vallecas", "zona_retiro", "zona_san-blas", "zona_tetuan",
    "zona_usera", "zona_vicalvaro", "zona_villa-de-vallecas", "zona_villaverde"
])

metros = st.number_input("Metros cuadrados", min_value=10, max_value=1000, value=70)
habitaciones = st.number_input("Número de habitaciones", min_value=1, max_value=10, value=2)
baños = st.number_input("Número de baños", min_value=1, max_value=5, value=1)
ascensor = st.selectbox("¿Tiene ascensor?", ["S", "N"])
localizacion = st.selectbox("Localización", ["EXTERIOR", "INTERIOR"])
planta = st.selectbox("Planta", ["BAJO", "1ª", "2ª", "3ª", "4ª", "5ª", "6ª", "ÁTICO"])

# Transformaciones
ascensor_bin = 1 if ascensor == "S" else 0
localizacion_bin = 1 if localizacion == "EXTERIOR" else 0
def transformar_planta(p):
    if "ÁTICO" in p:
        return 100
    elif "BAJO" in p:
        return 0
    else:
        return int(p.replace("ª", ""))

planta_val = transformar_planta(planta)

# Crear input vector
input_data = {
    "metros": metros,
    "habitaciones": habitaciones,
    "ascensor": ascensor_bin,
    "localizacion": localizacion_bin,
    "planta": planta_val,
    "baños": baños
}

# Añadir columnas de zona con 0s y activar solo la seleccionada
zonas = [
    "zona_barajas", "zona_barrio-de-salamanca", "zona_carabanchel", "zona_centro",
    "zona_chamartin", "zona_chamberi", "zona_ciudad-lineal", "zona_fuencarral",
    "zona_hortaleza", "zona_latina", "zona_moncloa", "zona_moratalaz",
    "zona_puente-de-vallecas", "zona_retiro", "zona_san-blas", "zona_tetuan",
    "zona_usera", "zona_vicalvaro", "zona_villa-de-vallecas", "zona_villaverde"
]
for z in zonas:
    input_data[z] = 1 if z == zona else 0

# Convertir a DataFrame
input_df = pd.DataFrame([input_data])

# Predicción
if st.button("Predecir precio"):
    pred = model.predict(input_df)[0]
    st.subheader(f"💶 Precio estimado del piso: {int(pred):,} €")
