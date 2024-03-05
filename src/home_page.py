import streamlit as st
import tabula
import pandas as pd
import joblib
import tensorflow as tf
from components.components import custom_title, description


# definición de columnas del dataset
columnas = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
            'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
            'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']

# def show_home_page():
#     # creación del dataframe
#     st.subheader("Página de Inicio")
#     uploaded_files = st.file_uploader("Elige tus archivos PDF", type="pdf", accept_multiple_files=True, key='home_page_file_uploader')

#     if uploaded_files:
#         # Procesa solo si hay archivos nuevos o si es la primera carga
#         if 'uploaded_files' not in st.session_state or uploaded_files != st.session_state.uploaded_files:
#             df = pd.DataFrame(columns=columnas)
    
#             for uploaded_file in uploaded_files:
#                 if uploaded_file is not None:
#                     # lectura de las tablas de los archivos
#                     df_temp_list = tabula.read_pdf(uploaded_file, pages='all')
#                     for df_temp in df_temp_list:
#                         # comprueba si es un dataframe
#                         if isinstance(df_temp, pd.DataFrame):
#                             # comprueba si tiene las columnas correctas
#                             if set(columnas).issubset(df_temp.columns):
#                                 # concatenación al dataframe principal
#                                 df = pd.concat([df, df_temp], ignore_index=True)
#                             else:
#                                 st.warning(f"El archivo {uploaded_file.name} no tiene las columnas correctas.")
#                         else:
#                             st.warning(f"El archivo {uploaded_file.name} no contiene ninguna tabla.")
            
#     # reemplaza las comas por puntos para poder convertir en float
#     pd.set_option('future.no_silent_downcasting', True)
#     df = df.replace(',', '.', regex=True)

#     # conversión de los datos de los archivos a float
#     df = df.astype(float)

#     # cálculo de la media para poder aplicar el modelo de clustering
#     columnas_median = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 
#                     'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 
#                     'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28']

#     df['Median'] = df[columnas_median].mean(axis=1)

#     # return df
#     # Almacena los archivos cargados y el DataFrame en st.session_state
#     st.session_state.uploaded_files = uploaded_files
#     st.session_state.df = df

def show_home_page():
    ### Cabecera  ##################################################################################

    # Imagen Cabecera de la aplicación
    st.image("src/static/image/banner.webp", use_column_width=True, output_format='auto')

    # Titulo de la aplicación
    st.markdown(custom_title('Fraud-Detect'), unsafe_allow_html=True)

    # Breve descripción de la aplicación
    st.markdown(description(), unsafe_allow_html=True)


    st.subheader("Página de Inicio")
    uploaded_files = st.file_uploader("Elige tus archivos PDF", type="pdf", accept_multiple_files=True, key='home_page_file_uploader')

    # Inicializa df solo si hay nuevos archivos para procesar
    if uploaded_files and ('uploaded_files' not in st.session_state or uploaded_files != st.session_state.uploaded_files):
        df = pd.DataFrame(columns=columnas)  # Crear un nuevo DataFrame para los archivos cargados
        
        for uploaded_file in uploaded_files:
            if uploaded_file is not None:
                df_temp_list = tabula.read_pdf(uploaded_file, pages='all')
                for df_temp in df_temp_list:
                    if isinstance(df_temp, pd.DataFrame):
                        if set(columnas).issubset(df_temp.columns):
                            df = pd.concat([df, df_temp], ignore_index=True)
                        else:
                            st.write(f"El archivo {uploaded_file.name} no tiene las columnas correctas.")
                    else:
                        st.write(f"El archivo {uploaded_file.name} no contiene ninguna tabla.")
        
        pd.set_option('future.no_silent_downcasting', True)
        df.replace(',', '.', regex=True, inplace=True)
        df = df.astype(float)
        
        columnas_median = [c for c in columnas if c not in ['Time', 'Amount']]
        df['Median'] = df[columnas_median].mean(axis=1)
        
        st.session_state['df'] = df  # Almacena el DataFrame procesado en el estado de la sesión
        st.session_state['uploaded_files'] = uploaded_files  # Actualiza la referencia de archivos cargados