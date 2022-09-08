import pandas as pd
import streamlit as st

# seteamos layout="wide" para usar más espacio (por defecto es "center")
st.set_page_config(layout="wide")

# Explicar problema y dataset

original_title = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Definición del problema </b></p>'
st.markdown(original_title, unsafe_allow_html=True)

st.markdown("")
st.markdown("## El objetivo de este proyecto es aplicar técnicas de procesamiento de lenguaje natural (NLP) a un conjunto de datos de tweets que mencionan a Putin y Zelensky. El objetivo principal es investigar cómo se percibe a estos líderes en un período de tiempo específico.")

st.markdown("")
st.markdown("")
original_title = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Recopilación de datos </b></p>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown("")
st.write('## Se utilizan dos conjuntos de datos disponibles en el sitio web de [Kaggle](https://www.kaggle.com/datasets/die9origephit/putin-and-zelensky-tweets). \n ## "Los dos conjuntos de datos incluyen los principales tweets diarios que contienen la palabra clave Putin en el primer conjunto de datos y Zelensky en el segundo. Cada conjunto de datos contiene 11 columnas respectivamente, cubren el período del 01/01/2022 al 17/07/2022 y vienen de todo el mundo"')