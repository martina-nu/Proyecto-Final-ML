import streamlit as st

# seteamos layout="wide" para usar más espacio (por defecto es "center")
st.set_page_config(layout="wide")

tit = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Referencias </b></p>'
st.markdown(tit, unsafe_allow_html=True)

st.markdown("")
st.markdown('* ##### **Datos:**')
st.markdown('> ###### https://www.kaggle.com/datasets/die9origephit/putin-and-zelensky-tweets')

st.markdown('* ##### **Preprocesamiento y EDA:**')
st.markdown('> ###### https://catriscode.com/2021/05/01/tweets-cleaning-with-python/')
st.markdown('> ###### https://neptune.ai/blog/exploratory-data-analysis-natural-language-processing-tools')
st.markdown('> ###### https://www.analyticsvidhya.com/blog/2020/04/beginners-guide-exploratory-data-analysis-text-data/')
st.markdown('> ###### https://catriscode.com/2021/05/01/tweets-cleaning-with-python/')
st.markdown('> ###### https://medium.com/analytics-vidhya/exploratory-data-analysis-on-covid-19-tweets-721f94bae087')

st.markdown('* ##### **Análisis de tópicos:**')
st.markdown('> ###### https://neptune.ai/blog/pyldavis-topic-modelling-exploration-tool-that-every-nlp-data-scientist-should-know')

st.markdown('* ##### **Análisis de sentimientos:**')
st.markdown('> ###### https://monkeylearn.com/sentiment-analysis/')
st.markdown('> ###### https://neptune.ai/blog/sentiment-analysis-python-textblob-vs-vader-vs-flair')
st.markdown('> ###### https://grabngoinfo.com/sentiment-analysis-without-modeling-textblob-vs-vader-vs-flair/')
st.markdown('> ###### https://towardsdatascience.com/sentiment-analysis-for-stock-price-prediction-in-python-bed40c65d178')
st.markdown('> ###### https://www.analyticsvidhya.com/blog/2021/06/twitter-sentiment-analysis-a-nlp-use-case-for-beginners/')

st.markdown('* ##### **Streamlit:**')
st.markdown('> ###### https://www.youtube.com/watch?v=cZSzK2uIqjY&t=661s')

st.markdown('* ##### **Código del proyecto:**')
st.markdown('> ###### https://github.com/martina-nu/Proyecto-Final-ML')
