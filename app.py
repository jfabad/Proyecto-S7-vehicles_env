import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis interactivo de anuncios de venta de coches')

st.write("✅ La app se ha cargado correctamente. Presiona un botón para ver los gráficos.")
fig = px.histogram(car_data, x='odometer')
st.plotly_chart(fig, use_container_width=True)

hist_button = st.button('Mostrar histograma del odómetro')
if hist_button:
    st.write('Histograma del odómetro de los vehículos en venta')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Mostrar gráfico de dispersión precio vs odómetro')
if scatter_button:
    st.write('Gráfico de dispersión entre precio y odómetro')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)
