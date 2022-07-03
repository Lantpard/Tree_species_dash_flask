from dash import html , dcc
import plotly.graph_objects as go
import geopandas as gpd
import pyproj
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
          
class graphtrees2:
    
 
    def __init__(self,map_title:str, ID:str,df1,df2):
          
        self.map_title = map_title 
        self.id = ID
        self.df1 = df1
        self.df2 = df2

 
    #@staticmethod
    def figura(self):
        df=self.df1
        data=self.df2

        def bad_conditions(estado):
            if estado in ['Enfermo', 'Muerto', 'Critico']:
                return 1
            else:
                return 0

        df['mal_estado'] = df.estado_sanitario.apply(bad_conditions)

        df.groupby('comuna').mal_estado.sum()

        trees_mal_estado_per_comuna = df.groupby('comuna').mal_estado.sum()
        comuna_values_mal = []
        for i in trees_mal_estado_per_comuna.index:
            new_value = f'COMUNA {i}'
            comuna_values_mal.append(new_value)

        mal_for_merge = {
            'COMUNAS':comuna_values_mal,
            'MAL_ESTADO':trees_mal_estado_per_comuna.values
        }

        mal_df = pd.DataFrame(mal_for_merge)

        mal_estado_data = data.merge(mal_df, how='inner', on='COMUNAS')

        map_df = mal_estado_data
        map_df.index = ['COMUNA 1', 'COMUNA 1_', 'COMUNA 5', 'COMUNA 4', 'COMUNA 3', 'COMUNA 2',
            'COMUNA 10', 'COMUNA 8', 'COMUNA 11', 'COMUNA 12', 'COMUNA 6',
            'COMUNA 7', 'COMUNA 9', 'COMUNA 13']
        map_df.to_crs(pyproj.CRS.from_epsg(4326), inplace=True)

        fig = px.choropleth(map_df, geojson=map_df.geometry, locations=map_df.index, color='MAL_ESTADO', color_continuous_scale="reds")
        fig.update_geos(fitbounds='locations', visible=False)

        fig.update_layout(
            title = {
                'text':'Trees in bad conditions on Ibague',
                'font_family':'Times New Roman',
                'font_size':22,
                'font_color':"white", 
                'x':0.45,
            },
            
            coloraxis_colorbar={
                'title':'Number of trees',      
            }
            , paper_bgcolor="black",plot_bgcolor="black"
                )

        
        return fig


    def display(self):   
        layout = html.Div(
            [
                html.H4([self.map_title]),
                html.Div([
                    dcc.Graph(figure=graphtrees2.figura(self), id=self.id)
                ])
                
            ]
        )
        return layout