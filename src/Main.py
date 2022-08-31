import streamlit as st

c1, c2 = st.columns([10, 7])
original_title = '<p style="font-family:Time New Roman; color:Black; font-size: 70px;">Proyecto Final</p>'
c1.markdown(original_title, unsafe_allow_html=True)

# Contenido de la primera columna
c2.image(['/workspace/Proyecto-Final-ML/src/images/UTEC.png', '/workspace/Proyecto-Final-ML/src/images/4geeks_image.png', '/workspace/Proyecto-Final-ML/src/images/BID.png'], width=60)
# Contenido de la segunda

st.markdown("# ANÁLISIS DE TWEETS UTILIZANDO TÉCNICAS DE NLP")
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown("## Presentación realizada por:")
nombre1 = '<p style="font-family:Calabria; color:Black; font-size: 35px;"> 👩‍💼 Romina Gonella</p>'
nombre2 = '<p style="font-family:Calabria; color:Black; font-size: 35px;"> 👩‍💼 Martina Nuñez</p>'
nombre3 = '<p style="font-family:Calabria; color:Black; font-size: 35px;"> 👨‍💼 Eduardo Coyto</p>'
st.markdown('')
st.markdown('')

st.markdown(nombre1, unsafe_allow_html=True)
st.markdown(nombre2, unsafe_allow_html=True)
st.markdown(nombre3, unsafe_allow_html=True)




