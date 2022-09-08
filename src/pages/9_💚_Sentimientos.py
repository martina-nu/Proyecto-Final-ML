import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn import metrics
from wordcloud import WordCloud
import seaborn as sns

# seteamos layout="wide" para usar más espacio (por defecto es "center")
st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False) # para evitar warnings avisando que no se puede usar st.pyplot() sin argumentos

final_p = 'data/processed/Putin_tweets.csv'
final_z = 'data/processed/Zelensky_tweets.csv'
df_final_p = pd.read_csv(final_p)
df_final_z = pd.read_csv(final_z)

tit = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Análisis de sentimientos </b></p>'
st.markdown(tit, unsafe_allow_html=True)

st.markdown('')
st.markdown('* ##### Análisis no supervisado')
st.markdown('* ##### Modelos preentrenados de las siguientes librerías: VADER, Textblob y Flair')

# PUTIN

tit = '<p style="font-family:Arial; color:Black; font-size: 40px;">Putin</p>'
st.markdown(tit, unsafe_allow_html=True)

# Flair negative
sent_vader_p_flairNeg = df_final_p['vader_Sentiment'].loc[df_final_p['flair_Sentiment'] == 'NEGATIVE']
sent_texblob_p_flairNeg = df_final_p['textblob_Sentiment'].loc[df_final_p['flair_Sentiment'] == 'NEGATIVE']

# Flair positive
sent_vader_p_flairPos = df_final_p['vader_Sentiment'].loc[df_final_p['flair_Sentiment'] == 'POSITIVE']
sent_texblob_p_flairPos = df_final_p['textblob_Sentiment'].loc[df_final_p['flair_Sentiment'] == 'POSITIVE']

x_axis_labels = ['Negative', 'Neutral', 'Positive'] # labels for x-axis
y_axis_labels = ['Negative', 'Neutral', 'Positive'] # labels for y-axis

sns.set(font_scale=5)


#PLOT PUTIN

fig, ax = plt.subplots(1, 2, figsize = (48, 24))


cf_matrix1 = confusion_matrix(sent_vader_p_flairNeg, sent_texblob_p_flairNeg)
sns.heatmap(cf_matrix1, cbar=False, annot=True, fmt='g', xticklabels=x_axis_labels, yticklabels=y_axis_labels, cmap="Blues",ax=ax[0])


cf_matrix2 = confusion_matrix(sent_vader_p_flairPos, sent_texblob_p_flairPos)
sns.heatmap(cf_matrix2,cbar=False, annot=True, fmt='g', xticklabels=x_axis_labels, yticklabels=y_axis_labels, cmap="Blues", ax=ax[1])


ax[0].set_ylabel("VADER", fontsize = 60, labelpad=50)
ax[0].set_xlabel("TextBlob", fontsize = 60, labelpad=50)

ax[1].set_ylabel("VADER", fontsize = 60, labelpad=50)
ax[1].set_xlabel("TextBlob", fontsize = 60, labelpad=50)

ax[0].set_title('Flair Negative', fontsize = 80, pad=50)
ax[1].set_title('Flair Positive', fontsize = 80, pad=50)

fig.show()
st.pyplot(fig)

# ZELENSKY

tit = '<p style="font-family:Arial;color:Black; font-size: 40px;">Zelensky</p>'
st.markdown(tit, unsafe_allow_html=True)

# Flair negative
sent_vader_z_flairNeg = df_final_z['vader_Sentiment'].loc[df_final_z['flair_Sentiment'] == 'NEGATIVE']
sent_texblob_z_flairNeg = df_final_z['textblob_Sentiment'].loc[df_final_z['flair_Sentiment'] == 'NEGATIVE']

# Flair positive
sent_vader_z_flairPos = df_final_z['vader_Sentiment'].loc[df_final_z['flair_Sentiment'] == 'POSITIVE']
sent_texblob_z_flairPos = df_final_z['textblob_Sentiment'].loc[df_final_z['flair_Sentiment'] == 'POSITIVE']

fig, ax = plt.subplots(1, 2, figsize = (48, 24))

cf_matrix3 = confusion_matrix(sent_vader_z_flairNeg, sent_texblob_z_flairNeg)
sns.heatmap(cf_matrix3, cbar=False, annot=True, fmt='g', xticklabels=x_axis_labels, yticklabels=y_axis_labels, cmap="Blues",ax=ax[0])


cf_matrix4 = confusion_matrix(sent_vader_z_flairPos, sent_texblob_z_flairPos)
sns.heatmap(cf_matrix4,cbar=False, annot=True, fmt='g', xticklabels=x_axis_labels, yticklabels=y_axis_labels, cmap="Blues", ax=ax[1])

