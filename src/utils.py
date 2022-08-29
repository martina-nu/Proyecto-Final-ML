## libraries ##

import pandas as pd
pd.set_option('display.max_colwidth', None)
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
from collections import Counter
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer

## functions to be used are defined here ##

# plot the 20 users with most tweets
def plot_frequency_charts(df, feature, title, pallete):
    freq_df = pd.DataFrame()
    freq_df[feature] = df[feature]
    
    f, ax = plt.subplots(1,1, figsize=(20,8))
    total = float(len(df))
    g = sns.countplot(df[feature], order = df[feature].value_counts().index[:20], palette=pallete)
    g.set_title("Number and percentage of {}".format(title))

    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x()+p.get_width()/2.,
                height + 3,
                '{:1.2f}%'.format(100*height/total),
                ha="center") 

    plt.title('Frequency of {} tweets'.format(feature))
    plt.ylabel('Frequency', fontsize=12)
    plt.xlabel(title, fontsize=12)
    plt.xticks(rotation=90)
    plt.show()

# functions to remove symbols

def no_symbol(tweet):
    return re.sub("[^a-z0-9]"," ", tweet)

def repeated_words(tweet):
    return re.sub(r'\b(\w+)( \1\b)+', r'\1', tweet)

def remove_users(tweet):
    tweet = re.sub('(Replying to \s@[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet)  # remove response info
    tweet = re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet)  # remove tweeted at
    return tweet
    
def no_num(tweet):
    return re.sub('([0-9]+)', '', tweet)

def double_space(tweet):
    return re.sub('\s+', ' ', tweet)

def no_links(tweet):
    tweet = re.sub(r'\n', '', tweet)
    pattern = r"[^\s]*\.(com|org|net)\S*"
    tweet = re.sub(pattern, '', tweet)
    tweet = re.sub(r'https?:\/\/\S*', '', tweet, flags=re.MULTILINE)
    tweet = re.sub(r'http\S+', '', tweet)   # remove http links
    tweet = re.sub(r"www.\S+", "", tweet)
    tweet = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweet)
    tweet = re.sub(r'bit.ly/\S+', '', tweet)  # remove bitly links
    tweet = tweet.strip('[link]')   # remove [links]
    tweet = re.sub(r'pic.twitter\S+','', tweet)
    tweet = re.sub(r'[\S]+\.(net|com|org|info|edu|gov|uk|de|ca|jp|fr|au|us|ru|ch|it|nel|se|no|es|mil)[\S]*\s?','',tweet)
    return tweet

def remove_quoted(tweet):
    tweet = re.sub(r'Quote Tweet.*', '', tweet) 
    return tweet

# Dictionary of English Contractions
contractions_dict = { "ain't": "are not","'s":" is","aren't": "are not",
                     "can't": "cannot","can't've": "cannot have",
                     "'cause": "because","could've": "could have","couldn't": "could not",
                     "couldn't've": "could not have", "didn't": "did not","doesn't": "does not",
                     "don't": "do not","hadn't": "had not","hadn't've": "had not have",
                     "hasn't": "has not","haven't": "have not","he'd": "he would",
                     "he'd've": "he would have","he'll": "he will", "he'll've": "he will have",
                     "how'd": "how did","how'd'y": "how do you","how'll": "how will",
                     "I'd": "I would", "I'd've": "I would have","I'll": "I will",
                     "I'll've": "I will have","I'm": "I am","I've": "I have", "isn't": "is not",
                     "it'd": "it would","it'd've": "it would have","it'll": "it will",
                     "it'll've": "it will have", "let's": "let us","ma'am": "madam",
                     "mayn't": "may not","might've": "might have","mightn't": "might not", 
                     "mightn't've": "might not have","must've": "must have","mustn't": "must not",
                     "mustn't've": "must not have", "needn't": "need not",
                     "needn't've": "need not have","o'clock": "of the clock","oughtn't": "ought not",
                     "oughtn't've": "ought not have","shan't": "shall not","sha'n't": "shall not",
                     "shan't've": "shall not have","she'd": "she would","she'd've": "she would have",
                     "she'll": "she will", "she'll've": "she will have","should've": "should have",
                     "shouldn't": "should not", "shouldn't've": "should not have","so've": "so have",
                     "that'd": "that would","that'd've": "that would have", "there'd": "there would",
                     "there'd've": "there would have", "they'd": "they would",
                     "they'd've": "they would have","they'll": "they will",
                     "they'll've": "they will have", "they're": "they are","they've": "they have",
                     "to've": "to have","wasn't": "was not","we'd": "we would",
                     "we'd've": "we would have","we'll": "we will","we'll've": "we will have",
                     "we're": "we are","we've": "we have", "weren't": "were not","what'll": "what will",
                     "what'll've": "what will have","what're": "what are", "what've": "what have",
                     "when've": "when have","where'd": "where did", "where've": "where have",
                     "who'll": "who will","who'll've": "who will have","who've": "who have",
                     "why've": "why have","will've": "will have","won't": "will not",
                     "won't've": "will not have", "would've": "would have","wouldn't": "would not",
                     "wouldn't've": "would not have","y'all": "you all", "y'all'd": "you all would",
                     "y'all'd've": "you all would have","y'all're": "you all are",
                     "y'all've": "you all have", "you'd": "you would","you'd've": "you would have",
                     "you'll": "you will","you'll've": "you will have", "you're": "you are",
                     "you've": "you have"}

