import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Calculadora de Resistencia dos Materiais")

opcao = st.selectbox("Escolha o calculo:", [
    "Tensao Normal",
    "Deformacao",
    "Tensao de Cisalhamento",
    "Fator de Seguranca",
    "Lei de Hooke"
])

if opcao == "Tensao Normal":
    F = st.number_input("Forca (N):")
    A = st.number_input("Area (m2):", value=1.0)
    if st.button("Calcular"):
        resultado = F / A
        st.success(f"Tensao Normal: {resultado:.2f} Pa")

elif opcao == "Deformacao":
    delta = st.number_input("Deslocamento (m):")
    L = st.number_input("Comprimento (m):", value=1.0)
    if st.button("Calcular"):
        resultado = delta / L
        st.success(f"Deformacao: {resultado:.4f}")

elif opcao == "Tensao de Cisalhamento":
    V = st.number_input("Forca cortante (N):")
    A = st.number_input("Area (m2):", value=1.0)
    if st.button("Calcular"):
        resultado = V / A
        st.success(f"Tensao de Cisalhamento: {resultado:.2f} Pa")

elif opcao == "Fator de Seguranca":
    R = st.number_input("Tensao de ruptura (Pa):")
    AP = st.number_input("Tensao aplicada (Pa):", value=1.0)
    if st.button("Calcular"):
        resultado = R / AP
        st.success(f"Fator de Seguranca: {resultado:.2f}")

elif opcao == "Lei de Hooke":
    E = st.number_input("Modulo de elasticidade (Pa):", value=200000000000.0)
    epsilon = st.number_input("Deformacao maxima:", value=0.01)
    if st.button("Calcular"):
        resultado = E * epsilon
        st.success(f"Lei de Hooke: {resultado:.2f} Pa")
        epsilon_valores = np.linspace(0, epsilon, 100)
        sigma_valores = E * epsilon_valores
        fig, ax = plt.subplots()
        ax.plot(epsilon_valores, sigma_valores / 1e6)
        ax.set_xlabel("Deformacao")
        ax.set_ylabel("Tensao (MPa)")
        ax.set_title("Lei de Hooke - Tensao x Deformacao")
        ax.grid(True)
        st.pyplot(fig)




