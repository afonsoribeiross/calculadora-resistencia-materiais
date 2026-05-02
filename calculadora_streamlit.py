import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Calculadora de Resistencia dos Materiais")

opcao = st.selectbox("Escolha o calculo:", [
    "Tensao Normal",
    "Deformacao",
    "Tensao de Cisalhamento",
    "Fator de Seguranca",
    "Lei de Hooke",
    "Circulo de Mohr",
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
elif opcao == "Circulo de Mohr":
    sigma_x = st.number_input("Tensão normal em X (Pa):")
    sigma_y = st.number_input("Tensão normal em Y (Pa):")
    tau_xy = st.number_input("Tensão de Cisalhamento (Pa):")
    if st.button("Calcular"):
        centro = (sigma_x + sigma_y) / 2
        raio = (((sigma_x - sigma_y) / 2) ** 2 + tau_xy ** 2) ** 0.5
        sigma_max = centro + raio
        sigma_min = centro - raio
        st.success(f"Tensao principal maxima: {sigma_max:.2f} Pa")
        st.success(f"Tensao principal minima: {sigma_min:.2f} Pa")
        st.success(f"Tensao de cisalhamento maxima: {raio:.2f} Pa")

        import numpy as np
        theta = np.linspace(0, 2 * np.pi, 100)
        x = centro + raio * np.cos(theta)
        y = raio * np.sin(theta)

        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.plot(sigma_x, tau_xy, 'ro', label='Ponto A')
        ax.plot(sigma_y, -tau_xy, 'bo', label='Ponto B')
        ax.plot(sigma_max, 0, 'g^', label='Tensao max')
        ax.plot(sigma_min, 0, 'g^', label='Tensao min')
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.set_xlabel("Tensao Normal (Pa)")
        ax.set_ylabel("Tensao de Cisalhamento (Pa)")
        ax.set_title("Circulo de Mohr")
        ax.legend()
        ax.grid(True)
        ax.set_aspect('equal')
        st.pyplot(fig)