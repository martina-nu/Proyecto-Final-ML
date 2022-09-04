import streamlit as st

# seteamos layout="wide" para usar más espacio (por defecto es "center")
st.set_page_config(layout="wide")


# oportunidades de mejora y agradecimientos

tit = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Oportunidades de mejora </b></p>'
st.markdown(tit, unsafe_allow_html=True)

st.markdown("* #### Profundizar análisis por usuarios")
st.markdown("* #### Incorporar ubicación geográfica de los tweets")
st.markdown("* #### Entrenar modelos no supervisados")
st.markdown("* #### Obtener datos más recientes")

st.markdown("")

tit = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Agradecimientos </b></p>'
st.markdown(tit, unsafe_allow_html=True)

st.markdown("* #### Profesores y todo el equipo de 4Geeks")
st.markdown("* #### UTEC")
st.markdown("* #### BID")
st.markdown("* #### Compañeras/os del Bootcamp")
