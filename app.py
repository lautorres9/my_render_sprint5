import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
st.header('SELECCIONAR')
# crear un control de verificación
checkbox_selected = st.checkbox('Control de verificación')


if checkbox_selected:  # al seleccionar el control de verificación
    # escribir un mensaje
    st.write(
        'Creación de un histograma y un diagrama de dispersión')

    # crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")

    # crear un diagra de dispersión
    fig_scatter = px.scatter(car_data, x="price", y="odometer", )

    # mostrar un gráfico Plotly interactivo
    col3, col4 = st.beta_columns(2)
    with col3:
        st.plotly_chart(fig_hist, use_container_width=True)
    with col4:
        st.plotly_chart(fig_scatter, use_container_width=True)
