import streamlit as st
import tabula
import pandas as pd
import joblib
import tensorflow as tf


# # definición de columnas del dataset
# columnas = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
#             'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
#             'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']

# def show_home_page():
#     # creación del dataframe
#     df = pd.DataFrame(columns=columnas)
#     st.subheader("Página de Inicio")
#     uploaded_files = st.file_uploader("Elige tus archivos PDF", type="pdf", accept_multiple_files=True, key='home_page_file_uploader')

#     for uploaded_file in uploaded_files:
#         if uploaded_file is not None:
#             # lectura de las tablas de los archivos
#             df_temp_list = tabula.read_pdf(uploaded_file, pages='all')
#             for df_temp in df_temp_list:
#                 # comprueba si es un dataframe
#                 if isinstance(df_temp, pd.DataFrame):
#                     # comprueba si tiene las columnas correctas
#                     if set(columnas).issubset(df_temp.columns):
#                         # concatenación al dataframe principal
#                         df = pd.concat([df, df_temp], ignore_index=True)
#                     else:
#                         st.write(f"El archivo {uploaded_file.name} no tiene las columnas correctas.")
#                 else:
#                     # shn kgm
#                     st.write(f"El archivo {uploaded_file.name} no contiene ninguna tabla.")
    
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

#     return df



# definición de columnas del dataset
columnas = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
            'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
            'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']

def show_home_page():
    st.subheader("Página de Inicio")
    if 'uploaded_files' not in st.session_state:
        st.session_state.uploaded_files = st.file_uploader("Elige tus archivos PDF", type="pdf", accept_multiple_files=True, key='home_page_file_uploader')

    if st.session_state.uploaded_files is not None and ('df' not in st.session_state or st.button('Recargar datos')):
        df = pd.DataFrame(columns=columnas)
        for uploaded_file in st.session_state.uploaded_files:
            # Proceso para cargar y concatenar los datos de los archivos al DataFrame `df`
            df_temp_list = tabula.read_pdf(uploaded_file, pages='all')
            for df_temp in df_temp_list:
                if isinstance(df_temp, pd.DataFrame) and set(columnas).issubset(df_temp.columns):
                    df = pd.concat([df, df_temp], ignore_index=True)
        
        # Realizar la limpieza y transformaciones necesarias en `df`
        pd.set_option('future.no_silent_downcasting', True)
        df.replace(',', '.', regex=True, inplace=True)
        df = df.astype(float)
        df['Median'] = df[columnas_median].mean(axis=1)

        # Almacenar el DataFrame en el estado de la sesión
        st.session_state.df = df

    # Si ya existe un DataFrame en el estado de la sesión, opcionalmente mostrarlo o realizar acciones adicionales
    if 'df' in st.session_state and st.session_state.df is not None:
        st.dataframe(st.session_state.df)