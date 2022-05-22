from matplotlib.pyplot import title
import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd
from pymongo import MongoClient
import plotly.express as px
import plotly.graph_objects as go
import os
import requests


@st.cache
def load_data_df():
    """Load dataset in cache"""
    client = MongoClient('localhost',27017)
    db = client.crunchyroll
    animes = db.anime.find()
    df = pd.DataFrame.from_records(animes,index="Unnamed: 0")
    df = df.drop(["_id"], axis=1)
    editor = list(df['editor'].drop_duplicates())
    anime_type = [
        'action',
        'adventure',
        'comedy',
        'drama',
        'fantasy',
        'harem',
        'historical',
        'idols',
        'isekai',
        'magical_girls',
        'mecha',
        'music',
        'mystery',
        'post_apocalyptic',
        'romance',
        'sci_fi',
        'seinen',
        'shojo',
        'shonen',
        'slice_of_life',
        'sports',
        'supernatural',
        'thriller'
    ]
    return df,editor,anime_type

# DEF FOR SPACE
def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")

# CONFIG PAGE
st.set_page_config(
    layout="wide", 
    page_icon="🎾", 
    page_title="ATP"
)

df,editor,anime_type = load_data_df()

# SIDEBAR
image = st.sidebar.image(os.getcwd()+'/images/header.jpg')

st.sidebar.title("OPTIONS")
space(1)
title_request = st.sidebar.text_input('TITLE')
space(1)
editor_choice = st.sidebar.multiselect('PLAYER', editor, default=None)
space(1)
col1, col2 = st.sidebar.columns(2)
start_year = col1.selectbox('START YEAR', range(1968, 2022))
space(1)
stop_year = col2.selectbox('STOP YEAR', range(start_year, 2022))
space(1)

# PAGE
if title_request != '':
    df = df[df['title'].str.lower().str.contains(title_request.lower())]
else:
    pass

if editor_choice != []:
    df = df[df['editor'].isin(editor_choice)]
else:
    pass

rows = df.shape[0]

selected = str(rows) + ' anime(s) selected'

st.title(selected)

gb = GridOptionsBuilder.from_dataframe(df[['title','editor','short_desc','nb_videos']])
gb.configure_pagination()
gridOptions = gb.build()

AgGrid(df[['title','editor','short_desc','nb_videos']],fit_columns_on_grid_load=True,gridOptions=gridOptions)

graph, graph1 = st.columns(2)

editors_data_graph= df['editor'].value_counts().to_frame()
names = df['editor'].value_counts().index.tolist()

graph.subheader('Graph of editors')

editors_graph = px.pie(editors_data_graph,values='editor',names=names,color_discrete_sequence=px.colors.sequential.Oranges)

editors_graph.update_layout(
    showlegend=True,
    margin=dict(l=1,r=1,b=1,t=1),
    font=dict(color='#383635', size=15)
)

editors_graph.update_traces(textposition='inside', textinfo='percent+label')

graph.write(editors_graph)

mean_data_graph= df['mean_stars'].value_counts().to_frame()
names = df['mean_stars'].value_counts().index.tolist()

graph1.subheader('Graph of mean stars')

mean_graph = px.bar(mean_data_graph,x=names,y='mean_stars',color_discrete_sequence=px.colors.sequential.Peach)

graph1.write(mean_graph)

# MISE EN FORME
m = st.markdown("""
<style>
    div.stButton > button:first-child {
        width: 27em;
    }

    .css-1wdq7j4 {
        background-attachment: fixed;
        flex-shrink: 0;
        height: 100vh;
        overflow: auto;
        padding: 6rem 1rem;
        position: relative;
        transition: margin-left 300ms ease 0s, box-shadow 300ms ease 0s;
        width: 35rem;
        z-index: 100;
        margin-left: 0px;
    }
</style>
""", unsafe_allow_html=True)
