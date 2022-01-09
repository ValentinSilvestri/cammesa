import os
import re
import pymongo
import pandas as pd
import numpy as np
import streamlit as st
from bokeh.plotting import figure
from bokeh.palettes import Set1_9


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def get_caudales():
    """Function to obtain the rivers basin flows from MongoDB Atlas.

    Returns:
        DataFrame: Pandas DataFrame with the query result.
    """

    st.spinner("Obteniendo los datos de caudales...")
    client = pymongo.MongoClient(os.environ['MONGO'])
    try:
        collection_name = client['publicaciones-especiales']['cuencas-datos-hidraulicos']
        project={
            '_id': 0,
            'fecha': 1,
            'situacionCuencaComahue': {
                'Caudal Collon Cura': 1,
                'Caudal Neuquen': 1,
                'Caudal Limay': 1,
                'Caudal Río Negro': 1,
                'Caudal Limay despues desembocadura de Collon Cura': 1
            },
            'situacionYacyretaSaltoGrande': {
                'Caudal Río Uruguay': 1,
                'Caudal Río Paraná': 1
            },
            'situacionCuencaPatagonica': {
                'Caudal Río Chubut': 1,
                'Caudal Río Futaleufu': 1
            },
            'situacionCuencaRioGrande': {
                'Caudal Río Grande': 1
            },
            'situacionCuencaRioSanJuan': {
                'Caudal Inicial Río San Juan': 1,
                'Caudal Final Río San Juan': 1
            }
        }
        df = pd.DataFrame(collection_name.find(projection=project))
        return df
    except Exception as e:
        st.error(f'Opps, algo fallo\n{e}')
    finally:
        client.close()


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def get_cotas():
    """Function to obtai the rivers basin levels from MongoDB Atlas.

    Returns:
        DataFrame: Pandas DataFrame with the query result.
    """
    st.spinner("Obteniendo los datos de cotas...")
    client = pymongo.MongoClient(os.environ['MONGO'])
    try:
        collection_name = client['publicaciones-especiales']['cuencas-datos-hidraulicos']
        project={
            '_id': 0, 
            'fecha': 1, 
            'situacionCuencaComahue': {
                'Cota Hoy Alicura': 1,
                'Cota Min Alicura': 1,
                'Cota Max Alicura': 1,
                'Cota Hoy Mari Menuco': 1,
                'Cota Min Mari Menuco': 1,
                'Cota Max Mari Menuco': 1, 
                'Cota Hoy Piedra del Aguila': 1,
                'Cota Min Piedra del Aguila': 1,
                'Cota Max Piedra del Aguila': 1, 
                'Cota Hoy Planicie Banderita Barreales': 1, 
                'Cota Min Planicie Banderita Barreales': 1, 
                'Cota Max Planicie Banderita Barreales': 1, 
                'Cota Hoy Arroyito': 1,
                'Cota Min Arroyito': 1,
                'Cota Max Arroyito': 1,
                'Cota Hoy El Chocon': 1,
                'Cota Min El Chocon': 1,
                'Cota Max El Chocon': 1,
                'Cota Hoy P': {
                    'P': {
                        'Leufu': 1
                    }
                }
            }, 
            'situacionYacyretaSaltoGrande': {
                'Cota Hoy Yacyreta': 1, 
                'Cota Min Yacyreta': 1, 
                'Cota Max Yacyreta': 1,
                'Cota Hoy Salto Grande': 1,
                'Cota Min Salto Grande': 1,
                'Cota Max Salto Grande': 1
            }, 
            'situacionCuencaPatagonica': {
                'Cota Hoy Futaleufu': 1, 
                'Cota Min Futaleufu': 1, 
                'Cota Max Futaleufu': 1, 
                'Cota Hoy Ameghino': 1,
                'Cota Min Ameghino': 1,
                'Cota Max Ameghino': 1
            }, 
            'situacionCuencaRioGrande': {
                'Cota Hoy Río Grande': 1,
                'Cota Min Río Grande': 1,
                'Cota Max Río Grande': 1
            }, 
            'situacionCuencaRioSanJuan': {
                'Cota Hoy Quebrada de Ullum': 1, 
                'Cota Min Quebrada de Ullum': 1, 
                'Cota Max Quebrada de Ullum': 1, 
                'Cota Hoy Los Caracole': 1,
                'Cota Min  Los Caracoles': 1,
                'Cota Max  Los Caracoles': 1,
                'Cota Hoy Punta Negra': 1,
                'Cota Min Punta Negra': 1,
                'Cota Max Punta Negra': 1
            }
        }

        df = pd.DataFrame(collection_name.find(projection=project))
        return df
    except Exception as e:
        st.error(f'Opps, algo fallo\n{e}')
    finally:
        client.close()


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def get_turbinado():
    """Function to obtain the rivers basin turbinate from MongoDB Atlas.

    Returns:
        DataFrame: Pandas DataFrame with the query result.
    """
    st.spinner("Obteniendo los datos de turbinado...")
    client = pymongo.MongoClient(os.environ['MONGO'])
    try:
        collection_name = client['publicaciones-especiales']['cuencas-datos-hidraulicos']
        project={
            '_id': 0, 
            'fecha': 1, 
            'situacionCuencaComahue': {
                'Turbinado Alicura': 1,
                'Turbinado Piedra del Aguila': 1,
                'Turbinado Arroyito': 1,
                'Turbinado El Chocon': 1,
                'Turbinado Mari Menuco': 1,
                'Turbinado P': {
                    'P': {
                        'Leufu': 1
                    }
                }
            },
            'situacionYacyretaSaltoGrande': {
                'Turbinado Salto Grande': 1, 
                'Turbinado Yacyreta': 1
            },
            'situacionCuencaPatagonica': {
                'Turbinado Futaleufu': 1, 
                'Turbinado Ameghino': 1
            }, 
            'situacionCuencaRioGrande': {
                'Turbinado Río Grande': 1
            }, 
            'situacionCuencaRioSanJuan': {
                'Turbinado Punta Negra': 1, 
                'Turbinado Ullum': 1, 
                'Turbinado Los Caracoles': 1, 
                'Turbinado Quebrada de Ullum': 1
            }
        }

        df = pd.DataFrame(collection_name.find(projection=project))
        return df
    except Exception as e:
        st.error(f'Opps, algo fallo\n{e}')
    finally:
        client.close()


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def get_vertido():
    """Function to obtain the rivers basin discharge from MongoDB Atlas.

    Returns:
        DataFrame: Pandas DataFrame with the query result.
    """
    st.spinner("Obteniendo los datos de turbinado...")
    client = pymongo.MongoClient(os.environ['MONGO'])
    try:
        collection_name = client['publicaciones-especiales']['cuencas-datos-hidraulicos']
        project={
            '_id': 0, 
            'fecha': 1, 
            'situacionCuencaComahue': {
                'Vertido El Chañar': 1,
                'Vertido Arroyito': 1,
                'Vertido Piedra del Aguila': 1,
                'Vertido P': {
                    'P': {
                        'Leufu': 1
                    }
                }
            },
            'situacionYacyretaSaltoGrande': {
                'Vertido Salto Grande': 1, 
                'Vertido Yacyreta': 1
            },
            'situacionCuencaPatagonica': {
                'Vertido Futaleufu': 1, 
                'Vertido Ameghino': 1
            }, 
            'situacionCuencaRioGrande': {
                'Bombeo Río Grande': 1
            }, 
            'situacionCuencaRioSanJuan': {
                'Vertido Punta Negra': 1, 
                'Vertido Los Caracoles': 1, 
                'Vertido Quebrada de Ullum': 1
            }
        }

        df = pd.DataFrame(collection_name.find(projection=project))
        return df
    except Exception as e:
        st.error(f'Opps, algo fallo\n{e}')
    finally:
        client.close()


