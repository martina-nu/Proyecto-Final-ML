import pandas as pd
import streamlit as st 

# seteamos layout="wide" para usar más espacio (por defecto es "center")
st.set_page_config(layout="wide")

original_title = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Preprocesamiento de los datos </b></p>'
st.markdown(original_title, unsafe_allow_html=True)

st.markdown("")
st.markdown('* ##### Se eliminan columnas irrelevantes ("UserScreenName", "Text", "Emojis" y "Image link")')
st.markdown('* ##### Se cambia tipo de datos ("Timestamp" a datetime64, "Comments", "Likes" y "Retweets" a int64)')
st.markdown('* ##### Se renombra "Embedded_text" ("Tweet")')
st.markdown('* ##### Se crean nuevas variables ("Is_Response" y "Quote_another")') 
st.markdown('* ##### Se crea columna "Clean_Tweet", que incluye las siguientes transformaciones sobre "Tweet":')
st.markdown('> ##### 1. Expansión de contracciones. 2. Conversión a minúsculas. 3. Supresión de: números, espacios en blanco y dobles, enlaces, palabras repetidas y letras repetidas en palabras, caracteres no alfanuméricos, menciones e información de respuesta, tweet original en teewts citados. 4. Lematización. 5. Se descartan tweets vacíos.')

Putin_title = '<p style="font-family:Time New Roman; color:Black; font-size: 40px;">Ejemplo</p>'
st.markdown(Putin_title, unsafe_allow_html=True)

df_interim_p = pd.read_csv('/workspace/Proyecto-Final-ML/data/interim/Putin_tweets.csv')

st.dataframe(df_interim_p[['Tweet', 'Clean_Tweet']].head(20))
