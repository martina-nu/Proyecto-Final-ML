import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
#import utils
import plotly.figure_factory as ff
import plotly.express as px 
import numpy as np 


# seteamos layout="wide" para usar más espacio (por defecto es "center")
st.set_page_config(layout="wide")


### --- LOAD DATAFRAME
interim_p = '/workspace/Proyecto-Final-ML/data/interim/Putin_tweets.csv'
interim_z = '/workspace/Proyecto-Final-ML/data/interim/Zelensky_tweets.csv'

df_interim_p = pd.read_csv(interim_p)
df_interim_z = pd.read_csv(interim_z)

tit = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Usuarios más frecuentes </b></p>'
st.markdown(tit, unsafe_allow_html=True)

p_title = '<p style="font-family:Time New Roman; color:Black; font-size: 40px;">Putin</p>'
st.markdown(p_title, unsafe_allow_html=True)

df_p = df_interim_p['UserName'].value_counts().reset_index()[:20]
fig_p = px.bar(df_p, x='index', y='UserName', text_auto=True)
fig_p.update_layout(xaxis_title="usuario", yaxis_title="frecuencia",font=dict(size=14))

# Plot!
st.plotly_chart(fig_p, use_container_width=True)

z_title = '<p style="font-family:Time New Roman; color:Black; font-size: 40px;">Zelensky</p>'
st.markdown(z_title, unsafe_allow_html=True)

df_z = df_interim_z['UserName'].value_counts().reset_index()[:20]
fig_z = px.bar(df_z, x='index', y='UserName', text_auto=True)
fig_z.update_layout(xaxis_title="usuario", yaxis_title="frecuencia",font=dict(size=14))

# Plot!
st.plotly_chart(fig_z, use_container_width=True)

bot_title = '<p style="font-family:Time New Roman; color:Black; font-size: 40px;">Twitter Bots 🤖 </p>'
st.markdown(bot_title, unsafe_allow_html=True)
st.markdown('')
st.write('##### Dentro de los usuarios que más publican se identificaron Bots utilizando la herramienta [Botometer](https://botometer.osome.iu.edu/)')
