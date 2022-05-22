from operator import index
from matplotlib.pyplot import title
import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd
from pymongo import MongoClient
import plotly.express as px
import plotly
import plotly.graph_objects as go
import os
import requests
from bs4 import BeautifulSoup

@st.cache
def load_data_df():
    """Load dataset in cache"""
    client = MongoClient('localhost',27017)
    db = client.tennis
    atp = db.atp.find()
    df = pd.DataFrame.from_records(atp,index="Unnamed: 0")
    df = df.drop(["_id"], axis=1)
    players = list(df['player_name'].drop_duplicates())
    surfaces = list(df['surface'].drop_duplicates())
    return df,players,surfaces

# DEF FOR SPACE
def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")

def get_image():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    f = open(os.getcwd() + '/images/temp.jpg','wb')
    f.write(requests.get('https://www.tennisabstract.com/photos/'+player_choice[0].lower().replace(' ','_')+'-sirobi.jpg',headers=headers).content)
    f.close()

def get_text():
    url = 'https://fr.wikipedia.org/wiki/'+player_choice[0].title().replace(' ','_')
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup.findAll('p')[3].text + soup.findAll('p')[4].text

# CONFIG PAGE
st.set_page_config(
    layout="wide", 
    page_icon="🎾", 
    page_title="ATP"
)

df,players,surfaces = load_data_df()

# SIDEBAR
image = st.sidebar.image(os.getcwd()+'/images/header.jpg')

st.sidebar.title("OPTIONS")
space(1)
player_choice = st.sidebar.multiselect('PLAYER', players, default=['Novak Djokovic','Roger Federer'])
space(1)
surface_choice = st.sidebar.multiselect('SURFACES', surfaces, default=surfaces)
space(1)
tourney_choice = st.sidebar.multiselect('TOURNEY', list(df['tourney_name'].drop_duplicates()), default=None)
space(1)
col1, col2 = st.sidebar.columns(2)
start_year = col1.selectbox('START YEAR', range(1968, 2023))
space(1)
values = range(start_year, 2023)
stop_year = col2.selectbox('STOP YEAR', values ,index=values.index(2022))
space(1)
algo = st.sidebar.selectbox('MACHINE LEARNING ALOGRITHM', ['Random Forest','SVC','Neural Network'])
space(1)


# PAGE
if player_choice != []:
    df = df[df['player_name'].isin(player_choice)]
else:
    pass

if surface_choice != []:
    df = df[df['surface'].isin(surface_choice)]
else:
    pass

if tourney_choice != []:
    df = df[df['tourney_name'].isin(tourney_choice)]
else:
    pass

if True:
    df = df[df['tourney_date']>= (str(start_year) + '-01-01') ]
    df = df[df['tourney_date']<= (str(stop_year)+ '-12-31')]


if len(player_choice) == 1:
    col1_desc, col2_img = st.columns(2)
    col1_desc.write(get_text())
    get_image()
    col2_img.image(os.getcwd()+'/images/temp.jpg')

rows = df.shape[0]

selected = str(rows) + ' Matche(s) selected'

st.title(selected)

liste= ['tourney_name','surface','draw_size','tourney_level','tourney_date','best_of','round','player_name','player_ioc','player_age','player_rank','player_rank_points','target']

gb = GridOptionsBuilder.from_dataframe(df[liste])
gb.configure_pagination()
gridOptions = gb.build()

AgGrid(df[liste],fit_columns_on_grid_load=True,gridOptions=gridOptions)

graph, graph1 = st.columns(2)

players_data_graph= df['player_name'].value_counts().to_frame()
names = df['player_name'].value_counts().index.tolist()

graph.subheader('Graph of players')

players_graph = px.pie(players_data_graph,values='player_name',names=names,color_discrete_sequence=px.colors.sequential.Darkmint)

players_graph.update_layout(
    margin=dict(l=1,r=1,b=1,t=1),
    font=dict(color='#383635', size=15)
)

players_graph.update_traces(textposition='inside', textinfo='percent+label')

graph.write(players_graph)

surface_data_graph= df['surface'].value_counts().to_frame()
surface_names = df['surface'].value_counts().index.tolist()

graph1.subheader('Graph of Surfaces')

mean_graph = px.bar(surface_data_graph,x=surface_names,y='surface',color_discrete_sequence=px.colors.sequential.Blugrn)

graph1.write(mean_graph)

# Classement en fonction de la date
# Taux gain / perte

# MAP 
world_data_graph= df['player_ioc'].value_counts().to_frame()
world_names = df['player_ioc'].value_counts().index.tolist()

# Resultat ML

st.write()

# MISE EN FORME
m = st.markdown("""
<style>
    div.stButton > button:first-child {
        width: 27em;
    }
    .css-1wdq7j4 {
        width: 28rem;
    }
</style>
""", unsafe_allow_html=True)
