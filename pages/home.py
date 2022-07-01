from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

register_page(__name__, path="/")


layout = html.Div([
    
            html.Header( 
                html.H1("Especies Arboreas de Ibague")
                )
            ,

            html.Div([
    
                html.Div([
                    dbc.NavLink(
                    (html.Img(src='/assets/info.png', height="100px", width="100px"),
                    html.H3("Acerca de")),href="/about")
        
                ],className="widget1")
                
                ,

                html.Div([
                    dbc.NavLink(
                    (html.Img(src='/assets/app.png', height="100px", width="100px"),
                    html.H3("Monitoreo")),href="/maptrees5")
                ],className="widget2"),

                html.Div([
                    dbc.NavLink(
                    (html.Img(src='/assets/arbol2.png', height="100px", width="100px"),
                    html.H3("Arboles en Ibague")),href="/storytelling")
                ],className="widget3"),

                html.Div([
                    dbc.NavLink(
                    (html.Img(src='/assets/prediccion.png', height="100px", width="100px"),
                    html.H3("Prediccion")),href="/model")
                ],className="widget4"),

                html.Div([
                    dbc.NavLink(
                    (html.Img(src='/assets/equipo.png', height="100px", width="100px"),
                    html.H3("Equipo")),href="/equipo")
                ],className="widget5"),

                html.Div([
                    dbc.NavLink(
                    (html.Img(src='/assets/mail.png', height="100px", width="100px"),
                    html.H3("Contactanos")),href="/mail")
                ],className="widget6")

            ],className="contenido")

        ],className="contenedor")