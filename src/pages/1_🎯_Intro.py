import pandas as pd
import streamlit as st

# Explicar problema y dataset

original_title = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Definición del problema </b></p>'
st.markdown(original_title, unsafe_allow_html=True)

st.markdown("")
st.markdown("## El objetivo de este proyecto es aplicar el análisis de sentimientos a un conjunto de datos de tweets que mencionan a Putin y Zelensky. El objetivo principal es averiguar cómo se percibe a estos líderes a lo largo del tiempo.")

st.markdown("")
st.markdown("")
original_title = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Recopilación de datos </b></p>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown("")
st.markdown('## Usaremos dos conjuntos de datos disponibles en el sitio web de Kaggle. \n ## "Los dos conjuntos de datos incluyen los principales tweets diarios que contienen la palabra clave Putin en el primer conjunto de datos y Zelensky en el segundo. Cada conjunto de datos contiene 11 columnas respectivamente, cubren el período del 01/01/2022 al 17/07/ 2022 y vienen de todo el mundo"')

padding_top = 2
padding_bottom = 1
padding_left = 0
padding_right = 0
# max_width_str = f'max-width: 100%;'
st.markdown(f'''
            <style>
                .appview-container.main.block-container {{
                    padding-top: {padding_top}rem;
                    padding-right: {padding_right}rem;
                    padding-left: {padding_left}rem;
                    padding-bottom: {padding_bottom}rem;
                }}
            </style>
            ''', unsafe_allow_html=True,
)