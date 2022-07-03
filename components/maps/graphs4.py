from dash import html , dcc
import plotly.graph_objects as go
import geopandas as gpd
import pyproj
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
          
class commontrees2:
    
 
    def __init__(self,map_title:str, ID:str,df1):
          
        self.map_title = map_title 
        self.id = ID
        self.df1 = df1
    

 
    #@staticmethod
    def figura(self):
        df=self.df1

        c_columns = ['cre', 'crh', 'cra', 'coa', 'ce', 'civ', 'crt', 'crg', 'cap']

        conflictos = {
            'cre': 'redes eléctricas',
            'crh':'redes hidráulicas',
            'cra':'redes de alcantarillado',
            'coa':'otros árboles',
            'ce':'estructuras',
            'civ':'infraestructura vial',
            'crt':'redes telefónicas',
            'crg':'redes de gas',
            'cap':'alumbrado público',
        }

        c_data = df[c_columns].rename(columns=conflictos).replace({'Si':1, 'No':0})
        conflict_data = c_data.sum().sort_values(ascending=False).head()
        conflict_X = conflict_data.index
        conflict_Y = conflict_data.values
        fig = px.bar(y=conflict_Y, x=conflict_X, text_auto='.2s',
                    title="Most type of conflicts of trees",
                    labels={'x':'Conflict', 'y':'Count'},
                    color_discrete_sequence =['rgb(231,63,116)'])

       

        fig.update_layout(title_x=0.5,paper_bgcolor="black",plot_bgcolor="black")

        
        return fig


    def display(self):   
        layout = html.Div(
            [
                html.H4([self.map_title]),
                html.Div([
                    dcc.Graph(figure=commontrees2.figura(self), id=self.id)
                ])
                
            ]
        )
        return layout