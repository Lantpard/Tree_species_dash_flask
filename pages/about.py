from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
from components.markdown.markformat import markformat
register_page(__name__)


file1 = open('./data/mdsamples/story1.md')
texto1  = markformat("", file1.read())

layout = html.Div([
    
            html.Header( 
                html.H1("Green Ibagué")
                )
            ,

            html.Div([
    
                
                texto1.show()
                ,dbc.NavLink(
                    (html.H6("Enlace")),href="https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Censo-de-Arbolado-urbano-en-Ibagu-Sria-Ambiente-y-/am4p-tz7w",target="_blank")

            ],className="descripcion")
                ,
            html.Div([
                html.Img(src='/assets/correlation.webp')
            ],className="correlation"),

            html.Div([
                html.Img(src='/assets/mintic.webp')
            ],className="mintic")

        ],className="contenedor2")