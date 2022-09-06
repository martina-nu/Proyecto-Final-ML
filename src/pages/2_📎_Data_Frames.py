import pandas as pd
import streamlit as st
import plotly.express as px

# seteamos layout="wide" para usar más espacio (por defecto es "center")
st.set_page_config(layout="wide")

original_title = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Datasets originales </b></p>'
st.markdown(original_title, unsafe_allow_html=True)

### --- LOAD DATAFRAME
raw_p = 'data/raw/Putin_Tweets.csv'
raw_z = 'data/raw/Zelensky_Tweets.csv'
df_raw_p = pd.read_csv(raw_p)
df_raw_z = pd.read_csv(raw_z)

Putin_title = '<p style="font-family:Arial; color:Black; font-size: 40px;">Tweets de Putin</p>'
st.markdown(Putin_title, unsafe_allow_html=True)
st.dataframe(df_raw_p.head(20))

st.markdown('')
string_p = str(df_raw_p.shape[0]) + ' filas y ' + str(df_raw_p.shape[1]) + ' columnas '
st.write(string_p)

Zelensky_title = '<p style="font-family:Arial; color:Black; font-size: 40px;">Tweets de Zelensky</p>'
st.markdown(Zelensky_title, unsafe_allow_html=True)
st.dataframe(df_raw_z.head(20))

st.markdown('')
string_z = str(df_raw_z.shape[0]) + ' filas y ' + str(df_raw_z.shape[1]) + ' columnas '
st.write(string_z)
