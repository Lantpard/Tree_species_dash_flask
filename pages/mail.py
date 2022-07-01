from dash import html,dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page


register_page(__name__, path="/mail")


layout = html.Div([
        html.Header( 
                html.H1("Contactanos")
                )
            ,
        html.Div([

                html.Div([
                    dbc.NavLink((

                    html.Img(src='/assets/face.webp', height="30")
                    ,html.H3("Alcaldia de ibagué")),href="https://es-la.facebook.com/alcaldiaibague/", target="_blank",class_name="link")

                ] ,className="facebook text-center textblanco")
                ,
                html.Div([
                    dbc.NavLink((
                    html.Img(src='/assets/twitter.webp', height="30")
                    ,html.H3("Alcaldia de ibagué")),href="https://twitter.com/Alcaldiaibague", target="_blank")
                ],className="twitter")
                ,
                html.Div([
                    dbc.NavLink((
                    html.Img(src='/assets/insta.webp', height="30",className="mx-2")
                    ,html.H3("Alcaldia de ibagué")),href="https://www.instagram.com/alcaldiadeibague/", target="_blank")
                ],className="instagram")
                ,
                html.Div([
                    dbc.NavLink((
                    html.Img(src='/assets/alcaldia.png', height="40")
                    ,html.H3("Alcaldia de ibagué")),href="https://ibague.gov.co/portal/index.php", target="_blank")
                ],className="web")

        ],className="info")
        ,
        html.Form([
                html.Div(
                    [
                    
                        dbc.Input(type="email", id="example-email", placeholder="name@example.com"),
                        
                    ],
                        className="correo",
                    )

                , html.Div(
                    [
                        dcc.Textarea(
                            id='textarea-example',
                            value='',
                            style={'width': '100%', 'height': 300},
                        )
                    ],
                        className="Observacion",
                    ) ,
                    html.Button([ "Enviar"

                                    ],type="submit",className="btn btn-light btn-outline-primary button1")
                    ],className="formulario")

        ],className="contenedor6")