def caudales():
    """Get the rivers basin flows and process this data.

    Returns:
        Figure: Bokeh plotting figure.
        DataFrame: Pandas DataFrame with the query result.
    """
    df = get_caudales()
    df = pd.concat([
        df['fecha'],
        pd.json_normalize(df['situacionCuencaComahue']),
        pd.json_normalize(df['situacionYacyretaSaltoGrande']),
        pd.json_normalize(df['situacionCuencaPatagonica']),
        pd.json_normalize(df['situacionCuencaRioGrande']),
        pd.json_normalize(df['situacionCuencaRioSanJuan'])
    ], axis=1, join="inner")

    df.rename(columns={
        "fecha": "Fecha",
        "Caudal Collon Cura": "Cuenca Comahue - Caudal Collon Cura",
        "Caudal Neuquen": "Cuenca Comahue - Caudal Neuquen",
        "Caudal Limay": "Cuenca Comahue - Caudal Limay",
        "Caudal Río Negro": "Cuenca Comahue - Caudal Río Negro",
        "Caudal Limay despues desembocadura de Collon Cura": "Cuenca Comahue - Caudal Limay despues desembocadura de Collon Cura",
        "Caudal Río Uruguay": "Yacyreta Salto Grande - Caudal Río Uruguay",
        "Caudal Río Paraná": "Yacyreta Salto Grande - Caudal Río Paraná",
        "Caudal Río Chubut": "Cuenca Patagónica - Caudal Río Chubut",
        "Caudal Río Futaleufu": "Cuenca Patagónica - Caudal Río Futaleufu",
        "Caudal Río Grande": "Cuenca Río Grande - Caudal Río Grande",
        "Caudal Inicial Río San Juan": "Cuenca Río San Juan - Caudal Inicial Río San Juan",
        "Caudal Final Río San Juan": "Cuenca Río San Juan - Caudal Final Río San Juan"
    }, inplace=True)

    df['Fecha'] =  pd.to_datetime(df['Fecha'], format='%Y/%m/%d').dt.date
    df = df.drop_duplicates().sort_values('Fecha').reset_index(drop=True)
    df = df.replace(0, np.nan)
    p = figure(x_axis_type="datetime", title="Caudales cuencas", sizing_mode="stretch_both")
    p.grid.grid_line_alpha=0.3
    p.xaxis.axis_label = 'Fecha'
    p.yaxis.axis_label = 'Caudal [m\u00b3/s]'
    p.legend.location = "top_left"

    return p, df


