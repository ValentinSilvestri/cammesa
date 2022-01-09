import streamlit as st
import src.pages.dg_agentes
import src.pages.dg_estaciones_transf
import src.pages.dg_consumo_gas
import src.pages.dg_generacion
import src.pages.p_catalogos
import src.pages.pe_cuencas
import src.pages.pe_perturbaciones
import src.pages.pe_cubrimiento_pico
import src.pages.pe_costo_marginal
import src.pages.pe_precios_mercado

PAGES = {
    # demanda-generacion
    "Agentes": src.pages.dg_agentes,
    "Estaciones transformadoras": src.pages.dg_estaciones_transf,
    "Consumo de gas": src.pages.dg_consumo_gas,
    "Generación por región": src.pages.dg_generacion,
    # publicaciones
    "Catálogos": src.pages.p_catalogos,
    # publicaciones-especiales
    "Cuencas - Hidráulica": src.pages.pe_cuencas,
    "Perturbaciones": src.pages.pe_perturbaciones,
    "Cubrimiento pico": src.pages.pe_cubrimiento_pico,
    "Costo marginal": src.pages.pe_costo_marginal,
    "Precios de mercado": src.pages.pe_precios_mercado,
}


def main():
    st.set_page_config(
        page_title="CAMMESA - Data Visualization",
        page_icon="⚡️",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://github.com/ValentinSilvestri/cammesa',
            'Report a bug': "https://github.com/ValentinSilvestri/cammesa/issues",
            'About': "# Análisis explotario de los datos de CAMMESA. Realizado por [@ValentinSilvestri](https://github.com/ValentinSilvestri)."
        }
    )
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()), index=5, help="Seleccione una página.")

    page = PAGES[selection]

    with st.spinner(f"Cargando {selection} ..."):
        page.write()

    st.sidebar.title("Contribute")
    st.sidebar.info(
        "This an open source project and you are very welcome to **contribute** your "
        "comments, questions, resources and apps as "
        "[issues](https://github.com/ValentinSilvestri/cammesa/issues) or "
        "[pull requests](https://github.com/ValentinSilvestri/cammesa/pulls) "
        "to the [source code](https://github.com/ValentinSilvestri/cammesa). "
    )
    st.sidebar.title("About")
    st.sidebar.info(
        """
        This app is maintained by Valentín Silvestri. You can learn more about me at
        *[@ValentinSilvestri](https://www.linkedin.com/in/valentinsilvestri/)*.
    """
    )

if __name__ == "__main__":
    main()