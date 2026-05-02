import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Calculadora de Resistencia dos Materiais")
st.sidebar.title("Sobre o app")
st.sidebar.info("Calculadora de Resistencia dos Materiais desenvolvida em Python por Afonso Ribeiro — Estudante de Engenharia Mecanica na UEMA.")
st.sidebar.markdown("---")
st.sidebar.markdown("**Calculos disponíveis:**")
st.sidebar.markdown("- Tensao Normal")
st.sidebar.markdown("- Deformacao")
st.sidebar.markdown("- Tensao de Cisalhamento")
st.sidebar.markdown("- Fator de Seguranca")
st.sidebar.markdown("- Lei de Hooke")
st.sidebar.markdown("- Circulo de Mohr")

opcao = st.selectbox("Escolha o calculo:", [
    "Tensao Normal",
    "Deformacao",
    "Tensao de Cisalhamento",
    "Fator de Seguranca",
    "Lei de Hooke",
    "Circulo de Mohr",
])

if opcao == "Tensao Normal":
    st.info("**Tensao Normal** (σ = F/A): Calcula a tensao gerada por uma forca aplicada perpendicularmente a uma secao transversal.")
    F = st.number_input("Forca (N):")
    A = st.number_input("Area (m2):", value=1.0)
    if st.button("Calcular"):
        resultado = F / A
        st.success(f"Tensao Normal: {resultado:.2f} Pa")

elif opcao == "Deformacao":
    st.info("**Deformacao** (ε = δ/L): Variacao relativa do comprimento de um material quando submetido a uma forca.")
    delta = st.number_input("Deslocamento (m):")
    L = st.number_input("Comprimento (m):", value=1.0)
    if st.button("Calcular"):
        resultado = delta / L
        st.success(f"Deformacao: {resultado:.4f}")

elif opcao == "Tensao de Cisalhamento":
    st.info("**Tensao de Cisalhamento** (τ = V/A): Tensao gerada por forcas que atuam paralelamente a secao transversal, como um corte.")
    V = st.number_input("Forca cortante (N):")
    A = st.number_input("Area (m2):", value=1.0)
    if st.button("Calcular"):
        resultado = V / A
        st.success(f"Tensao de Cisalhamento: {resultado:.2f} Pa")

elif opcao == "Fator de Seguranca":
    st.info("**Fator de Seguranca** (FS = σ_ruptura / σ_aplicada): Indica a margem de seguranca entre a tensao que rompe o material e a tensao real aplicada.")
    R = st.number_input("Tensao de ruptura (Pa):")
    AP = st.number_input("Tensao aplicada (Pa):", value=1.0)
    if st.button("Calcular"):
        resultado = R / AP
        st.success(f"Fator de Seguranca: {resultado:.2f}")

elif opcao == "Lei de Hooke":
    st.info("**Lei de Hooke** (σ = E x ε): Relacao linear entre tensao e deformacao no regime elastico — quanto maior a deformacao, maior a tensao.")
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
    st.info("**Circulo de Mohr**: Representacao grafica de todos os estados de tensao em diferentes angulos de um ponto de um material.")
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