def cotas():
    """Get the rivers basin levels and process this data.

    Returns:
        Figure: Bokeh plotting figure.
        DataFrame: Pandas DataFrame with the query result.
    """
    df = get_cotas()
    df = pd.concat([
        df['fecha'],
        pd.json_normalize(df['situacionCuencaComahue']),
        pd.json_normalize(df['situacionYacyretaSaltoGrande']),
        pd.json_normalize(df['situacionCuencaPatagonica']),
        pd.json_normalize(df['situacionCuencaRioGrande']),
        pd.json_normalize(df['situacionCuencaRioSanJuan'])
    ], axis=1, join="inner")

    df.rename(columns={
        'fecha': 'Fecha',
        'Cota Hoy Alicura': 'Cuenca Comahue - Alicura',
        'Cota Min Alicura': 'Cuenca Comahue - Min Alicura',
        'Cota Max Alicura': 'Cuenca Comahue - Max Alicura',
        'Cota Hoy Piedra del Aguila': 'Cuenca Comahue - Piedra del Aguil',
        'Cota Min Piedra del Aguila': 'Cuenca Comahue - Min Piedra del Aguila',
        'Cota Max Piedra del Aguila': 'Cuenca Comahue - Max Piedra del Aguila',
        'Cota Hoy Arroyito': 'Cuenca Comahue - Arroyito',
        'Cota Min Arroyito': 'Cuenca Comahue - Min Arroyito',
        'Cota Max Arroyito': 'Cuenca Comahue - Max Arroyito',
        'Cota Hoy Mari Menuco': 'Cuenca Comahue - Mari Menuco',
        'Cota Min Mari Menuco': 'Cuenca Comahue - Min Mari Menuco',
        'Cota Max Mari Menuco': 'Cuenca Comahue - Max Mari Menuco',
        'Cota Hoy Planicie Banderita Barreales': 'Cuenca Comahue - Planicie Banderita Barreales',
        'Cota Min Planicie Banderita Barreales': 'Cuenca Comahue - Min Planicie Banderita Barreales',
        'Cota Max Planicie Banderita Barreales': 'Cuenca Comahue - Max Planicie Banderita Barreales',
        'Cota Hoy El Chocon': 'Cuenca Comahue - El Chocon',
        'Cota Min El Chocon': 'Cuenca Comahue - Min El Chocon',
        'Cota Max El Chocon': 'Cuenca Comahue - Max El Chocon',
        'Cota Hoy P.P.Leufu': 'Cuenca Comahue - Leufu',
        'Cota Hoy Yacyreta': 'Cuenca Yacyreta - Yacyreta',
        'Cota Min Yacyreta': 'Cuenca Yacyreta - Min Yacyreta',
        'Cota Max Yacyreta': 'Cuenca Yacyreta - Max Yacyreta',
        'Cota Hoy Salto Grande': 'Cuenca Yacyreta - Salto Grande',
        'Cota Min Salto Grande': 'Cuenca Yacyreta - Min Salto Grande',
        'Cota Max Salto Grande': 'Cuenca Yacyreta - Max Salto Grande',
        'Cota Hoy Futaleufu': 'Cuenca Patagónica - Futaleufu',
        'Cota Min Futaleufu': 'Cuenca Patagónica - Min Futaleufu',
        'Cota Max Futaleufu': 'Cuenca Patagónica - Max Futaleufu',
        'Cota Hoy Ameghino': 'Cuenca Patagónica - Ameghino',
        'Cota Min Ameghino': 'Cuenca Patagónica - Min Ameghino',
        'Cota Max Ameghino': 'Cuenca Patagónica - Max Ameghino',
        'Cota Hoy Río Grande': 'Cuenca Río Grande - Río Grande',
        'Cota Min Río Grande': 'Cuenca Río Grande - Min Río Grande',
        'Cota Max Río Grande': 'Cuenca Río Grande - Max Río Grande',
        'Cota Hoy Quebrada de Ullum': 'Cuenca Río San Juan - Quebrada de Ullum',
        'Cota Min Quebrada de Ullum': 'Cuenca Río San Juan - Min Quebrada de Ullum',
        'Cota Max Quebrada de Ullum': 'Cuenca Río San Juan - Max Quebrada de Ullum',
        'Cota Hoy Punta Negra': 'Cuenca Río San Juan - Punta Negra',
        'Cota Min Punta Negra': 'Cuenca Río San Juan - Min Punta Negra',
        'Cota Max Punta Negra': 'Cuenca Río San Juan - Max Punta Negra'
    }, inplace=True)

    df['Fecha'] =  pd.to_datetime(df['Fecha'], format='%Y/%m/%d').dt.date
    df = df.drop_duplicates().sort_values('Fecha').reset_index(drop=True)
    df = df.replace(0, np.nan)
    p = figure(x_axis_type="datetime", title="Cotas cuencas", sizing_mode="stretch_both")
    p.grid.grid_line_alpha=0.3
    p.xaxis.axis_label = 'Fecha'
    p.yaxis.axis_label = 'Cota [cm]'

    p.legend.location = "top_left"

    return p, df


