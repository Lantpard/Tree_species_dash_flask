from dash import html , dcc
import plotly.graph_objects as go
import geopandas as gpd
import pyproj
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
          
class graphtrees:
    
 
    def __init__(self,map_title:str, ID:str,df1,df2):
          
        self.map_title = map_title 
        self.id = ID
        self.df1 = df1
        self.df2 = df2

 
    #@staticmethod
    def figura(self):
        df=self.df1
        data=self.df2

        trees_per_comuna = df.comuna.value_counts()

        comuna_values = []
        for i in trees_per_comuna.index:
            new_value = f'COMUNA {i}'
            comuna_values.append(new_value)
            
        data_for_merge = {
                'COMUNAS':comuna_values,
                'TREES':trees_per_comuna.values
        }

        trees_df = pd.DataFrame(data_for_merge)

        new_data = data.merge(trees_df, how='inner', on='COMUNAS')

        map_df = new_data
        map_df.index = ['COMUNA 1', 'COMUNA 1_', 'COMUNA 5', 'COMUNA 4', 'COMUNA 3', 'COMUNA 2',
            'COMUNA 10', 'COMUNA 8', 'COMUNA 11', 'COMUNA 12', 'COMUNA 6',
            'COMUNA 7', 'COMUNA 9', 'COMUNA 13']
        map_df.to_crs(pyproj.CRS.from_epsg(4326), inplace=True)

        fig = px.choropleth(map_df, geojson=map_df.geometry, locations=map_df.index, color='TREES', color_continuous_scale="greens")
        fig.update_geos(fitbounds='locations', visible=False)

        fig.update_layout(
            title = {
                'text':'Trees on Ibague',
                'font_family':'Times New Roman',
                'font_size':22,
                'font_color':"white", 
                'x':0.45,
            },
            
            coloraxis_colorbar={
                'title':'Number of trees',      
            },
            paper_bgcolor="black",plot_bgcolor="black"
                )

        
        return fig


    def display(self):   
        layout = html.Div(
            [
                html.H4([self.map_title]),
                html.Div([
                    dcc.Graph(figure=graphtrees.figura(self), id=self.id)
                ])
                
            ]
        )
        return layout