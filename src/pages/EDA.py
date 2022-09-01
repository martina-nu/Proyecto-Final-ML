import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read the final dataframes
df_final_p= pd.read_csv('../data/processed/Putin_tweets.csv')
df_final_z= pd.read_csv('../data/processed/Zelensky_tweets.csv')

# convert variables in the right type

df_final_p['Timestamp'] = pd.to_datetime(df_final_p['Timestamp'], format="%Y-%m-%d")
df_final_p['UserName'] = pd.Categorical(df_final_p['UserName'])
df_final_p['Is_response'] = pd.Categorical(df_final_p['Is_response'])
df_final_p['Quote_another'] = pd.Categorical(df_final_p['Quote_another'])
df_final_p['Top_tweet'] = pd.Categorical(df_final_p['Top_tweet'])
df_final_p['vader_Sentiment'] = pd.Categorical(df_final_p['vader_Sentiment'])
df_final_p['textblob_Sentiment'] = pd.Categorical(df_final_p['textblob_Sentiment'])
df_final_p['flair_Sentiment'] = pd.Categorical(df_final_p['flair_Sentiment'])

df_final_z['Timestamp'] = pd.to_datetime(df_final_z['Timestamp'], format="%Y-%m-%d")
df_final_z['UserName'] = pd.Categorical(df_final_z['UserName'])
df_final_z['Is_response'] = pd.Categorical(df_final_z['Is_response'])
df_final_z['Quote_another'] = pd.Categorical(df_final_z['Quote_another'])
df_final_z['Top_tweet'] = pd.Categorical(df_final_z['Top_tweet'])
df_final_z['vader_Sentiment'] = pd.Categorical(df_final_z['vader_Sentiment'])
df_final_z['textblob_Sentiment'] = pd.Categorical(df_final_z['textblob_Sentiment'])
df_final_z['flair_Sentiment'] = pd.Categorical(df_final_z['flair_Sentiment'])

# change flair sentiment categories
cat = {'flair_Sentiment': {'NEGATIVE': 'Negative', 'POSITIVE': 'Positive'}}
df_final_p = df_final_p.replace(cat)
df_final_z = df_final_z.replace(cat)

# correlation matrix between numerical variables - Putin
fig, ax = plt.subplots()
sns.heatmap(df_final_p.corr(), ax=ax, vmin=0, vmax=1, linewidths=.5,cmap="YlGnBu")
st.write(fig)

# correlation matrix between numerical variables - Zelensky
fig1, ax = plt.subplots()
sns.heatmap(df_final_z.corr(), ax= ax, vmin=0, vmax=1, linewidths=.5, cmap="YlGnBu")
st.write(fig1)