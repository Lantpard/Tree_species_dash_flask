from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

register_page(__name__, path="/result")


layout = html.Div([
    
            html.Header( 
                html.H1("su arbol esta: ")
                )
            

        ],className="contenedor")