# Regular expression for finding contractions
contractions_re=re.compile('(%s)' % '|'.join(contractions_dict.keys()))

# Function for expanding contractions
def expand_contractions(text,contractions_dict=contractions_dict):
  def replace(match):
    return contractions_dict[match.group(0)]
  return contractions_re.sub(replace, text)

#Extract stopwords
def clean_stopwords(text: str,stop_dict: dict)->str:
    if text is not None:
        words = text.split()
        words_clean = []
        for word in words:
            if word not in stop_dict:
                words_clean.append(word)
        result = ' '.join(words_clean)
    else:
        result = None
    return result

lemmatizer = WordNetLemmatizer()
def lemmatize_words(text):
    words = text.split()
    words = [lemmatizer.lemmatize(word, pos='v') for word in words]
    return ' '.join(words)

# Take the raw dataframe and return the processed dataframe
def preprocess(df_raw):
    
    # Make a copy of df
    df = df_raw.copy()

    # Drop uninteresting columns
    df.drop(columns=['UserScreenName',"Text", "Emojis","Image link"], axis=1, inplace=True)

    # Convert to datetime
    #df['Timestamp'] = df['Timestamp'].apply(pd.Timestamp).apply(pd.Timestamp.date)
    #df['Timestamp'] = pd.to_datetime(df['Timestamp'], format="%Y-%m-%d")
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], format="%Y-%m-%dT%H:%M:%S.%f")
    df['Timestamp'] = df['Timestamp'].dt.date

    # Convert to numeric (some of the records contain commas and letters, so we must remove these characters to transform them to numbers)
    df['Comments'] = df['Comments'].str.replace(',', '').astype('int64')
    df['Likes'] = df['Likes'].str.replace(',', '').replace({"K":"*1e3", "M":"*1e6"}, regex=True).map(pd.eval).astype('int64')
    df['Retweets'] = df['Retweets'].str.replace(',', '').replace({"K":"*1e3", "M":"*1e6"}, regex=True).map(pd.eval).astype('int64')

    # Rename the column "Embedded_Text" to make it more clear
    df.rename(columns = {'Embedded_text':'Tweet'}, inplace = True)

    # Create column "Is_response" (some of the tweets start with "Replying to" because they are responses to other tweets)
    df['Is_response'] = df['Tweet'].apply(lambda x: 1 if x.startswith('Replying to') else 0)
    df['Is_response'] = pd.Categorical(df['Is_response'])

    # Create column "Quote_another" (some of the tweets contains "Quote Tweet")
    df['Quote_another'] = df['Tweet'].apply(lambda x: 1 if "Quote Tweet" in x else 0)
    df['Quote_another'] = pd.Categorical(df['Quote_another'])

    # Create new column
    df['Clean_Tweet'] = df["Tweet"]

    # Expanding Contractions
    df['Clean_Tweet']=df['Clean_Tweet'].apply(lambda x:expand_contractions(x))

    # Remove mentions and replying info
    df['Clean_Tweet']=df['Clean_Tweet'].apply(remove_users)

    # Remove white spaces
    df['Clean_Tweet'] = df['Clean_Tweet'].str.strip()

    # Remove double spaces
    df['Clean_Tweet']=df['Clean_Tweet'].apply(double_space)

    # Remove quoted tweets
    df['Clean_Tweet']=df['Clean_Tweet'].apply(remove_quoted)

    # Remove links
    df['Clean_Tweet']=df['Clean_Tweet'].apply(no_links)

    # To lower case
    df['Clean_Tweet'] = df['Clean_Tweet'].str.lower()

    # Remove repeated words
    df['Clean_Tweet']=df['Clean_Tweet'].apply(repeated_words)

    # Remove non-alphanumeric characters
    df['Clean_Tweet']=df['Clean_Tweet'].apply(no_symbol)

    # Remove repeated letters
    df['Clean_Tweet']=df['Clean_Tweet'].str.replace(r"([a-zA-Z])\1{2,}",r"\1",regex=True)

    # Remove numbers   
    df['Clean_Tweet']=df['Clean_Tweet'].apply(no_num)

    # Remove "gif alt" text
    df['Clean_Tweet']=df['Clean_Tweet'].str.replace('gif alt', '')

    # Remove stopwords
    stop_dict = stopwords.words('english')
    df['Clean_Tweet']=df['Clean_Tweet'].apply(lambda x: clean_stopwords(x, stop_dict = stop_dict))
    df['Clean_Tweet']=df['Clean_Tweet'].str.replace(r'''['!,.]''', '', regex = True)

    # Lemmatize words
    df['Clean_Tweet'] = df['Clean_Tweet'].apply(lemmatize_words)

    # Delete empty tweets
    df = df[df['Clean_Tweet'] != '']

    # Reorder columns
    df = df[['Timestamp', 'UserName', 'Comments', 'Likes', 'Retweets', 'Is_response', 'Quote_another', 'Tweet', 'Clean_Tweet']]

    return df
