import streamlit as st
import pickle
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# seteamos layout="wide" para usar más espacio (por defecto es "center")
st.set_page_config(layout="wide")

# ENTIDADES

# load object
with open('data/interim/count_p.pkl' , 'rb') as f:
    count_p = pickle.load(f)

# load object
with open('data/interim/count_z.pkl' , 'rb') as f:
    count_z = pickle.load(f)

x_p,y_p=map(list,zip(*count_p))
x_z,y_z=map(list,zip(*count_z))

tit = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Análisis de entidades </b></p>'
st.markdown(tit, unsafe_allow_html=True)

st.markdown('* ##### Librería spacy')
st.markdown('* ##### Para no sesgar el análisis se excluye la palabra “putin” y “zelensky” según corresponda.')

fig = make_subplots(rows=1, cols=2, shared_xaxes=True, shared_yaxes=True)
fig.add_trace(go.Bar(x=x_p, y=y_p, name='Putin'),1,1)
fig.add_trace(go.Bar(x=x_z, y=y_z, name='Zelensky'),1, 2)
fig.update_layout(coloraxis=dict(colorscale='Bluered_r'), showlegend=True, font=dict(size=13))

st.plotly_chart(fig, use_container_width=True, showlegend= False)

st.markdown('')
st.markdown('* ##### Las principales entidades identificadas son:')
st.markdown('###### **GPE:** Países, ciudades o estados')
st.markdown('###### **NORP:** Nacionalidades, grupos religiosos y políticos')
st.markdown('###### **PERSON:** Personas (incluidas ficticias)')
st.markdown('###### **ORG:** Compañías, agencias, instituciones')
st.markdown('')
st.markdown('')

tit = '<p style="font-family:Arial; color:Black; font-size: 55px;"> <b> Top 10 entidades por categoría </b></p>'
st.markdown(tit, unsafe_allow_html=True)

# ENTIDAD GPE

tit_2 = '<p style="font-family:Arial; color:Black; font-size: 40px;">Países, ciudades o estados </p>'
st.markdown(tit_2, unsafe_allow_html=True)

# load object
with open('data/interim/count_gpe_p.pkl' , 'rb') as f:
    count_gpe_p = pickle.load(f)

# load object
with open('data/interim/count_gpe_z.pkl' , 'rb') as f:
    count_gpe_z = pickle.load(f)

x_p,y_p=map(list,zip(*count_gpe_p))
x_z,y_z=map(list,zip(*count_gpe_z))

fig = make_subplots(rows=1, cols=2, shared_xaxes=True, shared_yaxes=True)
fig.add_trace(go.Bar(x=x_p, y=y_p, name='Putin'),1,1)
fig.add_trace(go.Bar(x=x_z, y=y_z, name='Zelensky'),1, 2)
fig.update_layout(coloraxis=dict(colorscale='Bluered_r'), showlegend=True)

st.plotly_chart(fig, use_container_width=True, showlegend= False)

# ENTIDAD NORP

tit_3 = '<p style="font-family:Arial; color:Black; font-size: 40px;">Nacionalidades, grupos religiosos y políticos </p>'
st.markdown(tit_3, unsafe_allow_html=True)

# load object
with open('data/interim/count_norp_p.pkl' , 'rb') as f:
    count_norp_p = pickle.load(f)

# load object
with open('data/interim/count_norp_z.pkl' , 'rb') as f:
    count_norp_z = pickle.load(f)

x_p,y_p=map(list,zip(*count_norp_p))
x_z,y_z=map(list,zip(*count_norp_z))

fig = make_subplots(rows=1, cols=2, shared_xaxes=True, shared_yaxes=True)
fig.add_trace(go.Bar(x=x_p, y=y_p, name='Putin'),1,1)
fig.add_trace(go.Bar(x=x_z, y=y_z, name='Zelensky'),1, 2)
fig.update_layout(coloraxis=dict(colorscale='Bluered_r'), showlegend=True)

st.plotly_chart(fig, use_container_width=True, showlegend= False)

# ENTIDAD PERSON

tit_1 = '<p style="font-family:Arial; color:Black; font-size: 40px;">Personas </p>'
st.markdown(tit_1, unsafe_allow_html=True)

# load object
with open('data/interim/count_person_p.pkl' , 'rb') as f:
    count_person_p = pickle.load(f)

# load object
with open('data/interim/count_person_z.pkl' , 'rb') as f:
    count_person_z = pickle.load(f)

x_p,y_p=map(list,zip(*count_person_p))
x_z,y_z=map(list,zip(*count_person_z))

fig = make_subplots(rows=1, cols=2, shared_xaxes=True, shared_yaxes=True)
fig.add_trace(go.Bar(x=x_p, y=y_p, name='Putin'),1,1)
fig.add_trace(go.Bar(x=x_z, y=y_z, name='Zelensky'),1, 2)
fig.update_layout(coloraxis=dict(colorscale='Bluered_r'), showlegend=True)

st.plotly_chart(fig, use_container_width=True, showlegend= False)

# ENTIDAD ORG

tit_1 = '<p style="font-family:Arial; color:Black; font-size: 40px;">Compañías, agencias, instituciones </p>'
st.markdown(tit_1, unsafe_allow_html=True)

# load object
with open('data/interim/count_org_p.pkl' , 'rb') as f:
    count_org_p = pickle.load(f)

# load object
with open('data/interim/count_org_z.pkl' , 'rb') as f:
    count_org_z = pickle.load(f)

x_p,y_p=map(list,zip(*count_org_p))
x_z,y_z=map(list,zip(*count_org_z))

fig = make_subplots(rows=1, cols=2, shared_xaxes=True, shared_yaxes=True)
fig.add_trace(go.Bar(x=x_p, y=y_p, name='Putin'),1,1)
fig.add_trace(go.Bar(x=x_z, y=y_z, name='Zelensky'),1, 2)
fig.update_layout(coloraxis=dict(colorscale='Bluered_r'), showlegend=True)

st.plotly_chart(fig, use_container_width=True, showlegend= False)
