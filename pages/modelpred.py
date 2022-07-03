from dash import html,dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import pandas as pd
import joblib
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import sklearn.metrics as metrics
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold 
from sklearn.model_selection import cross_val_score 
from sklearn.model_selection import cross_val_predict 
from components.markdown.markformat import markformat

register_page(__name__, path="/model")

from components.sampledf.model_data import df_comunas,df_ibague

file1 = open('./data/mdsamples/story10.md')

texto1  = markformat('', file1.read())

df = df_ibague


def load_random_forest_model():

    model = open("./data/model/finalized_model.pkl", 'rb')
    return joblib.load(model)

def prepare_random_forest_data(af, dn,rd,bb,i,h,a,pl,e,ep,oo,
                                re,rh,ra,oa,est,iv,rt,rg,ap,v,cr,ce,
                               ncomun,densidad,comuna,emplazamiento,estadof,habito):

    if af == None:
        af=0
    else:
        af=af

    if dn == None:
        dn=0
    else:
        dn=dn
    
    if rd == None:
        rd=0
    else:
        rd=1

    if bb == None:
        bb=0
    else:
        bb=1

    if i == None:
        i=0
    else:
        i=1

    if h == None:
        h=0
    else:
        h=1

    if a == None:
        a=0
    else:
        a=1

    if pl == None:
        pl=0
    else:
        pl=1

    if e == None:
        e=0
    else:
        e=1

    if ep == None:
        ep=0
    else:
        ep=1

    if oo == None:
        oo=0
    else:
        oo=1

    if re == None:
        re=0
    else:
        re=1

    if rh == None:
        rh=0
    else:
        rh=1

    if ra == None:
        ra=0
    else:
        ra=1
        
    if oa == None:
        oa=0
    else:
        oa=1
    
    if est == None:
        est=0
    else:
        est=1
    
    if iv == None:
        iv=0
    else:
        iv=1
    
    if rt == None:
        rt=0
    else:
        rt=1
    
    if rg == None:
        rg=0
    else:
        rg=1
        
    if ap == None:
        ap=0
    else:
        ap=1
        
    if v == None:
        v=0
    else:
        v=1
        
    if cr == None:
        cr=0
    else:
        cr=1
        
    if ce == None:
        ce=0
    else:
        ce=1

    ncomun=ncomun
    densidad=densidad
    comuna=comuna
    emplazamiento=emplazamiento
    estadof=estadof
    habito=habito


    columnas=['altura_fuste','diametro_normal','rd','bbs','pi','ph','pa','pd','pe','pp','po','cre','crh','cra','coa','ce','civ','crt','crg','cap','r_vol','r_cr','r_ce',
                                'comuna_1','comuna_2','comuna_3','comuna_4','comuna_5','comuna_6','comuna_7','comuna_8','comuna_9','comuna_10','comuna_11','comuna_12','comuna_13',
                                'familia_Acanthaceae','familia_Adoxaceae','familia_Amaranthaceae','familia_Anacardiaceae','familia_Annonaceae','familia_Apocynaceae','familia_Araliaceae','familia_Araucariaceae','familia_Arecaceae','familia_Asparagaceae',
                                'familia_Asteraceae','familia_Basellaceae','familia_Bignoniaceae','familia_Bixaceae','familia_Boraginaceae','familia_Burseraceae','familia_Cactaceae','familia_Calophyllaceae','familia_Cannabaceae',
                                'familia_Capparidaceae','familia_Caricaceae','familia_Casuarinaceae','familia_Chrysobalanaceae','familia_Clusiaceae','familia_Combretaceae','familia_Compositae','familia_Cupressaceae','familia_Cycadaceae','familia_Erythroxylaceae',
                                'familia_Estrelitziaceae','familia_Euphorbiaceae','familia_Fabaceae','familia_Hernandiaceae','familia_Hipericaceae','familia_Juglandaceae','familia_Lacistemataceae','familia_Lamiaceae','familia_Lauraceae',
                                'familia_Lecythidaceae','familia_Leguminosae','familia_Lythraceae','familia_Magnoliaceae','familia_Malpighiaceae','familia_Malvaceae','familia_Melastomataceae','familia_Meliaceae','familia_Moraceae','familia_Moringaceae',
                                'familia_Muntingiaceae','familia_Myrtaceae','familia_Nyctaginaceae','familia_Ocnaceae','familia_Oleaceae','familia_Oxalidaceae','familia_Pandanaceae','familia_Passifloraceae','familia_Phyllanthaceae','familia_Pinaceae',
                                'familia_Piperaceae','familia_Plumbaginaceae','familia_Poaceae','familia_Podocarpaceae','familia_Poligonaceae','familia_Primulaceae','familia_Proteaceae','familia_Ramnaceae','familia_Rosaceae','familia_Rubiaceae','familia_Rutaceae','familia_Salicaceae',
                                'familia_Sapindaceae','familia_Sapotaceae','familia_Scrophulariaceae','familia_Simarubaceae','familia_Solanaceae','familia_Taxodiaceae','familia_Thymelaeaceae','familia_Urticaceae','familia_Verbenaceae','familia_Zygophyllaceae',
                                'habito_crecimiento_Arbol','habito_crecimiento_Arbusto','habito_crecimiento_Bambu','habito_crecimiento_Palma','emplazamiento_Alcorque','emplazamiento_Anden','emplazamiento_Antejardin','emplazamiento_Glorieta','emplazamiento_Parque',
                                'emplazamiento_Separador_vial','emplazamiento_Zona_blanda','estado_fisico_Bueno','estado_fisico_Malo','estado_fisico_Regular','densidad_follaje_Denso','densidad_follaje_Medio','densidad_follaje_Ralo']

    #print("columnas",len(columnas))
    ceros = [0] * 133
    dDataframe= dict(zip(columnas, ceros))

    #print(dDataframe)

    variables=[]
    valores=[]

    variables.append('altura_fuste')
    valores.append(int(af))

    variables.append('diametro_normal')
    valores.append(int(dn))

    variables.append('rd')
    valores.append(rd)

    variables.append('bbs')
    valores.append(bb)

    variables.append('pi')
    valores.append(i)

    variables.append('ph')
    valores.append(h)

    variables.append('pa')
    valores.append(a)
 
    variables.append('pd')
    valores.append(pl)

    variables.append('pe')
    valores.append(e)

    variables.append('pp')
    valores.append(ep)

    variables.append('po')
    valores.append(oo)

    variables.append('cre')
    valores.append(re)
    
    variables.append('crh')
    valores.append(rh)

    variables.append('cra')
    valores.append(ra)

    variables.append('coa')
    valores.append(oa)

    variables.append('ce')
    valores.append(est)

    variables.append('civ')
    valores.append(iv)

    variables.append('crt')
    valores.append(rt)

    variables.append('crg')
    valores.append(rg)

    variables.append('cap')
    valores.append(ap)

    variables.append('r_vol')
    valores.append(v)

    variables.append('r_cr')
    valores.append(cr)

    variables.append('r_ce')
    valores.append(ce)

    variables.append(("comuna_"+str(comuna)))
    valores.append(1)

    familia=df["familia"][df["nom_comun"]==ncomun].iloc[0]

    variables.append(("familia_"+str(familia)))
    valores.append(1)

    variables.append(("habito_crecimiento_"+str(habito)))
    valores.append(1)

    variables.append(("emplazamiento_"+str(emplazamiento)))
    valores.append(1)

    variables.append(("estado_fisico_"+str(estadof)))
    valores.append(1)

    variables.append(("densidad_follaje_"+str(densidad)))
    valores.append(1)

    dVariables=dict(zip(variables, valores))
    #print("variables",len(dVariables))
    #print(dVariables)

    dDataframe.update(dVariables)
    #print("dataframe",len(dDataframe))
    #print(dDataframe)
    data=pd.DataFrame(dDataframe, index=[0])
    #print("data",data.shape)    

    return data




