
# 🏠 Predicción de Precios de Pisos en Madrid

Este proyecto te permite estimar el precio de un piso en Madrid de forma rápida e intuitiva mediante una app construida con **Streamlit**.

## 🚀 ¿Cómo funciona?

La app utiliza un modelo de Machine Learning entrenado con datos reales de pisos en Madrid para predecir el precio de una vivienda en función de sus características.

## 🔧 ¿Qué necesitas?

1. Tener instalado **Python** en tu equipo.
2. Instalar las dependencias del proyecto con:

```bash
pip install -r requirements.txt
```

3. Lanzar la app con el siguiente comando:

```bash
streamlit run app.py
```

## 📍 ¿Dónde hacer la predicción?

En el menú lateral izquierdo de la app, accede a la **página 3 - Prediction**.

Ahí podrás introducir los datos del piso (zona, metros, número de habitaciones, planta, baños, etc.) y al pulsar el botón, obtendrás una estimación del precio actual del inmueble.

> **Nota:** El modelo ha sido entrenado con el dataset `data/pisos.csv`. Puedes modificarlo para adaptarlo a tus propios datos si lo necesitas.

---

Desarrollado como parte del Máster de Ciencia de Datos de Evolve Academy.
