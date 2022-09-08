import streamlit as st

# seteamos layout="wide" para usar más espacio (por defecto es "center")
st.set_page_config(layout="wide")

tit = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Conclusiones </b></p>'
st.markdown(tit, unsafe_allow_html=True)

st.markdown("")
st.markdown('* ##### similar cantidad de tweets en ambos datasets, ambos presentan crecimiento en el tiempo, con mayor aceleración para Zelensky')
st.markdown('* ##### gran cantidad de usuarios que tweetean, no hay mucha concentración de tweets por usuario, entre los 20 usuarios más frecuentes hay muchos que son considerados bots')
st.markdown('* ##### en un primer análisis de palabras se encuentran similitudes entre ambos, hay coincidencia de palabras con distinto peso relativo')
st.markdown('* ##### al analizar los tópicos, se identifican 3 grupos: uno relativo a opinión política internacional, otro asociado al impacto en la economía internacional y por último uno vinculado a cuestiones específicas de la guerra armamentística')
st.markdown('* ##### en el análisis de entidades se aprecia la presencia de personalidades norteamericanas e inglesas (posible influencia del idioma), alta relevancia de Putin en dataset de Zelensky')
st.markdown('* ##### respecto al análisis de sentimientos, hay una preponderancia de sentimientos negativos en el dataset de Putin y positivos en el de Zelensky')
st.markdown('* ##### las nubes de palabras refuerzan lo visto en análisis de tópicos: existen diferencias entre Putin y Zelensky, los sentimientos positivos asociados a Putin están vinculados a la libertad, la victoria, el enfrentamiento y referencias a Estados Unidos, mientras que para Zelensky los sentimientos positivos refieren más a su persona y liderazo, apoyo a la causa, solidarización.')
st.markdown('* ##### Respecto a los sentimientos negativos, se asocian en el caso de Putin al impacto de los precios en la economía y en el caso de Zelensky refieren a ataques, armas, impacto en personas.')


