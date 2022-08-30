import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Tweet of Putin and Zelensky')

### --- LOAD DATAFRAME
proccesed_p = '/workspace/Proyecto-Final-ML/data/processed/Putin_tweets.csv'
proccesed_z = '/workspace/Proyecto-Final-ML/data/processed/Zelensky_tweets.csv'
sheet_name_p = 'Tweet Putin'
sheet_name_z = 'Tweet Zelensky'

df_final_p = pd.read_csv(proccesed_p)
df_final_z = pd.read_csv(proccesed_z)
Zelensky_title = '<p style="font-family:Time New Roman; color:Black; font-size: 40px;">Tweet of Zelensky</p>'
st.markdown(Zelensky_title, unsafe_allow_html=True)
st.dataframe(df_final_z[['Timestamp', 'UserName', 'Tweet', 'Clean_Tweet']])

Putin_title = '<p style="font-family:Time New Roman; color:Black; font-size: 40px;">Tweet of Putin</p>'
st.markdown(Putin_title, unsafe_allow_html=True)
st.dataframe(df_final_p[['Timestamp', 'UserName', 'Tweet', 'Clean_Tweet']])

