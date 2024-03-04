# import numpy as np
# import pandas as pd
import streamlit as st
# import matplotlib.pyplot as plt
# import seaborn as sns
import tabula
import pages as pg
from home_page import show_home_page
from prediction_page import show_prediction_page
from etoo_bot import show_etoobot_page
from components.components import custom_header

# Estilos  ###################################################################################

style_width = """
    <style>
        .appview-container  .main  .block-container{
            max-width: 60%;
        }
    </style>
    """
st.markdown(style_width, unsafe_allow_html=True)

### Cabecera  ##################################################################################

st.markdown(custom_header('Fraud Credit Card App'), unsafe_allow_html=True)
st.markdown("""<br>""", unsafe_allow_html=True)


### Sidebar  ##################################################################################

# with st.sidebar:
#     st.header('Menú Principal')
#     st.session_state['page'] = st.selectbox(
#         'Elige una opción:',
#         ('Inicio', 'Análisis Exploratorio', 'Modelo', 'Predicción'),
#         key='page_selector'
#     )

def main():

    st.write(tabula.environment_info())
    # Inicialización de 'page' en st.session_state
    if 'page' not in st.session_state:
        st.session_state['page'] = 'Inicio'
    
    # Inicialización de 'df' en st.session_state
    if 'df' not in st.session_state:
        st.session_state['df'] = None

    # Sidebar para selección de página
    with st.sidebar:
        st.header('Menú Principal')
        st.session_state['page'] = st.selectbox(
            'Elige una opción:',
            ('Inicio', 'Predicción', 'Análisis Exploratorio', 'Modelo', 'Eto\'o Bot'),
            key='page_selector'
        )

    # Contenido de la página de Inicio
    if st.session_state['page'] == 'Inicio':
        st.session_state['df'] = show_home_page()

    # Contenido de otras páginas
    elif st.session_state['page'] == 'Análisis Exploratorio':
        pg.show_analysis_page()
    elif st.session_state['page'] == 'Modelo':
        pg.show_model_page()

    # Contenido de la página de Predicción
    elif st.session_state['page'] == 'Predicción':
        if st.session_state['df'] is not None and not st.session_state['df'].empty:
            show_prediction_page(st.session_state['df'])
        else:
            st.error('Por favor, carga los datos en la página de Inicio primero.')

    # Contenido de la página de Eto'o Bot
    elif st.session_state['page'] == 'Eto\'o Bot':
        if st.session_state['df'] is not None and not st.session_state['df'].empty:
            show_etoobot_page()
        else:
            st.error('Por favor, carga los datos en la página de Inicio primero.')
    


    # Botón para cambiar a la página de Predicción
    if st.session_state['page'] not in ['Predicción', 'Análisis Exploratorio', 'Modelo', 'Eto\'o Bot']:
        if st.button('Genera Predicción'):
            st.session_state['page'] = 'Predicción'  # Esto debería actualizar el selectbox automáticamente
    



    # Mostrar en la página principal la opción seleccionada y el valor del slider
    st.write(f'Página actual: {st.session_state["page"]}')


if __name__ == "__main__":
    main()
