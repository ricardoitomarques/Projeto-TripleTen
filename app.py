import streamlit as st
import pandas as pd
import plotly.express as px

path= "vehicles.csv"
car_data = pd.read_csv(path)

st.header('Análise Exploratória de Dados de Veículos')

# Caixa de seleção para histograma
if st.checkbox('Exibir Histograma de Quilometragem'):
    st.write('Gerando um histograma para a quilometragem dos veículos (odômetro)...')
    
    # Criar o histograma
    fig = px.histogram(car_data, x="odometer", nbins=50, 
                       title="Distribuição de Quilometragem dos Veículos",
                       labels={"odometer": "Quilometragem (milhas)"})
    
    # Exibir o gráfico interativo
    st.plotly_chart(fig, use_container_width=True)

# Caixa de seleção para gráfico de dispersão
if st.checkbox('Exibir Gráfico de Dispersão de Preço vs Quilometragem'):
    st.write('Gerando um gráfico de dispersão para o preço vs. quilometragem...')
    
    # Criar o gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price", 
                     title="Preço vs Quilometragem",
                     labels={"odometer": "Quilometragem (milhas)", "price": "Preço"},
                     color="condition",  # Diferenciar por condição do veículo
                     hover_data=["model", "fuel"])  # Mostrar informações adicionais ao passar o mouse
    
    # Exibir o gráfico interativo
    st.plotly_chart(fig, use_container_width=True)
