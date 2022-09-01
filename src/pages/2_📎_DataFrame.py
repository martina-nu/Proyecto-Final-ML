import pandas as pd
import streamlit as st
import plotly.express as px

original_title = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Datasets originales </b></p>'
st.markdown(original_title, unsafe_allow_html=True)

### --- LOAD DATAFRAME
raw_p = '/workspace/Proyecto-Final-ML/data/raw/Putin_Tweets.csv'
raw_z = '/workspace/Proyecto-Final-ML/data/raw/Zelensky_Tweets.csv'

df_raw_p = pd.read_csv(raw_p)
df_raw_z = pd.read_csv(raw_z)
Zelensky_title = '<p style="font-family:Time New Roman; color:Black; font-size: 40px;">Tweets de Putin</p>'
st.markdown(Zelensky_title, unsafe_allow_html=True)
st.dataframe(df_raw_p.head(20))

Putin_title = '<p style="font-family:Time New Roman; color:Black; font-size: 40px;">Tweets de Zelensky</p>'
st.markdown(Putin_title, unsafe_allow_html=True)
st.dataframe(df_raw_z.head(20))

