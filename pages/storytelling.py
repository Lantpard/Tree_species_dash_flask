#libraries
from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page
import pandas as pd

# dash-labs plugin call, menu name and route
register_page(__name__, path="/storytelling")

from components.markdown.markformat import markformat
from components.maps.mapsample import mapsample

from components.maps.mapstreescluster import map_trees_cluster
from components.maps.graphs import graphtrees
from components.maps.graphs2 import graphtrees2
from components.maps.graphs3 import commontrees
from components.maps.graphs4 import commontrees2
from components.sampledf.model_data import df_comunas,df_ibague

dfEnfermo=df_ibague[df_ibague["estado_sanitario"]=="Enfermo"]
dfCritico=df_ibague[df_ibague["estado_sanitario"]=="Critico"]
dfMuerto=df_ibague[df_ibague["estado_sanitario"]=="Muerto"]



mapclusterEnfermo = map_trees_cluster('Mapa Arboles Ibague', 'div_map_trees',dfEnfermo)

mapclusterCritico = map_trees_cluster('Mapa Arboles Ibague', 'div_map_trees',dfCritico)

mapclusterMuerto = map_trees_cluster('Mapa Arboles Ibague', 'div_map_trees',dfMuerto)

graphtree = graphtrees ("",'graph1',df_ibague,df_comunas)
graphtree2 = graphtrees2 ("",'graph2',df_ibague,df_comunas)

common = commontrees ("",'graph3',df_ibague)
common2 = commontrees2 ("",'graph4',df_ibague)


file1 = open('./data/mdsamples/story1.md')
file2 = open('./data/mdsamples/story2.md')
file3 = open('./data/mdsamples/story3.md')
file4 = open('./data/mdsamples/story4.md')
file5 = open('./data/mdsamples/story5.md')
file6 = open('./data/mdsamples/story6.md')
file7 = open('./data/mdsamples/story7.md')
file8 = open('./data/mdsamples/story8.md')
file9 = open('./data/mdsamples/story9.md')

texto1  = markformat('', file2.read())
texto2  = markformat('', file3.read())
texto3  = markformat('', file4.read())
texto4  = markformat('', file5.read())
texto5  = markformat('', file6.read())
texto6  = markformat('', file7.read())
texto7  = markformat('', file8.read())
texto8  = markformat('', file9.read())

mapa_ejemplo_story = mapsample('Mapa elecciones', 'id_mapa_story1')


# specific layout for this page
layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                 html.H1(['¿Cómo están los árboles en Ibagué?'],id="div_title_maps"),
                
            ], lg=12), 
           
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                 texto1.show()

            ], lg=4), 

            dbc.Col([
                html.H2(""),
                 graphtree.display()

            ], lg=8,class_name="maptext"), 
   
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                 texto2.show()

            ], lg=4), 

            dbc.Col([
                html.H2(""),
                 common.display()

            ], lg=8,class_name="maptext"), 
   
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                 dbc.NavLink((

                    html.Img(src='/assets/ocobo.jpeg',height="400px"),
                    html.H6("Ocobo. Fuente: Enlace")
                    ),href="https://co.pinterest.com/pin/346706871284432449/", target="_blank",class_name="link")

            ], lg=3), 

            dbc.Col([
                 dbc.NavLink((

                    html.Img(src='/assets/palma.jpeg',height="400px")
                    ,
                    html.H6("Palma Areca. Fuente: Enlace")
                    ),href="https://www.jardineriaon.com/palmeras-areca.html", target="_blank",class_name="link")
             

            ], lg=6), 
            dbc.Col([
              
               dbc.NavLink((

                    html.Img(src='/assets/pera.jpg',height="400px")
                    ,
                    html.H6("Pera Malaca. Fuente: Enlace")
                    ),href="https://www.flickr.com/photos/barloventomagico/2069979823", target="_blank",class_name="link")

            ], lg=3)
   
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                 texto3.show()

            ], lg=4), 

            dbc.Col([
                html.H2(""),
                 graphtree2.display()

            ], lg=8,class_name="maptext"), 
   
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                 texto4.show()

            ], lg=4), 

            dbc.Col([
                html.H2(""),
                 common2.display()

            ], lg=8,class_name="maptext"), 
   
        ]),

        html.Hr(),
        dbc.Row([
            dbc.Col([
                 html.H1(['¿Por qué es importante velar por el buen estado de los árboles?'],id="div_title_maps"),
                
            ], lg=12), 
           
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                 texto8.show()

            ], lg=4), 

            dbc.Col([
                dbc.NavLink((

                    html.Img(src='/assets/banco.jpeg',height="400px")
                    ,
                    html.H6("Banco de Desarrollo de América Latina. Fuente: Enlace")
                    ),href="https://www.caf.com/es/conocimiento/visiones/2020/12/bosques-urbanos-para-mejorar-la-calidad-de-vida-en-las-ciudades/", target="_blank",class_name="link")

            ], lg=8,class_name="maptext"), 
   
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                 html.H1(['Agrupamiento de árboles por estado sanitario'],id="div_title_maps"),
                
            ], lg=12), 
           
        ]),
         html.Hr(),

        dbc.Row([
            dbc.Col([
                 texto5.show()

            ], lg=4), 

            dbc.Col([
                 mapclusterEnfermo.display()

            ], lg=8), 
   
        ]),
        
        html.Hr(),
        dbc.Row([
            dbc.Col([
                 texto6.show()

            ], lg=4), 

            dbc.Col([
                 mapclusterCritico.display()

            ], lg=8), 
   
        ]),
        html.Hr()
        ,
        dbc.Row([
            dbc.Col([
                 texto7.show()

            ], lg=4), 

            dbc.Col([
                 mapclusterMuerto.display()

            ], lg=8), 
   
        ])
        ,
        html.Hr()
        
    ]
)