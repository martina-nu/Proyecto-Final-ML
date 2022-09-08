import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px 
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud

# seteamos layout="wide" para usar más espacio (por defecto es "center")
st.set_page_config(layout="wide")

tit = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Análisis de palabras</b></p>'
st.markdown(tit, unsafe_allow_html=True)

### --- LOAD DATAFRAME
interim_p = 'data/interim/Putin_tweets.csv'
interim_z = 'data/interim/Zelensky_tweets.csv'

df_interim_p = pd.read_csv(interim_p)
df_interim_z = pd.read_csv(interim_z)

# define common words to omit
common_words = ['vladimir', 'putin', 'volodymyr', 'zelensky', 'russia', 'russian', 'russians', 'ukraine', 'ukrainian', 'president', 'u'] 
# ajustar si queda bien la lematizacion
common_phrases = ['following', 'medium', 'include', 'potentially', 'sensitive', 'content', 'setting', 'view'] 

oneWord_title = '<p style="font-family:Arial; color:Black; font-size: 40px;">Nube de 100 palabras más frecuentes</p>'
st.markdown(oneWord_title, unsafe_allow_html=True)

fig, ax = plt.subplots(1, 2, figsize = (24, 24))

# Putin 
wordcloud_p = WordCloud(width=600, height=600, random_state = 123, stopwords=common_words+common_phrases, max_words=100).generate(' '.join(i for i in df_interim_p.Clean_Tweet))
ax[0].set_title('Putin',fontsize = 40,  pad=30)
ax[0].imshow(wordcloud_p, interpolation = 'bilinear')
ax[0].axis("off")

# Zelensky
wordcloud_z = WordCloud(width=600, height=600, random_state = 123, stopwords=common_words+common_phrases, max_words=100).generate(' '.join(i for i in df_interim_z.Clean_Tweet))
ax[1].set_title('Zelensky', fontsize = 40,  pad=30)
ax[1].imshow(wordcloud_z, interpolation = 'bilinear')
ax[1].axis("off")

fig.show()
st.pyplot(fig)

def get_top_ngram(corpus, n=None, stop_words=None):
    vec = CountVectorizer(ngram_range=(n, n), stop_words=stop_words).fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:10]

#### BIGRAM

df_p_bi= pd.DataFrame(get_top_ngram(df_interim_p['Clean_Tweet'], 2, common_words + common_phrases))
df_p_bi.columns=['Text', 'Freq']

df_z_bi= pd.DataFrame(get_top_ngram(df_interim_z['Clean_Tweet'], 2, common_words + common_phrases))
df_z_bi.columns=['Text', 'Freq']

bigram_title = '<p style="font-family:Arial; color:Black; font-size: 40px;">Bigramas </p>'
st.markdown(bigram_title, unsafe_allow_html=True)

fig = make_subplots(rows=1, cols=2, shared_xaxes=True)

fig.add_trace(go.Bar(x=df_p_bi['Text'], y=df_p_bi['Freq'], name='Putin'),1,1)

fig.add_trace(go.Bar(x=df_z_bi['Text'], y=df_z_bi['Freq'], name='Zelensky'),1, 2)

fig.update_layout(coloraxis=dict(colorscale='Bluered_r'), showlegend=True)

st.plotly_chart(fig, use_container_width=True, showlegend= False)

#### TRIGRAM

df_z_tri= pd.DataFrame(get_top_ngram(df_interim_z['Clean_Tweet'],3, common_words + common_phrases))
df_z_tri.columns = ['Text', 'Freq']

df_p_tri= pd.DataFrame(get_top_ngram(df_interim_p['Clean_Tweet'],3, common_words + common_phrases))
df_p_tri.columns = ['Text', 'Freq']

trigram_title = '<p style="font-family:Arial; color:Black; font-size: 40px;">Trigramas </p>'
st.markdown(trigram_title, unsafe_allow_html=True)

fig = make_subplots(rows=1, cols=2, shared_xaxes=True)

fig.add_trace(go.Bar(x=df_p_tri['Text'], y=df_p_tri['Freq'], name='Putin'),1,1)

fig.add_trace(go.Bar(x=df_z_tri['Text'], y=df_z_tri['Freq'], name='Zelensky'),1, 2)

fig.update_layout(coloraxis=dict(colorscale='Bluered_r'), showlegend=True)

st.plotly_chart(fig, use_container_width=True, showlegend= False)








