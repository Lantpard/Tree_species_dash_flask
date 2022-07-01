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

        df["lat"]=df["latitude"]
        df["lon"]=df["longitude"]

        df1=df[df["comuna"]==1]
        comuna1 = [dl.Circle(center=[row["lat"], row["lon"]],radius=2) for i, row in df1.iterrows()]

        df1=df[df["comuna"]==5]
        comuna5 = [dl.Circle(center=[row["lat"], row["lon"]],radius=2) for i, row in df1.iterrows()]
        
        m=[]
        for i in range(len(df)):
            m.append(dict(lat=df["latitude"].iloc[i], lon=df["longitude"].iloc[i]))


        keys = ["watercolor", "toner", "terrain"]
        url_template = "http://{{s}}.tile.stamen.com/{}/{{z}}/{{x}}/{{y}}.png"
        attribution = 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, ' \
              '<a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data ' \
              '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'

        layout = dl.Map([
            dl.TileLayer(),
            # From in-memory geojson. All markers at same point forces spiderfy at any zoom level.
            dl.GeoJSON(data=dlx.dicts_to_geojson(m), cluster=True, zoomToBoundsOnClick=True,superClusterOptions={"radius": 60})
            # From hosted asset (best performance).
   
            ], center=(4.430081,-75.2112492), zoom=13, style={'height': '600px'})
 

        return layout



