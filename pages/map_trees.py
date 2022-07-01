
from dash import html , dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page
import dash_leaflet as dl

from components.maps.mapstrees import map_trees
from components.sampledf.model_data import df_comunas,df_ibague

mapa_trees = map_trees('Mapa Arboles Ibague', 'div_map_trees', df_ibague, df_comunas)


register_page(__name__, path="/maptrees")

df1=df_ibague
df2=df_comunas

df1["lat"]=df1["latitude"]
df1["lon"]=df1["longitude"]

comuna=list(df1["comuna"].unique())

"""    
df3=df1[df1["comuna"]==1]
comuna1 = [dl.Circle(center=[row["lat"], row["lon"]],radius=2) for i, row in df3.iterrows()]

df3=df1[df1["comuna"]==2]
comuna2 = [dl.Circle(center=[row["lat"], row["lon"]],radius=2) for i, row in df3.iterrows()]

df3=df1[df1["comuna"]==3]
comuna3 = [dl.Circle(center=[row["lat"], row["lon"]],radius=2) for i, row in df3.iterrows()]

df3=df1[df1["comuna"]==4]
comuna4 = [dl.Circle(center=[row["lat"], row["lon"]],radius=2) for i, row in df3.iterrows()]

df3=df1[df1["comuna"]==5]
comuna5 = [dl.Circle(center=[row["lat"], row["lon"]],radius=2) for i, row in df3.iterrows()]

df3=df1[df1["comuna"]==6]
comuna6 = [dl.Circle(center=[row["lat"], row["lon"]],radius=2) for i, row in df3.iterrows()]
"""
df3=df1[df1["comuna"]==7]
comuna7 = [dl.Circle(center=[row["lat"], row["lon"]],radius=2) for i, row in df3.iterrows()]
"""
df3=df1[df1["comuna"]==8]
comuna8 = [dl.Circle(center=[row["lat"], row["lon"]],radius=2) for i, row in df3.iterrows()]

df3=df1[df1["comuna"]==9]
comuna9 = [dl.Circle(center=[row["lat"], row["lon"]],radius=2) for i, row in df3.iterrows()]

df3=df1[df1["comuna"]==10]
comuna10 = [dl.Circle(center=[row["lat"], row["lon"]],radius=2) for i, row in df3.iterrows()]

df3=df1[df1["comuna"]==11]
comuna11 = [dl.Circle(center=[row["lat"], row["lon"]],radius=2) for i, row in df3.iterrows()]

df3=df1[df1["comuna"]==12]
comuna12 = [dl.Circle(center=[row["lat"], row["lon"]],radius=2) for i, row in df3.iterrows()]

df3=df1[df1["comuna"]==13]
comuna13 = [dl.Circle(center=[row["lat"], row["lon"]],radius=2) for i, row in df3.iterrows()]
"""

df4=df2[df2['COMUNAS']=="COMUNA 1"]

geojson=df4

polygon = dl.GeoJSON(url='./data/dftrees/COMUNAS.geojson',zoomToBounds=True, zoomToBoundsOnClick=True, id="comunas")


keys = ["watercolor", "toner", "terrain"]
url_template = "http://{{s}}.tile.stamen.com/{}/{{z}}/{{x}}/{{y}}.png"
attribution = 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, ' \
'<a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data ' \
'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'



layout= html.Div(
    [
        dbc.Row([
            dbc.Col([
                html.Div([
                   dl.Map([
            dl.LayersControl(
                [dl.BaseLayer(dl.TileLayer(url=url_template.format(key), attribution=attribution),
                      name=key, checked=key == "toner") for key in keys] +
                [
                    #dl.Overlay(dl.LayerGroup(comuna1), name="comuna1", checked=True),
                #dl.Overlay(dl.LayerGroup(comuna2), name="comuna2", checked=False)
                #,
                #dl.Overlay(dl.LayerGroup(comuna3), name="comuna3", checked=False)
                #,
                #dl.Overlay(dl.LayerGroup(comuna4), name="comuna4", checked=False)
                #,
                #dl.Overlay(dl.LayerGroup(comuna5), name="comuna5", checked=False)
                #,
                #dl.Overlay(dl.LayerGroup(comuna6), name="comuna6", checked=False)
                #,
                dl.Overlay(dl.LayerGroup(comuna7), name="comuna7", checked=True)
                #,
                #dl.Overlay(dl.LayerGroup(comuna8), name="comuna8", checked=False)
                #,
                #dl.Overlay(dl.LayerGroup(comuna9), name="comuna9", checked=False)
                #,
                #dl.Overlay(dl.LayerGroup(comuna10), name="comuna10", checked=False)
                #,
                #dl.Overlay(dl.LayerGroup(comuna11), name="comuna11", checked=False)
                #,
                #dl.Overlay(dl.LayerGroup(comuna12), name="comuna12", checked=False)
                #,
                #dl.Overlay(dl.LayerGroup(comuna13), name="comuna13", checked=False)
                ,
                dl.Overlay(dl.LayerGroup(polygon), name="pol1", checked=False)]

            )
            ], center=(4.430081,-75.2112492), zoom=13, style={'height': '600px'})  
                ],id="row_map2")   
            ])
            #,dcc.Dropdown(id="dd", value=dd_defaults, options=dd_options, clearable=False, multi=True)
        ], className= "card"),

    ], className='container-fluid', style={'margin': 'auto', 'width':'100%'}
)  

"""
@clientside_callback(
    [Output("geojson", "hideout")], 
    [Input("dd", "value")],
    prevent_initial_call=True
    )
"""
