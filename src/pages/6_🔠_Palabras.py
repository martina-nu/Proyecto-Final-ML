import streamlit as st
import pandas as pd 
import plotly.express as px 
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from sklearn.feature_extraction.text import CountVectorizer

# seteamos layout="wide" para usar más espacio (por defecto es "center")
st.set_page_config(layout="wide")


### --- LOAD DATAFRAME
interim_p = '/workspace/Proyecto-Final-ML/data/interim/Putin_tweets.csv'
interim_z = '/workspace/Proyecto-Final-ML/data/interim/Zelensky_tweets.csv'

df_interim_p = pd.read_csv(interim_p)
df_interim_z = pd.read_csv(interim_z)


def get_top_ngram(corpus, n=None):
    vec = CountVectorizer(ngram_range=(n, n)).fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:10]

df_p_bi= pd.DataFrame(get_top_ngram(df_interim_p['Clean_Tweet'], 2))
df_p_bi.columns=['Text', 'Freq']

df_z_bi= pd.DataFrame(get_top_ngram(df_interim_z['Clean_Tweet'], 2))
df_z_bi.columns=['Text', 'Freq']


df_z_tri= pd.DataFrame(get_top_ngram(df_interim_z['Clean_Tweet'],3))
df_z_tri.columns = ['Text', 'Freq']

df_p_tri= pd.DataFrame(get_top_ngram(df_interim_p['Clean_Tweet'],3))
df_p_tri.columns = ['Text', 'Freq']


fig = make_subplots(rows=1, cols=2, shared_xaxes=True)

fig.add_trace(go.Bar(x=df_p_bi['Text'], y=df_p_bi['Freq']),1,1)

fig.add_trace(go.Bar(x=df_z_bi['Text'], y=df_z_bi['Freq']),1, 2,)

fig.update_layout(coloraxis=dict(colorscale='Bluered_r'), showlegend=True)




st.plotly_chart(fig, use_container_width=True, showlegend= False)







