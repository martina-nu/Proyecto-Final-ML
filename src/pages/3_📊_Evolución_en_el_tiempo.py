import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
#import plotly.express as px
import plotly.graph_objects as go

# seteamos layout="wide" para usar más espacio (por defecto es "center")
st.set_page_config(layout="wide")

original_title = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Cantidad de tweets por mes según presidente </b></p>'
st.markdown(original_title, unsafe_allow_html=True)

interim_p = '/workspace/Proyecto-Final-ML/data/interim/Putin_tweets.csv'
interim_z = '/workspace/Proyecto-Final-ML/data/interim/Zelensky_tweets.csv'

df_interim_p = pd.read_csv(interim_p)
df_interim_z = pd.read_csv(interim_z)

df_p = df_interim_p.groupby(pd.to_datetime(df_interim_p['Timestamp']).dt.strftime('%b-%Y'), sort=False)['Clean_Tweet'].size().reset_index()
#df_p['President']= 'Putin'
df_z = df_interim_z.groupby(pd.to_datetime(df_interim_z['Timestamp']).dt.strftime('%b-%Y'), sort=False)['Clean_Tweet'].size().reset_index()
#df_z['President']= 'Zelensky'
#df = pd.concat([df_p, df_z], axis=0 )
#df.columns = ['Month', 'Count', 'President']

#fig = px.line(df, x='Month', y='Count', color='President', symbol="President")

fig = go.Figure()
fig.add_trace(go.Scatter(x=df_p.Timestamp, y=df_p.Clean_Tweet, mode='lines+markers', name='Putin'))
fig.add_trace(go.Scatter(x=df_z.Timestamp, y=df_z.Clean_Tweet, mode='lines+markers', name='Zelensky'))
fig.update_layout(
    xaxis_title="mes", yaxis_title="cantidad de tweets",legend_title="Presidente",
    font=dict(size=18))

# Plot!
st.plotly_chart(fig, use_container_width=True)
