import os
import pymongo
import pandas as pd
import streamlit as st
from bokeh.palettes import Set1_9
from bokeh.plotting import figure
from bokeh.layouts import column
from utils import endpoints as ed


def get_regiones():
    """Function to obtain the regions from MongoDB Atlas.

    Returns:
        DataFrame: Pandas DataFrame with the query result.
    """
    response = ed.DemandaGeneracion.RegionesDemanda()
    if response:
        return pd.json_normalize(response.json())
    else:
        client = pymongo.MongoClient(os.environ['MONGO'])
        try:
            collection_name = client['demanda-generacion']['regiones-demanda']
            project={
                '_id': 0,
            }
            return pd.DataFrame(collection_name.find(projection=project))
        except Exception as e:
            pass
        finally:
            client.close()


def write():
    """Function to write the Streamlit content of the page dg_demanda
    """
    df = get_regiones()

    st.header("Demanda y Generación ⚡️", anchor=None)

    with st.container():
        st.subheader("Análisis de la demanda por región", anchor=None)

        regiones = df['nombre'].unique().tolist()

        region = st.radio(
            "Seleccionar las regiones a graficar.",
            options=regiones,
            index=len(regiones)-1
        )

        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

        response = ed.DemandaGeneracion.ObtieneDemandaYTemperaturaRegion(df[df['nombre'] == region]['id'].max())
        if response:
            df_demanda = pd.json_normalize(response.json())
            df_demanda['fecha'] = pd.to_datetime(df_demanda['fecha']).dt.tz_localize(None)
        else:
            print('Error.')

        p1 = figure(x_axis_type="datetime", title="Demanda por región", sizing_mode="stretch_both")
        p1.grid.grid_line_alpha=0.3
        p1.xaxis.axis_label = 'Hora'
        p1.yaxis.axis_label = 'Demanda [MW]'
        p1.legend.location = "top_left"

        dem = ['demHoy', 'demAyer', 'demSemanaAnt']

        for index, day in enumerate(dem):
            p1.line(
                df_demanda['fecha'],
                df_demanda[day],
                color=Set1_9[index],
                legend_label=f'{region} - {day}',
                muted_color=Set1_9[index],
                muted_alpha=0.2,
                line_width=2,
                alpha=0.8
            )
        p1.legend.background_fill_alpha = 0
        p1.legend.click_policy="mute"
        p1.legend.background_fill_alpha = 0.0

        if 'tempHoy' in df_demanda.columns:

            temp = ['tempHoy', 'tempAyer', 'tempSemanaAnt']
            p2 = figure(x_axis_type="datetime", title="Temperatura por región", sizing_mode="stretch_both")
            p2.grid.grid_line_alpha=0.3
            p2.xaxis.axis_label = 'Hora'
            p2.yaxis.axis_label = 'Temperatura [ºC]'
            p2.legend.location = "top_left"

            for index, day in enumerate(temp):
                p2.line(
                    df_demanda.dropna(subset = [day])['fecha'],
                    df_demanda.dropna(subset = [day])[day],
                    color=Set1_9[index],
                    legend_label=f'{region} - {day}',
                    muted_color=Set1_9[index],
                    muted_alpha=0.2,
                    line_width=2,
                    alpha=0.8
                )
            p2.scatter(
                df_demanda.dropna(subset = ['tempPrevista'])['fecha'],
                df_demanda.dropna(subset = ['tempPrevista'])['tempPrevista'],
                color='#000003',
                legend_label=f'{region} - Previsto',
                muted_color='#000003',
                muted_alpha=0.2,
                marker='x',
                size=20,
                alpha=0.8
            )
            p2.legend.background_fill_alpha = 0
            p2.legend.click_policy="mute"
            p2.legend.background_fill_alpha = 0.0

            p = column(p1, p2, sizing_mode='stretch_both')
            st.bokeh_chart(p)
        else:
            st.bokeh_chart(p1)
