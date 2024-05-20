import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
st.header('Diagramas')
hist_button = st.button('Construir histograma')  # crear un botón
scatter_button = st.button(
    'Construir diagrama de dispersión')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

    # agregar texto debajo del gráfico
    st.markdown("""
    Este gráfico muestra la distribución de los vehículos de acuerdo a su millaje ("odometer"). Es decir, cada barra representa el número ("count") de vehículos que tienen un rango específico de millas. Se puede observar que entre 500 a 600 carros tienen acumulados entre 98.000 a 122.000 millas.
    """)

if scatter_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un diagrama de dispersión
    fig = px.scatter(car_data, x="price", y="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

    # agregar texto debajo del gráfico
    st.markdown("""
    Este gráfico muestra la relación entre el precio de un vehículo y su millaje. Se puede observar que entre menos millas acumuladas su precio es mayor con respecto a los que tienen acumuladas menos millas.
    """)

    # Link del repositorio github
    st.markdown("""
    **https://github.com/lautorres9/my_render_sprint5**
    """)
