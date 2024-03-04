import streamlit as st


def show_analysis_page():
    st.subheader("Página de análisis")
    # Aquí puedes añadir más contenido para esta página

    st.markdown("""
        ## Importaciones de librerías necesarias
        ```python
        import tensorflow as tf
        from tensorflow import keras
        from tensorflow.keras import Sequential
        from tensorflow.keras.layers import Flatten, Dense, Dropout, BatchNormalization
        from tensorflow.keras.layers import Conv1D, MaxPool1D
        from tensorflow.keras.optimizers import Adam
        import pandas as pd
        import numpy as np
        import seaborn as sns
        import matplotlib.pyplot as plt
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import StandardScaler
        from sklearn.cluster import KMeans
        from joblib import dump
        ```
        """, unsafe_allow_html=True
                )

    st.divider()
    image_path = "src/static/image/ccdf_V_Preparacion_de_datos.jpg"
    st.markdown(f"""
        ## Exploración, visualización y tratamiento de los datos
        ```python
        ccdf.head()
        ```
        ![Alt Text]({image_path})
        """, unsafe_allow_html=True
                )

    st.divider()

    st.markdown("""

        ```python
        
        ```
        """, unsafe_allow_html=True
                )

    st.divider()


    st.markdown("""

        ```python
        
        ```
        """, unsafe_allow_html=True
                )

    st.divider()


    st.markdown("""

        ```python
        
        ```
        """, unsafe_allow_html=True
                )

    st.divider()


    st.markdown("""

        ```python
        
        ```
        """, unsafe_allow_html=True
                )

    st.divider()



    st.markdown("""
        ```python
        # Mapa de calor para observar la correlaciones de los datos
        f, (ax) = plt.subplots(1, figsize=(24,20))
        sub_sample_corr = ccdf.corr()
        sns.heatmap(sub_sample_corr, cmap='coolwarm_r')
        plt.show()
        ```
        """, unsafe_allow_html=True
                )

    st.divider()


def show_model_page():
    st.subheader("Página de modelo")
    # Aquí puedes añadir más contenido para esta página
