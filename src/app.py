import streamlit as st
import pages as pg
from home_page import show_home_page
from prediction_page import show_prediction_page
from etoo_bot import show_etoobot_page
from components.components import custom_header, custom_title, custom_width, custom_footer, description


# Configuración de la página ##################################################################

st.set_page_config(
    page_title="Fraud-Detect",
    page_icon="💳",
    initial_sidebar_state="expanded",  
)

st.markdown(custom_width(), unsafe_allow_html=True)




### Sidebar  ##################################################################################


def main():

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
        # st.session_state['df'] = show_home_page()
        show_home_page()

    # Contenido de la página de Predicción
    elif st.session_state['page'] == 'Predicción':
        # if st.session_state['df'] is not None and not st.session_state['df'].empty:
        #     show_prediction_page(st.session_state['df'])
        # else:
        #     st.error('Por favor, carga los datos en la página de Inicio primero.')
        if st.session_state.get('df') is not None and not st.session_state['df'].empty:
            show_prediction_page()  # Ahora accede a `st.session_state['df']` internamente
        else:
            st.error('Por favor, carga los datos en la página de Inicio primero.')

    # Contenido de otras páginas
    elif st.session_state['page'] == 'Análisis Exploratorio':
        pg.show_analysis_page()
    elif st.session_state['page'] == 'Modelo':
        pg.show_model_page()

    # Contenido de la página de Eto'o Bot
    elif st.session_state['page'] == 'Eto\'o Bot':
            show_etoobot_page()
    


    # Botón para cambiar a la página de Predicción
    if st.session_state['page'] not in ['Predicción', 'Análisis Exploratorio', 'Modelo', 'Eto\'o Bot']:
        if st.button('Genera Predicción'):
            st.session_state['page'] = 'Predicción'  # Esto debería actualizar el selectbox automáticamente
    


    # TO-DO: Mantener (este mensaje) solo en home_page para mostrar "Predicción completa".
    # Mostrar en la página principal la opción seleccionada y el valor del slider
    st.write(f'Página actual: {st.session_state["page"]}')

    # Pie de página con información de los creadores
    if st.session_state['page'] == 'Inicio':
        # Footer de la página de inicio
        st.markdown(custom_footer(), unsafe_allow_html=True)


if __name__ == "__main__":
    main()

        
