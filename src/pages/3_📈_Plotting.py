import streamlit as st
import pandas as pd
import numpy as np 
pd.set_option('display.max_colwidth', None)
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
nltk.download('stopwords')
import utils
# vader
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# textblob
from textblob import TextBlob
# flair
import flair
# functions to use (defined in utils.py)
import utils


proccesed_p = '/workspace/Proyecto-Final-ML/data/processed/Putin_tweets.csv'
proccesed_z = '/workspace/Proyecto-Final-ML/data/processed/Zelensky_tweets.csv'
df_final_p = pd.read_csv(proccesed_p)
df_final_z = pd.read_csv(proccesed_z)

# define common words to omit
common_words = ['vladimir', 'putin', 'volodymyr', 'zelensky', 'russia', 'russian', 'russians', 'ukraine', 'ukrainian', 'president', 'u'] 

# change flair sentiment categories
cat = {'flair_Sentiment': {'NEGATIVE': 'Negative', 'POSITIVE': 'Positive'}}
df_final_p = df_final_p.replace(cat)
df_final_z = df_final_z.replace(cat)


# Putin WordCloud (1 word) - vader

fig, ax = plt.subplots(figsize = (10, 10))

# Positive
wordcloud_pos = WordCloud(width=600, height=600, stopwords=common_words).generate(' '.join(i for i in df_final_p[df_final_p['vader_Sentiment'] == 'Positive'].Clean_Tweet))
plt.title('Vader positive sentiment', fontsize = 40)
plt.imshow(wordcloud_pos, interpolation = 'bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
plt.imshow(wordcloud_pos, interpolation='bilinear')
st.pyplot(fig)

# Negative
wordcloud_neg = WordCloud(width=600, height=600, stopwords=common_words).generate(' '.join(i for i in df_final_p[df_final_p['vader_Sentiment'] == 'Negative'].Clean_Tweet))
plt.title('Vader negative sentiment', fontsize = 40)
plt.imshow(wordcloud_neg, interpolation = 'bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
plt.imshow(wordcloud_neg, interpolation='bilinear')
st.pyplot(fig)