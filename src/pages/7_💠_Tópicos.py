## Topic Modeling ##
import pandas as pd
import pickle
import pyLDAvis
from streamlit import components

import streamlit as st

# seteamos layout="wide" para usar más espacio (por defecto es "center")
st.set_page_config(layout="wide")

tit = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Análisis de tópicos </b></p>'
st.markdown(tit, unsafe_allow_html=True)

p_tit = '<p style="font-family:Time New Roman; color:Black; font-size: 40px;">Tópicos asociados a Putin</p>'
st.markdown(p_tit, unsafe_allow_html=True)

# load model
with open('data/interim/vis_p.pkl' , 'rb') as f:
    vis_p = pickle.load(f)

html_string = pyLDAvis.prepared_data_to_html(vis_p)
components.v1.html(html_string, width=1300, height=800, scrolling=True)

z_tit = '<p style="font-family:Time New Roman; color:Black; font-size: 40px;">Tópicos asociados a Zelensky</p>'
st.markdown(z_tit, unsafe_allow_html=True)

# load model
with open('data/interim/vis_z.pkl' , 'rb') as f:
    vis_z = pickle.load(f)

html_string = pyLDAvis.prepared_data_to_html(vis_z)
components.v1.html(html_string, width=1300, height=800, scrolling=True)

