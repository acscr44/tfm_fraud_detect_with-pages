import nbformat
import streamlit as st
import base64
from io import BytesIO

def cargar_cuaderno_jupyter(path):
    with open(path, 'r', encoding='utf-8') as f:
        return nbformat.read(f, as_version=4)

def mostrar_cuaderno_jupyter(nb, num_celda_inicio=0, num_celda_final=None):
    for i, cell in enumerate(nb.cells):
        # Si se especificó un número de celda final y se alcanza, detener el bucle
        if num_celda_final is not None and i > num_celda_final:
            break
        # Continuar si el índice de la celda actual aún no ha alcanzado el número de celda de inicio
        if i < num_celda_inicio:
            continue
        
        if cell.cell_type == 'markdown':
            st.markdown(cell.source)
        elif cell.cell_type == 'code':
            st.code(cell.source, language='python')
            for output in cell.outputs:
                if output.output_type == 'execute_result' or output.output_type == 'display_data':
                    if 'text/plain' in output.data:
                        st.text(output.data['text/plain'])
                    if 'image/png' in output.data:
                        base64_img = output.data['image/png']
                        img_bytes = base64.b64decode(base64_img)
                        st.image(img_bytes, use_column_width=True)
                    if 'text/html' in output.data:
                        st.markdown(output.data['text/html'], unsafe_allow_html=True)
                elif output.output_type == 'stream':
                    st.text(output.text)
                elif output.output_type == 'error':
                    st.error('\n'.join(output.traceback))




def show_analysis_page():
    st.subheader("Página de análisis")
    # Aquí puedes añadir más contenido para esta página

    # Cargar el cuaderno Jupyter
    nb_path = 'src/static/notebooks/modelo_tfm.ipynb'
    nb = cargar_cuaderno_jupyter(nb_path)

    # Especificar el inicio y el final
    # num_celda_inicio = 0  # Ajusta este valor según sea necesario
    num_celda_final = 25  # Ajusta este valor según sea necesario

    # Mostrar el rango especificado de celdas del cuaderno en Streamlit
    mostrar_cuaderno_jupyter(nb, num_celda_final=num_celda_final)
    

def show_model_page():
    st.subheader("Página de modelo")
    # Aquí puedes añadir más contenido para esta página   

    # Cargar el cuaderno Jupyter
    nb_path = 'src/static/notebooks/modelo_tfm.ipynb'
    nb = cargar_cuaderno_jupyter(nb_path)

    # Especificar el inicio y el final
    num_celda_inicio = 25  # Ajusta este valor según sea necesario
    # num_celda_final = 25  # Ajusta este valor según sea necesario

    # Mostrar el rango especificado de celdas del cuaderno en Streamlit
    mostrar_cuaderno_jupyter(nb, num_celda_inicio=num_celda_inicio)





    # st.markdown("""
    #     ## Importaciones de librerías necesarias
    #     ```python
    #     import tensorflow as tf
    #     from tensorflow import keras
    #     from tensorflow.keras import Sequential
    #     from tensorflow.keras.layers import Flatten, Dense, Dropout, BatchNormalization
    #     from tensorflow.keras.layers import Conv1D, MaxPool1D
    #     from tensorflow.keras.optimizers import Adam
    #     import pandas as pd
    #     import numpy as np
    #     import seaborn as sns
    #     import matplotlib.pyplot as plt
    #     from sklearn.model_selection import train_test_split
    #     from sklearn.preprocessing import StandardScaler
    #     from sklearn.cluster import KMeans
    #     from joblib import dump
    #     ```
    #     """, unsafe_allow_html=True
    #             )

    # st.divider()
    # image_path = "src/static/image/ccdf_head_IV_Exploracion_y_visualizacion.jpg"
    # st.markdown(f"""
    #     ## Exploración, visualización y tratamiento de los datos
    #     ```python
    #     ccdf.head()
    #     ```
    #     ![Alt Text]({image_path})
    #     """
    #             )
    # st.image(image_path, use_column_width=True)

    # st.divider()

    # st.markdown("""

    #     ```python
        
    #     ```
    #     """, unsafe_allow_html=True
    #             )

    # st.divider()

    # st.markdown("""

    #     ```python
        
    #     ```
    #     """, unsafe_allow_html=True
    #             )

    # st.divider()

    # st.markdown("""

    #     ```python
        
    #     ```
    #     """, unsafe_allow_html=True
    #             )

    # st.divider()

    # st.markdown("""

    #     ```python
        
    #     ```
    #     """, unsafe_allow_html=True
    #             )

    # st.divider()

    # st.markdown("""
    #     ```python
    #     # Mapa de calor para observar la correlaciones de los datos
    #     f, (ax) = plt.subplots(1, figsize=(24,20))
    #     sub_sample_corr = ccdf.corr()
    #     sns.heatmap(sub_sample_corr, cmap='coolwarm_r')
    #     plt.show()
    #     ```
    #     """, unsafe_allow_html=True
    #             )

    # st.divider()



