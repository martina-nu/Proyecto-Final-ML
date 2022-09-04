## Topic Modeling ##
import pandas as pd
import pickle
import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import *
from nltk.tokenize import word_tokenize
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis
import gensim
import gensim.corpora as corpora
from gensim.corpora import Dictionary
from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel

import streamlit as st

# seteamos layout="wide" para usar más espacio (por defecto es "center")
st.set_page_config(layout="wide")

pyLDAvis.enable_notebook()

# load model
with open('data/interim/vis_p.pkl' , 'rb') as f:
    vis_p = pickle.load(f)
vis_p
st.pyplot(vis_p)

### NO FUNCIONA EL GRÁFICO CON STREAMLIT