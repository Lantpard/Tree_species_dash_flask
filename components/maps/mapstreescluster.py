import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash_extensions.javascript import Namespace,assign
from dash import Dash, html
from geojson import Feature, FeatureCollection, Point
import pandas as pd


class map_trees_cluster:

    def __init__(self,map_title:str, ID:str,df):
        """__init__ _summary_

        Args:
            map_title (str): Titulo del mapa, html H4 element
            ID (str): css id to use with callbacks
            df (_type_): dataframe with info to use in choropleth
            markers (_type_): small point as overlay in map
        """        
        self.map_title = map_title 
        self.id = ID
        self.df = df
 

        
        

    def display(self):

        df=self.df

        
        m=[]
        for i in range(len(df)):
            m.append(dict(lat=df["latitude"].iloc[i], lon=df["longitude"].iloc[i]))


        url = 'https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png'

        layout = dl.Map([
            dl.TileLayer(url=url),
            # From in-memory geojson. All markers at same point forces spiderfy at any zoom level.
            dl.GeoJSON(data=dlx.dicts_to_geojson(m), cluster=True, zoomToBoundsOnClick=True,superClusterOptions={"radius": 30})
            # From hosted asset (best performance).
   
            ], center=(4.430081,-75.2112492), zoom=6,style={'width': '100%', 'height': '50vh', 'margin': "auto", "display": "block"})
 

        return layout



