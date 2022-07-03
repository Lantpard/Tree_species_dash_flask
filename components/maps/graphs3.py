from dash import html , dcc
import plotly.graph_objects as go
import geopandas as gpd
import pyproj
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
          
class commontrees:
    
 
    def __init__(self,map_title:str, ID:str,df1):
          
        self.map_title = map_title 
        self.id = ID
        self.df1 = df1
    

 
    #@staticmethod
    def figura(self):
        df=self.df1
   

        most_common_trees = df.nom_comun.value_counts().head()
        x_common = most_common_trees.index
        y_common = most_common_trees.values
      

        fig = px.bar(y=y_common, x=x_common, text_auto='.2s',
                    title="Most common trees in Ibague",
                    labels={'x':'Trees', 'y':'Count'},
                    color_discrete_sequence =['mediumseagreen'])

       

        fig.update_layout(title_x=0.5,paper_bgcolor="black",plot_bgcolor="black")

        
        return fig


    def display(self):   
        layout = html.Div(
            [
                html.H4([self.map_title]),
                html.Div([
                    dcc.Graph(figure=commontrees.figura(self), id=self.id)
                ])
                
            ]
        )
        return layout