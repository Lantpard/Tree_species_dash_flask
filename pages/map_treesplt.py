
from turtle import bgcolor
from dash import html , dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page
import dash_leaflet as dl
import plotly.express as px
from components.maps.mapstrees import map_trees
from components.sampledf.model_data import df_comunas,df_ibague


mapa_trees = map_trees('Mapa Arboles Ibague', 'div_map_trees', df_ibague, df_comunas)


register_page(__name__, path="/maptrees5")

import pandas as pd

mapbox_token = 'pk.eyJ1IjoiY3J5cHRvcG90bHVjayIsImEiOiJjazhtbTN6aHEwa3lwM25taW5qNTdicHAwIn0.xFsCTDqPE_0L-OHwv21qTg'

import plotly.offline as py     #(version 4.4.1)
import plotly.graph_objs as go

df = df_ibague
df['color']=df.apply(lambda x: 'red' if x["estado_sanitario"]=="Muerto" else ('orange' if x["estado_sanitario"]=="Critico" else ('yellow' if x["estado_sanitario"]=="Enfermo" else ('green'))), axis=1)

blackbold={'color':'black', 'font-weight': 'bold'}

layout = dbc.Container([
#---------------------------------------------------------------
# Map_legen + Borough_checklist + Recycling_type_checklist + Web_link + Map
  
        dbc.Row([
            dbc.Col([
                 html.H1(['¿Cual es el estado de los árboles en Ibagué?'],id="div_title_maps"),
                 html.Hr()
            ], lg=12)

            ])

            ,
        dbc.Row([
            dbc.Col([

                html.Div([

            html.H3("Filtros"),

# Recycling_type_checklist
            html.H3('Seleccione Estado Sanitario: '),
            dcc.Dropdown(id='status_type',
                    options=[{'label':str(b),'value':b} for b in sorted(df['estado_sanitario'].unique())],
                    value=[b for b in sorted(df['estado_sanitario'].unique())], multi = True
            ),
            html.Hr()
            ,
            # Map-legend
            html.Ul([
                html.H3("Convenciones:"),
                html.Li("Sano", className='circle', style={'background': 'green','color':'black',
                    'list-style':'none','text-indent': '17px'}),
                html.Li("Enfermo", className='circle', style={'background': 'yellow','color':'black',
                    'list-style':'none','text-indent': '17px','white-space':'nowrap'}),
                html.Li("Critico", className='circle', style={'background': 'orange','color':'black',
                    'list-style':'none','text-indent': '17px'}),
                html.Li("Muerto", className='circle', style={'background': 'red','color':'black',
                    'list-style':'none','text-indent': '17px'})
            ]
            ),
            html.Hr()
            ,
            
            

            # Borough_checklist
            html.H3('Seleccione Comuna: '),
            dcc.Dropdown(id='comuna_name',
                    options=[{'label':str(b),'value':b} for b in sorted(df['comuna'].unique())],
                    value=[b for b in sorted(df['comuna'].unique())], multi = True
            )
                ],className="cardmap")
            ],lg=3)
            
            
            ,
            dbc.Col([

        html.Div([
            dcc.Graph(id='graph',className="mapview"
            )
        ], className='nine columns')

            ],lg=9)
        ])
        ])


#---------------------------------------------------------------
# Output of Graph
@callback(Output('graph', 'figure'),
              [Input('comuna_name', 'value'),
               Input('status_type', 'value')])

def update_figure(chosen_comuna,chosen_status):
    df_sub = df[(df['comuna'].isin(chosen_comuna)) &
                (df['estado_sanitario'].isin(chosen_status))]

    # Create figure
    locations=[go.Scattermapbox(
                    lon = df_sub['longitude'],
                    lat = df_sub['latitude'],
                    mode='markers',
                    marker={'color' : df_sub['color']},
                    unselected={'marker' : {'opacity':1}},
                    selected={'marker' : {'opacity':0.5, 'size':25}},
                    hoverinfo='text',
                    hovertext=df_sub['nom_comun'],
                    customdata=df_sub['Codigo_Uni']
    )]



    # Return figure
    return {
        'data': locations,
        'layout': go.Layout(
            uirevision= 'foo', #preserves state of figure/map after callback activated
            clickmode= 'event+select',
            hovermode='closest',
            hoverdistance=2,
            autosize=True,
            mapbox=dict(
                accesstoken=mapbox_token,
                bearing=25,
                style='stamen-terrain',
                center=dict(
                    lat=4.430081,
                    lon=-75.2112492
                ),
                pitch=40,
                zoom=12
            ),
        )
    }

