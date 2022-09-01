import streamlit as st 

original_title = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Preprocesamiento de los datos </b></p>'
st.markdown(original_title, unsafe_allow_html=True)

st.markdown("")
st.markdown('### * Eliminar columnas irrelevantes ("UserScreenName", "Text", "Emojis" y "Image link")')