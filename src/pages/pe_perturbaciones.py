import os
import re
import datetime
import pymongo
import pandas as pd
import numpy as np
import streamlit as st
from bokeh.plotting import figure
from bokeh.palettes import Set1_9


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def get_perturbaciones():
    """Function to obtain the disturbances on the SADI from MongoDB Atlas.

    Returns:
        DataFrame: Pandas DataFrame with the query result.
    """

    st.spinner("Obteniendo los datos de perturbaciones en el SADI...")
    client = pymongo.MongoClient(os.environ['MONGO'])
    try:
        collection_name = client['publicaciones-especiales']['perturbaciones-sadi']
        project={
            '_id': 0,
        }
        df = pd.DataFrame(collection_name.find(projection=project))
        return df
    except Exception as e:
        st.error(f'Opps, algo fallo\n{e}')
    finally:
        client.close()


def perturbaciones():
    """Get the disturbances on the SADI and process this data.

    Returns:
        Figure: Bokeh plotting figure.
        DataFrame: Pandas DataFrame with the query result.
    """
    df = get_perturbaciones()

    df['fechaFalla'] = pd.to_datetime(df['fechaFalla'], format='%Y-%m-%d').dt.date
    df = df.drop_duplicates().sort_values('fechaFalla', ascending=False).reset_index(drop=True)

    p = figure(x_axis_type="datetime", title="Cantidad de perturbaciones en el SADI", sizing_mode="stretch_both")
    p.grid.grid_line_alpha=0.3
    p.xaxis.axis_label = 'Fecha'
    p.yaxis.axis_label = 'Perturbaciones'
    p.legend.location = "top_left"

    return p, df


def write():
    """Function to write the Streamlit content of the page pe_cuencas
    """
    p, df = perturbaciones()

    st.header("Publicaciones especiales - Perturbaciones SADI 🌊", anchor=None)

    with st.container():
        st.subheader("Análisis de perturbaciones", anchor=None)

        df_occ_total = df.groupby(['fechaFalla']).size().to_frame(name = 'size').reset_index()
        
        p.scatter(
            df_occ_total['fechaFalla'],
            df_occ_total['size'],
            legend_label='Total',
            size=10,
            color="navy",
            alpha=0.5,
            marker='x'
        )
        st.bokeh_chart(p)

        with st.expander("Ver datos"):
            st.write("Datos de las perturbaciones totales en el SADI.")
            st.dataframe(df)
            st.download_button(
                label="Descargar dataset como .CSV",
                data=df.to_csv(index=False).encode('utf-8'),
                file_name='Caudales.csv',
                mime='text/csv',
            )
        
        st.subheader("Apagón eléctrico de Argentina 2019", anchor=None)
        st.write("El apagón eléctrico de Argentina, Paraguay, Uruguay, Chile y Brasil de 2019 fue un conjunto de interrupciones del suministro de energía eléctrica producido el 16 de junio de 2019 que afectaron gran parte del territorio de dichos países. Aquí se pueden observar las perturbaciones registradas en el SADI ese día.")
        st.table(df[df['fechaFalla'] == datetime.datetime.strptime('2019-06-16', '%Y-%m-%d').date()][['tipo', 'descripcion']])