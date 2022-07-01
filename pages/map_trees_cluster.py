
from dash import html , dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page


from components.maps.mapstrees import map_trees
from components.maps.mapstreescluster import map_trees_cluster
from components.sampledf.model_data import df_comunas,df_ibague

x=df_ibague["latitude"]
y=df_ibague["longitude"]

mapa_trees = map_trees('Mapa Arboles Ibague', 'div_map_trees',df_ibague)

mapa_trees_cluster = map_trees_cluster('Mapa Arboles Ibague', 'div_map_trees',df_ibague)

register_page(__name__, path="/maptreesCluster")

layout= html.Div(
    [
        dbc.Row([
            dbc.Col([
                html.Div([
                    mapa_trees_cluster.display()  
                ],id="row_map")   
            ])
        ], className= "mapcluster"),

    ], className='container-fluid', style={'margin': 'auto', 'width':'100%'}
)  
