import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Explorador interactivo de pisos")

df = pd.read_csv("data/pisos.csv")
st.dataframe(df)

st.sidebar.header("Filtros")
barrios = st.sidebar.multiselect("Barrio", df["zona"].unique())
precio_min, precio_max = df["PrecioActual"].min(), df["PrecioActual"].max()
price_range = st.sidebar.slider("Precio", precio_min, precio_max, (precio_min, precio_max))
habitaciones = st.sidebar.slider("Habitaciones", df["habitaciones"].min(), df["habitaciones"].max(), (df["habitaciones"].min(), df["habitaciones"].max()))

df_filtrado = df[
    (df["zona"].isin(barrios)) & # barrio
    (df["PrecioActual"].between(price_range[0], price_range[1])) & # precio
    (df["habitaciones"].between(habitaciones[0], habitaciones[1])) # habs
]

st.write(f"Se encontraron {df_filtrado.shape[0]} pisos")
st.dataframe(df_filtrado)

st.plotly_chart(px.histogram(df, x="PrecioActual")) 
#st.plotly_char(px.) # scatterplot: x, y -> metros vs. precio
st.plotly_chart(px.scatter(df, x="PrecioActual", y="metros")) 

st.plotly_chart(px.box(df, x= "zona", y="PrecioActual"))