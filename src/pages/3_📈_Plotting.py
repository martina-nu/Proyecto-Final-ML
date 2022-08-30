import streamlit as st
import pandas as pd
pd.set_option('display.max_colwidth', None)
import matplotlib.pyplot as plt
import seaborn as sns
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from wordcloud import WordCloud
from collections import Counter
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer
# vader
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download("vader_lexicon")
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

fig, ax = plt.subplots(1, 2, figsize = (24, 24))

# Positive
wordcloud_pos = WordCloud(width=600, height=600, stopwords=common_words).generate(' '.join(i for i in df_final_p[df_final_p['vader_Sentiment'] == 'Positive'].Clean_Tweet))
ax[0].set_title('Vader positive sentiment', fontsize = 'xx-large')
ax[0].imshow(wordcloud_pos, interpolation = 'bilinear')
ax[0].axis("off")

# Positive
wordcloud_neg = WordCloud(width=600, height=600, stopwords=common_words).generate(' '.join(i for i in df_final_p[df_final_p['vader_Sentiment'] == 'Negative'].Clean_Tweet))
ax[1].set_title('Vader negative sentiment', fontsize = 'xx-large')
ax[1].imshow(wordcloud_neg, interpolation = 'bilinear')
ax[1].axis("off")

fig.show()