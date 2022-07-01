#libraries
from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

# dash-labs plugin call, menu name and route
register_page(__name__, path="/storytelling")

from components.markdown.markformat import markformat
from components.maps.mapsample import mapsample

from components.maps.mapstreescluster import map_trees_cluster
from components.sampledf.model_data import df_comunas,df_ibague

mapa_trees_cluster = map_trees_cluster('Mapa Arboles Ibague', 'div_map_trees',df_ibague)


file1 = open('./data/mdsamples/story1.md')
file2 = open('./data/mdsamples/story2.md')
file3 = open('./data/mdsamples/story3.md')
file4 = open('./data/mdsamples/story4.md')

texto1  = markformat('', file2.read())
texto2  = markformat('', file3.read())
texto3  = markformat('', file4.read())

mapa_ejemplo_story = mapsample('Mapa elecciones', 'id_mapa_story1')


# specific layout for this page
layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                 html.H1(['¿Cómo están los árboles en Ibagué?'],id="div_title_maps"),
                 html.Hr()
            ], lg=12), 
           
        ]),

        dbc.Row([
            dbc.Col([
                 texto1.show()

            ], lg=4), 

            dbc.Col([
                html.H2("Mapa Cluster Arboles Ibagué"),
                 mapa_trees_cluster.display()

            ], lg=8), 
   
        ]),

        html.Hr(),

        dbc.Row([
            dbc.Col([
                 texto2.show()

            ], lg=4), 

            dbc.Col([
                 mapa_ejemplo_story.display()

            ], lg=8), 
   
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                 texto3.show()

            ], lg=4), 

            dbc.Col([
                 mapa_ejemplo_story.display()

            ], lg=8), 
   
        ]),
        
    ]
)