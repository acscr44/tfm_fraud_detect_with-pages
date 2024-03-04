import streamlit as st
import tabula
import pandas as pd
import joblib
import tensorflow as tf


# definición de columnas del dataset
columnas = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
            'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
            'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']

def show_home_page():
    # creación del dataframe
    df = pd.DataFrame(columns=columnas)
    st.subheader("Página de Inicio")
    uploaded_files = st.file_uploader("Elige tus archivos PDF", type="pdf", accept_multiple_files=True, key='home_page_file_uploader')

    for uploaded_file in uploaded_files:
        if uploaded_file is not None:
            # lectura de las tablas de los archivos
            df_temp_list = tabula.read_pdf(uploaded_file, pages='all')
            for df_temp in df_temp_list:
                # comprueba si es un dataframe
                if isinstance(df_temp, pd.DataFrame):
                    # comprueba si tiene las columnas correctas
                    if set(columnas).issubset(df_temp.columns):
                        # concatenación al dataframe principal
                        df = pd.concat([df, df_temp], ignore_index=True)
                    else:
                        st.write(f"El archivo {uploaded_file.name} no tiene las columnas correctas.")
                else:
                    # shn kgm
                    st.write(f"El archivo {uploaded_file.name} no contiene ninguna tabla.")
    
    # reemplaza las comas por puntos para poder convertir en float
    pd.set_option('future.no_silent_downcasting', True)
    df = df.replace(',', '.', regex=True)

    # conversión de los datos de los archivos a float
    df = df.astype(float)

    # cálculo de la media para poder aplicar el modelo de clustering
    columnas_median = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 
                    'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 
                    'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28']

    df['Median'] = df[columnas_median].mean(axis=1)


    # Footer de la página de inicio
    # Pie de página con información de los creadores
    st.markdown('Creadores:')
    st.page_link("https://www.linkedin.com/in/pablo-oller-perez-7995721b2", label="**Pablo Oller Pérez**")
    st.page_link("https://www.linkedin.com/in/pablo-oller-perez-7995721b2", label="**Pablo Santos Quirce**")
    st.page_link("https://www.linkedin.com/in/pablo-oller-perez-7995721b2", label="**Alejandro Castillo Carmona**")

    
    return df