from dash import html,dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

from components.maps.mapcol_departamentos import mapcol_departamentos


from components.sampledf.model import df_maptest

register_page(__name__,path="/dash1")

mapa_colombia_departamentos = mapcol_departamentos('Mapa Departamentos Colombia', 'div_municipios_fig2',df_maptest)

layout = html.Div([
    
            html.Header( 
                html.H1("Monitoreo Especies")
                )
            ,

            html.Div([
    
                html.Div([
                    html.H2("¿Como Funciona?")
                    ],className="label1"),
                html.Div([
                html.H2("¿Que desea ver?")
                    ],className="label2"),
                

                 html.Div([
                    html.Div(['Seleccione tipo'], className="mb-2  selector-label"),
                    dcc.Dropdown(
                    id="id_selector_tipo",
                    options=[
                        {"label": "Arborizacion", "value": "Arborizacion"},
                        {"label": "Mantenimiento", "value": "Mantenimiento"},
                        {"label": "Siembra", "value": "Siembra"}
                    ],
                    value=['Arborizacion'],
                    multi = False
                )
                ],className="select1"),
                html.Div([
                html.H2("Filtrar por:")
                ],className="label3"),
                
                html.Div([
                    html.Div(['Seleccione la comuna'], className="mb-2  selector-label"),
                    dcc.Dropdown(
                    id="id_selector_comuna",
                    options=[
                        {"label": "TODOS", "value": "TODOS"},
                        {"label": "1", "value": "1"},
                        {"label": "2", "value": "2"},
                        {"label": "3", "value": "3"},
                        {"label": "4", "value": "4"},
                    ],
                    value=['1', '2', '3', '4'],
                    multi = True
                )
                ],className="select2"),
                html.Div([
                    html.Div(['Especie (Nombre Comun)'], className="mb-2  selector-label"),
                    dcc.Dropdown(
                    id="id_selector_especie",
                    options=[
                        {"label": "TODOS", "value": "TODOS"},
                        {"label": "Ocobo", "value": "Ocobo"},
                        {"label": "Palma Areca", "value": "Palma Areca"},
                        {"label": "Palma Malaca", "value": "Palma Malaca"},
                        {"label": "Mango", "value": "Mango"},
                    ],
                    value=['Ocobo', 'Palma Areca', 'Palma Malaca', 'Mango'],
                    multi = True
                )
                ],className="select3"),
                html.Div([
                    html.Div(['Estado Sanitario'], className="mb-2  selector-label"),
                    dcc.Dropdown(
                    id="id_selector_estado",
                    options=[
                        {"label": "TODOS", "value": "TODOS"},
                        {"label": "Sano", "value": "Sano"},
                        {"label": "Enfermo", "value": "Enfermo"},
                        {"label": "Critico", "value": "Critico"},
                        {"label": "Muerto", "value": "Muerto"},
                    ],
                    value=['Sano', 'Enfermo', 'Critico', 'Muerto'],
                    multi = True
                )
                ],className="select4")
            ],className="filtros")

                ,
            html.Div([
                
                    mapa_colombia_departamentos.display()  
                    ],id="row_map",className="map"),


        ],className="contenedor3")