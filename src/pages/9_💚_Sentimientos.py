import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn import metrics
from wordcloud import WordCloud

# seteamos layout="wide" para usar más espacio (por defecto es "center")
st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False) # para evitar warnings avisando que no se puede usar st.pyplot() sin argumentos

final_p = '/workspace/Proyecto-Final-ML/data/processed/Putin_tweets.csv'
final_z = '/workspace/Proyecto-Final-ML/data/processed/Zelensky_tweets.csv'
df_final_p = pd.read_csv(final_p)
df_final_z = pd.read_csv(final_z)

tit = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Análisis de sentimientos </b></p>'
st.markdown(tit, unsafe_allow_html=True)

st.markdown('')
st.markdown('* ##### Análisis no supervisado')
st.markdown('* ##### Modelos preentrenados de las siguientes librerías: VADER, Textblob y Flair')

# PUTIN

tit = '<p style="font-family:Time New Roman; color:Black; font-size: 40px;">Putin</p>'
st.markdown(tit, unsafe_allow_html=True)

# Flair negative
sent_vader_p_flairNeg = df_final_p['vader_Sentiment'].loc[df_final_p['flair_Sentiment'] == 'NEGATIVE']
sent_texblob_p_flairNeg = df_final_p['textblob_Sentiment'].loc[df_final_p['flair_Sentiment'] == 'NEGATIVE']

# Flair positive
sent_vader_p_flairPos = df_final_p['vader_Sentiment'].loc[df_final_p['flair_Sentiment'] == 'POSITIVE']
sent_texblob_p_flairPos = df_final_p['textblob_Sentiment'].loc[df_final_p['flair_Sentiment'] == 'POSITIVE']

fig, ax = plt.subplots(1, 2, figsize = (24, 24))

ConfusionMatrixDisplay.from_predictions(sent_vader_p_flairNeg, sent_texblob_p_flairNeg,  labels = ['Negative', 'Neutral', 'Positive'], colorbar = False, ax = ax[0])
ConfusionMatrixDisplay.from_predictions(sent_vader_p_flairPos, sent_texblob_p_flairPos,  labels = ['Negative', 'Neutral', 'Positive'], colorbar = False, ax = ax[1])
ax[0].set_title('Flair Negative', fontsize = 35)
ax[1].set_title('Flair Positive', fontsize = 35)

fig.show()
st.pyplot(fig)

# ZELENSKY

tit = '<p style="font-family:Time New Roman; color:Black; font-size: 40px;">Zelensky</p>'
st.markdown(tit, unsafe_allow_html=True)

# Flair negative
sent_vader_z_flairNeg = df_final_z['vader_Sentiment'].loc[df_final_z['flair_Sentiment'] == 'NEGATIVE']
sent_texblob_z_flairNeg = df_final_z['textblob_Sentiment'].loc[df_final_z['flair_Sentiment'] == 'NEGATIVE']

# Flair positive
sent_vader_z_flairPos = df_final_z['vader_Sentiment'].loc[df_final_z['flair_Sentiment'] == 'POSITIVE']
sent_texblob_z_flairPos = df_final_z['textblob_Sentiment'].loc[df_final_z['flair_Sentiment'] == 'POSITIVE']

fig, ax = plt.subplots(1, 2, figsize = (24, 24))

ConfusionMatrixDisplay.from_predictions(sent_vader_z_flairNeg, sent_texblob_z_flairNeg,  labels = ['Negative', 'Neutral', 'Positive'], colorbar = False, ax = ax[0])
ConfusionMatrixDisplay.from_predictions(sent_vader_z_flairPos, sent_texblob_z_flairPos,  labels = ['Negative', 'Neutral', 'Positive'], colorbar = False, ax = ax[1])
ax[0].set_title('Flair Negative', fontsize = 35)
ax[1].set_title('Flair Positive', fontsize = 35)

fig.show()
st.pyplot(fig)

# define common words to omit
common_words = ['vladimir', 'putin', 'volodymyr', 'zelensky', 'russia', 'russian', 'russians', 'ukraine', 'ukrainian', 'president', 'u'] 
# ajustar si queda bien la lematizacion
common_phrases = ['following', 'medium', 'include', 'potentially', 'sensitive', 'content', 'setting', 'view'] 

# WORDCLOUD PUTIN

tit = '<p style="font-family:Time New Roman; color:Black; font-size: 40px;">WordCloud según tipo de sentimiento - Putin</p>'
st.markdown(tit, unsafe_allow_html=True)

fig, ax = plt.subplots(1, 2, figsize = (24, 24))

# Wordcloud sentimientos negativos
putin_neg = df_final_p.Clean_Tweet[(df_final_p.flair_Sentiment == 'NEGATIVE') & (df_final_p.vader_Sentiment == 'Negative') & (df_final_p.textblob_Sentiment == 'Negative')]
wordcloud_p_neg = WordCloud(width=600, height=600, random_state = 123, stopwords=common_words+common_phrases, max_words=100).generate(' '.join(i for i in putin_neg))
ax[0].set_title('Sentimientos negativos', fontsize = 35)
ax[0].imshow(wordcloud_p_neg, interpolation = 'bilinear')
ax[0].axis("off")

# Wordcloud sentimientos positivos
putin_pos = df_final_p.Clean_Tweet[(df_final_p.flair_Sentiment == 'POSITIVE') & (df_final_p.vader_Sentiment == 'Positive') & (df_final_p.textblob_Sentiment == 'Positive')]
wordcloud_p_pos = WordCloud(width=600, height=600, random_state = 123, stopwords=common_words+common_phrases, max_words=100).generate(' '.join(i for i in putin_pos))
ax[1].set_title('Sentimientos positivos', fontsize = 35)
ax[1].imshow(wordcloud_p_pos, interpolation = 'bilinear')
ax[1].axis("off")

fig.show()
st.pyplot(fig)

# WORDCLOUD ZELENSKY

tit = '<p style="font-family:Time New Roman; color:Black; font-size: 40px;">WordCloud según tipo de sentimiento - Zelensky</p>'
st.markdown(tit, unsafe_allow_html=True)

fig, ax = plt.subplots(1, 2, figsize = (24, 24))

# Wordcloud sentimientos negativos
zelensky_neg = df_final_z.Clean_Tweet[(df_final_z.flair_Sentiment == 'NEGATIVE') & (df_final_z.vader_Sentiment == 'Negative') & (df_final_z.textblob_Sentiment == 'Negative')]
wordcloud_z_neg = WordCloud(width=600, height=600, random_state = 123, stopwords=common_words+common_phrases, max_words=100).generate(' '.join(i for i in zelensky_neg))
ax[0].set_title('Sentimientos negativos', fontsize = 35)
ax[0].imshow(wordcloud_z_neg, interpolation = 'bilinear')
ax[0].axis("off")

# Wordcloud sentimientos positivos
zelensky_pos = df_final_z.Clean_Tweet[(df_final_z.flair_Sentiment == 'POSITIVE') & (df_final_z.vader_Sentiment == 'Positive') & (df_final_z.textblob_Sentiment == 'Positive')]
wordcloud_z_pos = WordCloud(width=600, height=600, random_state = 123, stopwords=common_words+common_phrases, max_words=100).generate(' '.join(i for i in zelensky_pos))
ax[1].set_title('Sentimientos positivos', fontsize = 35)
ax[1].imshow(wordcloud_z_pos, interpolation = 'bilinear')
ax[1].axis("off")

fig.show()
st.pyplot(fig)
