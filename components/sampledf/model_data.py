import pandas as pd
import geopandas as gpd
from typing import NamedTuple, Optional

df_ibague = pd.read_csv('./data/dftrees/Datos_Ibague_limpios.csv',dtype={'latitude':float,'longitude':float},low_memory=False)

df_comunas = gpd.read_file('./data/dftrees/COMUNAS.geojson')



#df1=df_ibague[df_ibague['comuna']==1]
#for i in range(len(df1)):
#    print(df1['latitude'].iloc[i],df1['longitude'].iloc[i])

#print(len(df1))

class Contact(NamedTuple):
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None