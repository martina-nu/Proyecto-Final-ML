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

df_p = df_interim_p['UserName'].value_counts().reset_index()[:20]
fig = px.bar(df_p, x='index', y='UserName', text_auto=True)

# Plot!
st.plotly_chart(fig, use_container_width=True)


# FALTA ZELENSKY