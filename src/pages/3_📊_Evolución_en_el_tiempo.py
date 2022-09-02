import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt

# seteamos layout="wide" para usar más espacio (por defecto es "center")
st.set_page_config(layout="wide")

interim_p = '/workspace/Proyecto-Final-ML/data/interim/Putin_tweets.csv'
interim_z = '/workspace/Proyecto-Final-ML/data/interim/Zelensky_tweets.csv'

df_interim_p = pd.read_csv(interim_p)
df_interim_z = pd.read_csv(interim_z)


# Plot number of tweets mentioning each president by month
plt.figure(figsize=(18,6))
df_interim_p.groupby(pd.to_datetime(df_interim_p['Timestamp']).dt.strftime('%b-%Y'), sort=False)['Clean_Tweet'].size().plot(label= 'Putin', marker = 's')
df_interim_z.groupby(pd.to_datetime(df_interim_z['Timestamp']).dt.strftime('%b-%Y'), sort=False)['Clean_Tweet'].size().plot(label= 'Zelensky', marker = 's')
st.plotly_chart