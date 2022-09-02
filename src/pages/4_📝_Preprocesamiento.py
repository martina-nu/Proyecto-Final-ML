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
st.markdown('> 1. ##### Expansión de contracciones.')
st.markdown('> 2. ##### Supresión de menciones e información de respuesta.')
st.markdown('> 3. ##### Supresión de espacios en blanco y espacios dobles.')
st.markdown('> 4. ##### Supresión de tweet original en teewts citados (sólo comentario).')
st.markdown('> 5. ##### Supresión de enlaces.')
st.markdown('> 6. ##### Texto a minúsculas.')
st.markdown('> 7. ##### Supresión de palabras repetidas.')
st.markdown('> 8. ##### Supresión de caracteres no alfanuméricos.')
st.markdown('> 9. ##### Supresión de letras repetidas en palabras.')
st.markdown('> 10. ##### Supresión de números.')
st.markdown('> 11. ##### Supresión de palabras vacías')
st.markdown('> 12. ##### Lematización')
st.markdown('> 13. ##### Se descartan tweets vacíos.')