import streamlit as st
import tabula
import pandas as pd
import joblib
import tensorflow as tf
import data_loader  # Importa el módulo completo



# definición de columnas del dataset
columnas = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
            'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
            'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']

# carga del modelo de detección de fraude
modelo = joblib.load('model/modelo_fraud_detect.pkl')

# carga del modelo de clustering
modelo_clustering = joblib.load('model/clustering_fraud_detect.pkl')


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
    df = df.replace(',', '.', regex=True)

    # conversión de los datos de los archivos a float
    df = df.astype(float)

    # cálculo de la media para poder aplicar el modelo de clustering
    columnas_median = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 
                    'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 
                    'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28']

    df['Median'] = df[columnas_median].mean(axis=1)

    # columnas necesarias para la aplicación del modelo de clustering
    df_clustering = df[['Median', 'Amount']]

    # conversión de dataframe a tensor
    df_tensor = tf.convert_to_tensor(df[columnas].values, dtype=tf.float32)  # Solo selecciona las columnas originales aquí

    df_clustering_tensor = tf.convert_to_tensor(df_clustering.values, dtype=tf.float32)

    st.divider()

    # aplicación de los modelos
    if not df.empty:
        # Switcher para mostrar o no las gráficas
        # on = st.toggle('Mostrar las gráficas')
        df['Class'] = modelo.predict(df_tensor)
        df['Cluster'] = modelo_clustering.predict(df_clustering_tensor)

        # creación del dataframe para guardar los resultados
        results_df = pd.DataFrame(columns=["Detección Fraude", "Cluster"])

        # diccionario para definir las etiquetas de la columna cluster
        cluster_labels = {0: "PG", 1: "LS", 2: "BN", 3: "LN", 4: "IN"}

        # bucle para añadir los resultados al dataframe
        for i in range(len(df)):
            new_row = pd.DataFrame({"Detección Fraude": ["NO FRAUDE ✅" if df['Class'][i] == 0 else "FRAUDE ❌"], 
                                    "Cluster": [cluster_labels[df['Cluster'][i]]]})
            results_df = pd.concat([results_df, new_row], ignore_index=True)

        st.dataframe(results_df)

        st.divider()


def show_analysis_page():
    st.subheader("Página de análisis")
    # Aquí puedes añadir más contenido para esta página

def show_model_page():
    st.subheader("Página de modelo")
    # Aquí puedes añadir más contenido para esta página

def show_prediction_page():
    st.subheader("Página de predicción")
    # Aquí puedes añadir más contenido para esta página