def turbinado():
    """Get the rivers basin discharge and process this data.

    Returns:
        Figure: Bokeh plotting figure.
        DataFrame: Pandas DataFrame with the query result.
    """
    df = get_turbinado()
    df = pd.concat([
        df['fecha'],
        pd.json_normalize(df['situacionCuencaComahue']),
        pd.json_normalize(df['situacionYacyretaSaltoGrande']),
        pd.json_normalize(df['situacionCuencaPatagonica']),
        pd.json_normalize(df['situacionCuencaRioGrande']),
        pd.json_normalize(df['situacionCuencaRioSanJuan'])
    ], axis=1, join="inner")

    df.rename(columns={
        'fecha': 'Fecha',
        'Turbinado Alicura': 'Cuenca Comahue - Alicura',
        'Turbinado Piedra del Aguila': 'Cuenca Comahue - Piedra del Aguila',
        'Turbinado Arroyito': 'Cuenca Comahue - Arroyito',
        'Turbinado El Chocon': 'Cuenca Comahue - El Chocon',
        'Turbinado Mari Menuco': 'Cuenca Comahue - Mari Menuco',
        'Turbinado P.P.Leufu': 'Cuenca Comahue - Leufu',
        'Turbinado Salto Grande': 'Cuenca Yacyreta - Salto Grande',
        'Turbinado Yacyreta': 'Cuenca Yacyreta - Yacyreta',
        'Turbinado Futaleufu': 'Cuenca Patagónica - Futaleufu',
        'Turbinado Ameghino': 'Cuenca Patagónica - Ameghino',
        'Turbinado Río Grande': 'Cuenca Río Grande - Río Grande',
        'Turbinado Punta Negra': 'Cuenca Río San Juan - Punta Negra',
        'Turbinado Ullum': 'Cuenca Río San Juan - Ullum',
        'Turbinado Los Caracoles': 'Cuenca Río San Juan - Los Caracoles',
        'Turbinado Quebrada de Ullum': 'Cuenca Río San Juan - Quebrada de Ullum'
    }, inplace=True)

    df['Fecha'] =  pd.to_datetime(df['Fecha'], format='%Y/%m/%d').dt.date
    df = df.drop_duplicates().sort_values('Fecha').reset_index(drop=True)
    # df = df.replace(0, np.nan)
    p = figure(x_axis_type="datetime", title="Turbinado", sizing_mode="stretch_both")
    p.grid.grid_line_alpha=0.3
    p.xaxis.axis_label = 'Fecha'
    p.yaxis.axis_label = 'Turbinado'
    p.legend.location = "top_left"

    return p, df


