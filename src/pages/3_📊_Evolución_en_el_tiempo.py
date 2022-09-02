import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.express as px

# seteamos layout="wide" para usar más espacio (por defecto es "center")
st.set_page_config(layout="wide")

interim_p = '/workspace/Proyecto-Final-ML/data/interim/Putin_tweets.csv'
interim_z = '/workspace/Proyecto-Final-ML/data/interim/Zelensky_tweets.csv'

df_interim_p = pd.read_csv(interim_p)
df_interim_z = pd.read_csv(interim_z)


df_p = df_interim_p.groupby(pd.to_datetime(df_interim_p['Timestamp']).dt.strftime('%b-%Y'), sort=False)['Clean_Tweet'].size().reset_index()
df_p['President']= 'Putin'
df_z = df_interim_z.groupby(pd.to_datetime(df_interim_z['Timestamp']).dt.strftime('%b-%Y'), sort=False)['Clean_Tweet'].size().reset_index()
df_z['President']= 'Zelensky'
df = pd.concat([df_p, df_z], axis=0 )

fig = px.line(df, x='Timestamp', y='Clean_Tweet', color='President', symbol="President")

# Plot!
st.plotly_chart(fig, use_container_width=True)
