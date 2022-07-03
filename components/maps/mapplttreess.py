from dash import html , dcc
import plotly.graph_objects as go

mapbox_token = 'pk.eyJ1IjoiY3J5cHRvcG90bHVjayIsImEiOiJjazhtbTN6aHEwa3lwM25taW5qNTdicHAwIn0.xFsCTDqPE_0L-OHwv21qTg'

          
class mapplttrees:
   
    def __init__(self,map_title:str, ID:str,df):
        self.map_title = map_title 
        self.id = ID
        self.df = df 

    #@staticmethod
    def figura(self):
        df_sub=self.df

        mapa = go.Scattermapbox(
                    lon = df_sub['longitude'],
                    lat = df_sub['latitude'],
                    mode='markers',
                    marker={'color' : df_sub['color']},
                    unselected={'marker' : {'opacity':1}},
                    selected={'marker' : {'opacity':0.5, 'size':25}},
                    hoverinfo='text',
                    hovertext=df_sub['nom_comun'],
                    customdata=df_sub['Codigo_Uni']
            )
        
        fig = go.Figure(data=mapa)

        layaout= go.Layout(
                uirevision= 'foo', 
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
                ))
        
        fig.update_layout(layaout)
        
        return fig


    def display(self):   
        layout = html.Div(
            [
                html.H4([self.map_title]),
                html.Div([
                    dcc.Graph(figure=mapplttrees.figura(self), id=self.id)
                ])
                
            ]
        )
        return layout