ax[0].set_ylabel("VADER", fontsize = 60, labelpad=50)
ax[0].set_xlabel("TextBlob", fontsize = 60, labelpad=50)

ax[1].set_ylabel("VADER", fontsize = 60, labelpad=50)
ax[1].set_xlabel("TextBlob", fontsize = 60, labelpad=50)

ax[0].set_title('Flair Negative', fontsize = 80, pad=50)
ax[1].set_title('Flair Positive', fontsize = 80, pad=50)

fig.show()
st.pyplot(fig)

tit = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Nube de palabras según tipo de sentimientos </b></p>'
st.markdown(tit, unsafe_allow_html=True)

# define common words to omit
common_words = ['vladimir', 'putin', 'volodymyr', 'zelensky', 'russia', 'russian', 'russians', 'ukraine', 'ukrainian', 'president', 'u'] 
# ajustar si queda bien la lematizacion
common_phrases = ['following', 'medium', 'include', 'potentially', 'sensitive', 'content', 'setting', 'view'] 

# WORDCLOUD PUTIN

tit = '<p style="font-family:Arial; color:Black; font-size: 40px;">Putin</p>'
st.markdown(tit, unsafe_allow_html=True)

fig, ax = plt.subplots(1, 2, figsize = (24, 24))

# Wordcloud sentimientos negativos
putin_neg = df_final_p.Clean_Tweet[(df_final_p.flair_Sentiment == 'NEGATIVE') & (df_final_p.vader_Sentiment == 'Negative') & (df_final_p.textblob_Sentiment == 'Negative')]
wordcloud_p_neg = WordCloud(collocation_threshold = 2, min_word_length =3,width=600, height=600, random_state = 12, stopwords=common_words+common_phrases, max_words=100).generate(' '.join(i for i in putin_neg))
ax[0].set_title('Sentimientos negativos', fontsize = 40,  pad=30)
ax[0].imshow(wordcloud_p_neg, interpolation = 'bilinear')
ax[0].axis("off")

# Wordcloud sentimientos positivos
putin_pos = df_final_p.Clean_Tweet[(df_final_p.flair_Sentiment == 'POSITIVE') & (df_final_p.vader_Sentiment == 'Positive') & (df_final_p.textblob_Sentiment == 'Positive')]
wordcloud_p_pos = WordCloud(collocation_threshold = 2, min_word_length =3,width=600, height=600, random_state = 12, stopwords=common_words+common_phrases, max_words=100).generate(' '.join(i for i in putin_pos))
ax[1].set_title('Sentimientos positivos', fontsize = 40,  pad=30)
ax[1].imshow(wordcloud_p_pos, interpolation = 'bilinear')
ax[1].axis("off")

fig.show()
st.pyplot(fig)

# WORDCLOUD ZELENSKY

tit = '<p style="font-family:Arial; color:Black; font-size: 40px;">Zelensky</p>'
st.markdown(tit, unsafe_allow_html=True)

fig, ax = plt.subplots(1, 2, figsize = (24, 24))

# Wordcloud sentimientos negativos
zelensky_neg = df_final_z.Clean_Tweet[(df_final_z.flair_Sentiment == 'NEGATIVE') & (df_final_z.vader_Sentiment == 'Negative') & (df_final_z.textblob_Sentiment == 'Negative')]
wordcloud_z_neg = WordCloud( collocation_threshold = 2, min_word_length =3, width=600, height=600, random_state = 123, stopwords=common_words+common_phrases, max_words=100).generate(' '.join(i for i in zelensky_neg))
ax[0].set_title('Sentimientos negativos', fontsize = 40,  pad=30)
ax[0].imshow(wordcloud_z_neg, interpolation = 'bilinear')
ax[0].axis("off")

# Wordcloud sentimientos positivos
zelensky_pos = df_final_z.Clean_Tweet[(df_final_z.flair_Sentiment == 'POSITIVE') & (df_final_z.vader_Sentiment == 'Positive') & (df_final_z.textblob_Sentiment == 'Positive')]
wordcloud_z_pos = WordCloud( collocation_threshold = 2, min_word_length =3, width=600, height=600, random_state = 123, stopwords=common_words+common_phrases, max_words=100).generate(' '.join(i for i in zelensky_pos))
ax[1].set_title('Sentimientos positivos', fontsize = 40,  pad=30)
ax[1].imshow(wordcloud_z_pos, interpolation = 'bilinear')
ax[1].axis("off")

fig.show()
st.pyplot(fig)