layout = html.Div([
    
            html.Header(
                html.H1("¿Cual es el estado de mi Árbol?")
                )
            ,

            html.Div([
                
            
                html.Div(id='my-output')

            ],className="esta2"),

            dbc.Button("¿Como funciona?", id="open-fs"),
                    dbc.Modal(
                        [
                            dbc.ModalHeader(dbc.ModalTitle("Modo de uso")),
                            dbc.ModalBody(texto1.show()),
                        ],
                        id="modal-fs",
                        fullscreen=True
                    )
            ,
            html.Div([
                
                html.H3("Seleccione las caracteristicas de su Árbol")

            ],className="descripcion2")

            ,
            html.Div([
                
                    html.Div([
                        
                        dbc.Label(["Características físicas:"],className="c1"),
                        dbc.Input(placeholder="Altura Fuste",className="c2",name="af",id="af"),
                        dbc.Input(placeholder="Diámetro Normal",className="c3",name="dn",id="dn"),
                        dbc.Checklist(options=[{'label':'Raíces Descubiertas','value':'Raices Descubiertas'}],className="c4",name="rd",id="rd"),
                        dbc.Checklist(options=[{'label':'Bifurcación Basal','value':'Bifurcacion Basal'}],className="c5",name="bb",id="bb")
                    

                    ],className="caracteristicas")

                    ,html.Div([
                
                        dbc.Label("Presencia de plagas:",className="p1"),
                        dbc.Checklist(options=[{'label':'Insectos','value':'Insectos'}],className="p2",name="i",id="i"),
                        dbc.Checklist(options=[{'label':'Hongos','value':'Hongos'}],className="p3",name="h",id="h"),
                        dbc.Checklist(options=[{'label':'Agallas','value':'Agallas'}],className="p4",name="a",id="a"),
                        dbc.Checklist(options=[{'label':'Pudrición Localizada','value':'Pudricion Localizada'}],className="p5",name="pl",id="pl"),
                        dbc.Checklist(options=[{'label':'Epifitas','value':'Epifitas'}],className="p6",name="e" ,id="e"),
                        dbc.Checklist(options=[{'label':'Especies Parasitas','value':'Especies Parasitas'}],className="p7",name="ep",id="ep"),
                        dbc.Checklist(options=[{'label':'Otros Objetos','value':'Otros Objetos'}],className="p8",name="oo",id="oo"),
                    

                    ],className="presencias")

                    ,html.Div([
                
                        dbc.Label(["Conflictos:"],className="con1"),
                        dbc.Checklist(options=[{'label':'Redes Eléctricas','value':'Redes Eléctricas'}],className="con2",name="re",id="re"),
                        dbc.Checklist(options=[{'label':'Redes Hidráulicas','value':'Redes Hidráulicas'}],className="con3",name="rh",id="rh"),
                        dbc.Checklist(options=[{'label':'Redes Alcantarillado','value':'Redes Alcantarillado'}],className="con4",name="ra",id="ra"),
                        dbc.Checklist(options=[{'label':'Otros Árboles','value':'Otros Arboles'}],className="con5",name="oa",id="oa"),
                        dbc.Checklist(options=[{'label':'Estructuras','value':'Estructuras'}],className="con6",name="est",id="est"),
                        dbc.Checklist(options=[{'label':'Infraestructura Vial','value':'Infraestructura Vial'}],className="con7",name="iv",id="iv"),
                        dbc.Checklist(options=[{'label':'Redes telefónicas','value':'Redes telefónicas'}],className="con8",name="rt",id="rt"),
                        dbc.Checklist(options=[{'label':'Redes Gas','value':'Redes Gas'}],className="con9",name="rg",id="rg"),
                        dbc.Checklist(options=[{'label':'Alumbrado Publico','value':'Alumbrado Publico'}],className="con10",name="ap",id="ap"),

                    ],className="conflictos")
                     ,html.Div([
                
                        dbc.Label("Riesgos:",className="r1"),
                        dbc.Checklist(options=[{'label':'Volcamiento','value':'Volcamiento'}],className="r2",name="v",id="v"),
                        dbc.Checklist(options=[{'label':"Caída Ramas",'value':'Caída Ramas'}],className="r3",name="cr",id="cr"),
                        dbc.Checklist(options=[{'label':"Caída Elementos",'value':'Caída Elementos'}],className="r4",name="ce",id="ce"),

                    ],className="riesgos")

                    ,html.Div([

                            html.Div([
                                
                                html.Label(children=['Nombre común: ']),
                                html.Hr(),
                                dcc.Dropdown(id='ncomun',
                                options=[{'label':str(b),'value':b} for b in sorted(df['nom_comun'].unique())],
                                value=[b for b in sorted(df['nom_comun'].unique())], multi = False
                                )

                            ],className="familia")
                            
                            ,html.Div([
                                html.Label(children=['Densidad Follaje: ']),
                                html.Hr(),
                                dcc.Dropdown(id='densidad',
                                options=[{'label':str(b),'value':b} for b in sorted(df['densidad_follaje'].unique())],
                                value=[b for b in sorted(df['densidad_follaje'].unique())], multi = False
                                )

                            ],className="densidad")

                            ,html.Div([

                                html.Label(children=['Comuna: ']),
                                html.Hr(),
                                dcc.Dropdown(id='comuna',
                                options=[{'label':str(b),'value':b} for b in sorted(df['comuna'].unique())],
                                value=[b for b in sorted(df['comuna'].unique())], multi = False
                                )

                            ],className="comuna")
                            
                            ,html.Div([

                                html.Label(children=['Emplazamiento: ']),
                                html.Hr(),
                                dcc.Dropdown(id='emplazamiento',
                                options=[{'label':str(b),'value':b} for b in sorted(df['emplazamiento'].unique())],
                                value=[b for b in sorted(df['emplazamiento'].unique())], multi = False
                                ,loading_state={"component_name":"emplazamiento"} )
                            ],className="emplazamiento")

                            ,html.Div([

                                html.Label(children=['Estado Físico: ']),
                                html.Hr(),
                                dcc.Dropdown(id='estadof',
                                options=[{'label':str(b),'value':b} for b in sorted(df['estado_fisico'].unique())],
                                value=[b for b in sorted(df['estado_fisico'].unique())], multi = False
                                ,loading_state={"component_name":"estado_fisico"} )
                            ],className="estadof")
                            ,html.Div([

                                html.Label(children=['Habito Crecimiento: ']),
                                html.Hr(),
                                dcc.Dropdown(id='habito',
                                options=[{'label':str(b),'value':b} for b in sorted(df['habito_crecimiento'].unique())],
                                value=[b for b in sorted(df['habito_crecimiento'].unique())], multi = False
                                ,loading_state={"component_name":"habito_crecimiento"} )
                            ],className="habito_crecimiento")
                            


                    ],className="selectores")

                        ,
                             html.Button([ "Predecir"

                            ],type="button",className="btn btn-light btn-outline-primary button1",id="predecir")

                            , html.A([ "Restablecer"
                                
                            ],className="btn btn-light btn-outline-success  button2", href="/model")

            ],className="formulario2")


        ],className="contenedor7")




@callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='af', component_property='value'),
    Input(component_id='dn', component_property='value'),
    Input(component_id='rd', component_property='value'),
    Input(component_id='bb', component_property='value'),
    Input(component_id='i', component_property='value'),
    Input(component_id='h', component_property='value'),
    Input(component_id='a', component_property='value'),
    Input(component_id='pl', component_property='value'),
    Input(component_id='e', component_property='value'),
    Input(component_id='ep', component_property='value'),
    Input(component_id='oo', component_property='value'),
    Input(component_id='re', component_property='value'),
    Input(component_id='rh', component_property='value'),
    Input(component_id='ra', component_property='value'),
    Input(component_id='oa', component_property='value'),
    Input(component_id='est', component_property='value'),
    Input(component_id='iv', component_property='value'),
    Input(component_id='rt', component_property='value'),
    Input(component_id='rg', component_property='value'),
    Input(component_id='ap', component_property='value'),
    Input(component_id='v', component_property='value'),
    Input(component_id='cr', component_property='value'),
    Input(component_id='ce', component_property='value'),
    Input(component_id='comuna', component_property='value'),
    Input(component_id='ncomun', component_property='value'),
    Input(component_id='densidad', component_property='value'),
    Input(component_id='emplazamiento', component_property='value'),
    Input(component_id='estadof', component_property='value'),
    Input(component_id='habito', component_property='value'),
    Input(component_id='predecir', component_property='n_clicks')
)
def update_output_div(af,dn,rd,bb,i,h,a,pl,e,ep,oo,re,rh,ra,oa,est,iv,rt,rg,ap,v,cr,ce,comuna,ncomun,densidad,emplazamiento,estadof,habito,boton):
    if str(boton) != "None":

        prepared_data=prepare_random_forest_data(af, dn,rd,bb,i,h,a,pl,e,ep,oo,
                                re,rh,ra,oa,est,iv,rt,rg,ap,v,cr,ce,
                               ncomun,densidad,comuna,emplazamiento,estadof,habito)
        #print(prepared_data.shape[1])
        if prepared_data.shape[1]==133:

            loaded_model = load_random_forest_model()
        
            prediction = loaded_model.predict(prepared_data)

            salida= f'Su árbol esta: \n{prediction[0]}'
        else:
            salida = "Falto seleccionar alguna opción, intenta de nuevo!"
    elif str(boton)=="":
        salida=""
    else:
        salida=""
    return  salida

@callback(
    Output("modal-fs", "is_open"),
    Input("open-fs", "n_clicks"),
    State("modal-fs", "is_open"),
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open