def vertido():
    """Get the rivers basin discharge and process this data.

    Returns:
        Figure: Bokeh plotting figure.

        DataFrame: Pandas DataFrame with the query result.
    """
    df = get_vertido()
    df = pd.concat([
        df['fecha'],
        pd.json_normalize(df['situacionCuencaComahue']),
        pd.json_normalize(df['situacionYacyretaSaltoGrande']),
        pd.json_normalize(df['situacionCuencaPatagonica']),
        pd.json_normalize(df['situacionCuencaRioGrande']),
        pd.json_normalize(df['situacionCuencaRioSanJuan'])
    ], axis=1, join="inner")

    df.rename(columns={
        'fecha': 'Fecha',
        'Vertido El Chañar': 'Cuenca Comahue - El Chañar',
        'Vertido Arroyito': 'Cuenca Comahue - Arroyito',
        'Vertido Piedra del Aguila': 'Cuenca Comahue - Piedra del Aguila',
        'Vertido P.P.Leufu': 'Cuenca Comahue - Leufu',
        'Vertido Salto Grande': 'Cuenca Yacyreta - Salto Grande',
        'Vertido Yacyreta': 'Cuenca Yacyreta - Yacyreta',
        'Vertido Futaleufu': 'Cuenca Patagónica - Futaleufu',
        'Vertido Ameghino': 'Cuenca Patagónica - Ameghino',
        'Bombeo Río Grande': 'Cuenca Río Grande - Bombeo Río Grande',
        'Vertido Punta Negra': 'Cuenca Río San Juan - Punta Negra',
        'Vertido Los Caracoles': 'Cuenca Río San Juan - Los Caracoles',
        'Vertido Quebrada de Ullum': 'Cuenca Río San Juan - Quebrada de Ullum'
    }, inplace=True)

    df['Fecha'] =  pd.to_datetime(df['Fecha'], format='%Y/%m/%d').dt.date
    df = df.drop_duplicates().sort_values('Fecha').reset_index(drop=True)
    # df = df.replace(0, np.nan)
    p = figure(x_axis_type="datetime", title="Vertido", sizing_mode="stretch_both")
    p.grid.grid_line_alpha=0.3
    p.xaxis.axis_label = 'Fecha'
    p.yaxis.axis_label = 'Vertido'
    p.legend.location = "top_left"

    return p, df


