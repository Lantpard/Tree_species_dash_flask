import folium
import geopandas as gpd
from folium import plugins
from folium.plugins import HeatMap

import pandas as pd
from components.sampledf.model_data import df_comunas,df_ibague

def mapl():

    data = df_ibague

    star_coords = (4.430081,-75.2112492)

    map_hooray = folium.Map(location=star_coords, zoom_start=13, tiles ='Stamen Terrain')


    heat_data = [[row['latitude'],row['longitude']] for index, row in data.iterrows()]

    HeatMap(heat_data).add_to(map_hooray)

    map_hooray.save('assets/html/heatmap.html')
  
    return map_hooray