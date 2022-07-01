import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash_extensions.javascript import Namespace,assign
from dash import Dash, html
from geojson import Feature, FeatureCollection, Point
import pandas as pd


class map_trees:

    def __init__(self,map_title:str, ID:str, dataframe1="" ,dataframe2="" ):
        """__init__ _summary_

        Args:
            map_title (str): Titulo del mapa, html H4 element
            ID (str): css id to use with callbacks
            df (_type_): dataframe with info to use in choropleth
            markers (_type_): small point as overlay in map
        """        
        self.map_title = map_title 
        self.id = ID
        self.df1 = dataframe1
        self.df2 = dataframe2

        
        

    def display(self):

        df1=self.df1
        df2=self.df2

        df1["lat"]=df1["latitude"]
        df1["lon"]=df1["longitude"]

        comuna=list(df1["comuna"].unique())
    
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

        df3=df1[df1["comuna"]==7]
        comuna7 = [dl.Circle(center=[row["lat"], row["lon"]],radius=2) for i, row in df3.iterrows()]

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
        
        df4=df2[df2['COMUNAS']=="COMUNA 1"]

        geojson=df4

        polygon = dl.GeoJSON(url='./data/dftrees/COMUNAS.geojson',zoomToBounds=True, zoomToBoundsOnClick=True, id="comunas")
        

        keys = ["watercolor", "toner", "terrain"]
        url_template = "http://{{s}}.tile.stamen.com/{}/{{z}}/{{x}}/{{y}}.png"
        attribution = 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, ' \
              '<a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data ' \
              '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'

        layout = dl.Map([
            dl.LayersControl(
                [dl.BaseLayer(dl.TileLayer(url=url_template.format(key), attribution=attribution),
                      name=key, checked=key == "toner") for key in keys] +
                [dl.Overlay(dl.LayerGroup(comuna1), name="comuna1", checked=True),
                dl.Overlay(dl.LayerGroup(comuna2), name="comuna2", checked=False)
                ,
                dl.Overlay(dl.LayerGroup(comuna3), name="comuna3", checked=False)
                ,
                dl.Overlay(dl.LayerGroup(comuna4), name="comuna4", checked=False)
                ,
                dl.Overlay(dl.LayerGroup(comuna5), name="comuna5", checked=False)
                ,
                dl.Overlay(dl.LayerGroup(comuna6), name="comuna6", checked=False)
                ,
                dl.Overlay(dl.LayerGroup(comuna7), name="comuna7", checked=False)
                ,
                dl.Overlay(dl.LayerGroup(comuna8), name="comuna8", checked=False)
                ,
                dl.Overlay(dl.LayerGroup(comuna9), name="comuna9", checked=False)
                ,
                dl.Overlay(dl.LayerGroup(comuna10), name="comuna10", checked=False)
                ,
                dl.Overlay(dl.LayerGroup(comuna11), name="comuna11", checked=False)
                ,
                dl.Overlay(dl.LayerGroup(comuna12), name="comuna12", checked=False)
                ,
                dl.Overlay(dl.LayerGroup(comuna13), name="comuna13", checked=False)
                ,
                dl.Overlay(dl.LayerGroup(polygon), name="pol1", checked=False)]

            )
            ], center=(4.430081,-75.2112492), zoom=13, style={'height': '600px'})
 

        return layout



