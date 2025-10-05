#Import libraries
import pandas as pd
import streamlit as st
import plotly.express as px
#Load data
df_cars = pd.read_csv('C:/Users/maja_/tripleten/projects/Proyecto-7/vehicles_us.csv')\
#Create header
st.header('Anuncio de coches')
#Create button to and histogram graph when you click on it.
hist_button = st.button('Construir Histograma')
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de autos en Norte América')
    fig_hist = px.histogram(df_cars, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)
#Create button to build scatter graph when you click on it.
scatter_button = st.button('Construir Diagrama de Dispersión')
if scatter_button:
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de autos en Norte América')
    fig_scatter = px.scatter(df_cars, x="odometer", y='price')
    st.plotly_chart(fig_scatter)