def write():
    """Function to write the Streamlit content of the page pe_cuencas
    """
    p_caudales, df_caudales = caudales()
    p_cotas, df_cotas = cotas()
    p_turbinado, df_turbinado = turbinado()
    p_vertido, df_vertido = vertido()

    st.title("Cammesa API data", anchor=None)
    st.header("Publicaciones especiales - Cuencas/Datos Hidráulicos :+1:", anchor=None)

    with st.container():
        st.subheader("Análisis de caudales", anchor=None)
        options = st.multiselect(
            "Seleccionar datos a graficar.",
            options=[
                "Cuenca Comahue - Caudal Collon Cura",
                "Cuenca Comahue - Caudal Neuquen",
                "Cuenca Comahue - Caudal Limay",
                "Cuenca Comahue - Caudal Río Negro",
                "Cuenca Comahue - Caudal Limay despues desembocadura de Collon Cura",
                "Yacyreta Salto Grande - Caudal Río Uruguay",
                "Yacyreta Salto Grande - Caudal Río Paraná",
                "Cuenca Patagónica - Caudal Río Chubut",
                "Cuenca Patagónica - Caudal Río Futaleufu",
                "Cuenca Río Grande - Caudal Río Grande",
                "Cuenca Río San Juan - Caudal Inicial Río San Juan",
                "Cuenca Río San Juan - Caudal Final Río San Juan"
            ],
            default=[
                "Yacyreta Salto Grande - Caudal Río Paraná",
                "Yacyreta Salto Grande - Caudal Río Uruguay"
            ]
        )
        for index, value in enumerate(options):
            p_caudales.line(
                df_caudales['Fecha'],
                df_caudales[value],
                color=Set1_9[index],
                legend_label=re.split(r" - ", value)[1].strip()
            )
        st.bokeh_chart(p_caudales)

        with st.expander("Ver datos"):
            st.write("Datos de los caudales de las cuencas en [m\u00b3/s].")
            st.dataframe(df_caudales)
            st.download_button(
                label="Descargar dataset como .CSV",
                data=df_caudales.to_csv(index=False).encode('utf-8'),
                file_name='Caudales.csv',
                mime='text/csv',
            )

    with st.container():
        st.subheader("Análisis de cotas", anchor=None)
        options_cotas = st.multiselect(
            "Seleccionar datos a graficar.",
            options=[
                'Cuenca Comahue - Alicura',
                'Cuenca Comahue - Min Alicura',
                'Cuenca Comahue - Max Alicura',
                'Cuenca Comahue - Piedra del Aguil',
                'Cuenca Comahue - Min Piedra del Aguila',
                'Cuenca Comahue - Max Piedra del Aguila',
                'Cuenca Comahue - Arroyito',
                'Cuenca Comahue - Min Arroyito',
                'Cuenca Comahue - Max Arroyito',
                'Cuenca Comahue - Mari Menuco',
                'Cuenca Comahue - Min Mari Menuco',
                'Cuenca Comahue - Max Mari Menuco',
                'Cuenca Comahue - Planicie Banderita Barreales',
                'Cuenca Comahue - Min Planicie Banderita Barreales',
                'Cuenca Comahue - Max Planicie Banderita Barreales',
                'Cuenca Comahue - El Chocon',
                'Cuenca Comahue - Min El Chocon',
                'Cuenca Comahue - Max El Chocon',
                'Cuenca Comahue - Leufu',
                'Cuenca Yacyreta - Yacyreta',
                'Cuenca Yacyreta - Min Yacyreta',
                'Cuenca Yacyreta - Max Yacyreta',
                'Cuenca Yacyreta - Salto Grande',
                'Cuenca Yacyreta - Min Salto Grande',
                'Cuenca Yacyreta - Max Salto Grande',
                'Cuenca Patagónica - Futaleufu',
                'Cuenca Patagónica - Min Futaleufu',
                'Cuenca Patagónica - Max Futaleufu',
                'Cuenca Patagónica - Ameghino',
                'Cuenca Patagónica - Min Ameghino',
                'Cuenca Patagónica - Max Ameghino',
                'Cuenca Río Grande - Río Grande',
                'Cuenca Río Grande - Min Río Grande',
                'Cuenca Río Grande - Max Río Grande',
                'Cuenca Río San Juan - Quebrada de Ullum',
                'Cuenca Río San Juan - Min Quebrada de Ullum',
                'Cuenca Río San Juan - Max Quebrada de Ullum',
                'Cuenca Río San Juan - Punta Negra',
                'Cuenca Río San Juan - Min Punta Negra',
                'Cuenca Río San Juan - Max Punta Negra'
            ],
            default=[
                'Cuenca Yacyreta - Salto Grande',
                'Cuenca Yacyreta - Min Salto Grande',
                'Cuenca Yacyreta - Max Salto Grande'
            ]
        )
        for index, value in enumerate(options_cotas):
            p_cotas.line(
                df_cotas['Fecha'],
                df_cotas[value],
                color=Set1_9[index],
                legend_label=re.split(r" - ", value)[1].strip()
            )
        st.bokeh_chart(p_cotas)
        with st.expander("Ver datos"):
            st.write("Datos de los Cotas de las cuencas en [cm].")
            st.dataframe(df_cotas)
            st.download_button(
                label="Descargar dataset como .CSV",
                data=df_cotas.to_csv(index=False).encode('utf-8'),
                file_name='Cotas.csv',
                mime='text/csv',
            )

    with st.container():
        st.subheader("Análisis del turbinado", anchor=None)
        options_turbinado = st.multiselect(
            "Seleccionar datos a graficar.",
            options=[
                'Cuenca Comahue - Alicura',
                'Cuenca Comahue - Piedra del Aguila',
                'Cuenca Comahue - Arroyito',
                'Cuenca Comahue - El Chocon',
                'Cuenca Comahue - Mari Menuco',
                'Cuenca Comahue - Leufu',
                'Cuenca Yacyreta - Salto Grande',
                'Cuenca Yacyreta - Yacyreta',
                'Cuenca Patagónica - Futaleufu',
                'Cuenca Patagónica - Ameghino',
                'Cuenca Río Grande - Río Grande',
                'Cuenca Río San Juan - Punta Negra',
                'Cuenca Río San Juan - Ullum',
                'Cuenca Río San Juan - Los Caracoles',
                'Cuenca Río San Juan - Quebrada de Ullum'
            ], default=[
                'Cuenca Yacyreta - Yacyreta',
                'Cuenca Yacyreta - Salto Grande'
            ]
        )
        for index, value in enumerate(options_turbinado):
            p_turbinado.line(
                df_turbinado['Fecha'],
                df_turbinado[value],
                color=Set1_9[index],
                legend_label=re.split(r" - ", value)[1].strip()
            )
        st.bokeh_chart(p_turbinado)
        with st.expander("Ver datos"):
            st.write("Datos del turbinado.")
            st.dataframe(df_turbinado)
            st.download_button(
                label="Descargar dataset como .CSV",
                data=df_turbinado.to_csv(index=False).encode('utf-8'),
                file_name='Turbinado.csv',
                mime='text/csv',
            )

    with st.container():
        st.subheader("Análisis del vertido", anchor=None)
        options_vertido = st.multiselect(
            "Seleccionar datos a graficar.",
            options=[
                'Cuenca Comahue - El Chañar',
                'Cuenca Comahue - Arroyito',
                'Cuenca Comahue - Piedra del Aguila',
                'Cuenca Comahue - Leufu',
                'Cuenca Yacyreta - Salto Grande',
                'Cuenca Yacyreta - Yacyreta',
                'Cuenca Patagónica - Futaleufu',
                'Cuenca Patagónica - Ameghino',
                'Cuenca Río Grande - Bombeo Río Grande',
                'Cuenca Río San Juan - Punta Negra',
                'Cuenca Río San Juan - Los Caracoles',
                'Cuenca Río San Juan - Quebrada de Ullum'
            ], default=[
                'Cuenca Yacyreta - Yacyreta',
                'Cuenca Yacyreta - Salto Grande'
            ]
        )
        for index, value in enumerate(options_vertido):
            p_vertido.line(
                df_vertido['Fecha'],
                df_vertido[value],
                color=Set1_9[index],
                legend_label=re.split(r" - ", value)[1].strip()
            )
        st.bokeh_chart(p_vertido)
        
        with st.expander("Ver datos"):
            st.write("Datos del vertido.")
            st.dataframe(df_vertido)
            st.download_button(
                label="Descargar dataset como .CSV",
                data=df_vertido.to_csv(index=False).encode('utf-8'),
                file_name='Vertido.csv',
                mime='text/csv',
            )
