
from dash import html , dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page
import folium
from components.maps.mapstreesheat import mapl

from components.maps.mapstrees import map_trees
from components.maps.mapstreescluster import map_trees_cluster
from components.sampledf.model_data import df_comunas,df_ibague

#register_page(__name__, path="/maptreesheat1")

#html_string = mapl()._repr_html_()

layout= html.Div(
    [
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Iframe(id='map', srcDoc=open('assets/html/heatmap.html','r').read(),width='100%',height='600')  
                ],id="row_map1")   
            ])
        ], className= "card"),

    ], className='container-fluid', style={'margin': 'auto', 'width':'100%'}
)  
