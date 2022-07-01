from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

register_page(__name__, path="/equipo")


layout = html.Div([
    
            html.Header( 
                html.H1("Equipo")
                )
            ,

            html.Div([
    
                html.Div([
                    html.Img(src='/assets/eduard.webp', height="100px", width="100px",className="center foto"),
                    html.Br(),
                    html.H3("Eduard Molano"),
                    html.H3("Ing. Electrónico")
        
                ],className="foto1")
                
                ,

                html.Div([
                    
                    html.Img(src='/assets/leo.png', height="100px", width="100px",className="center foto"),
                    html.Br(),
                    html.H3("Leonardo Pérez"),
                    html.H3("Ing. Electromecanico")

                ],className="foto2"),

                html.Div([
                    html.Img(src='/assets/daniel.jpeg', height="100px", width="100px",className="center foto"),
                    html.Br(),
                    html.H3("Daniel Ruiz"),
                    html.H3("Ing. Civil")

                ],className="foto3"),

                html.Div([
                    html.Img(src='/assets/luisa.jpeg', height="100px", width="100px",className="center foto"),
                    html.Br(),
                    html.H3("Luisa de la Hortua"),
                    html.H3("Estadística")

                ],className="foto4"),

                html.Div([
                    html.Img(src='/assets/stiven.jpeg', height="100px", width="100px",className="center imgRedonda"),
                    html.Br(),
                    html.H3("Stiven Cabrera"),
                    html.H3("Est. Ing. Biológica")

                ],className="foto5"),

                html.Div([
                   
                    html.Img(src='/assets/juan.jpeg', height="100px", width="100px",className="center foto"),
                    html.Br(),
                    html.H3("Juan Bautista"),
                    html.H3("Ing. Sistemas")
                    
                ],className="foto6")

            ],className="contenido5")

        ],className="contenedor5")