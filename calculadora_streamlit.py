import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Calculadora de Resistência dos Materiais")
st.sidebar.title("Sobre o app")
st.sidebar.info("Calculadora de Resistência dos Materiais desenvolvida em Python por Afonso Ribeiro.")
st.sidebar.markdown("---")
st.sidebar.markdown("**Cálculos disponíveis:**")
st.sidebar.markdown("- Tensão Normal")
st.sidebar.markdown("- Deformação")
st.sidebar.markdown("- Tensão de Cisalhamento")
st.sidebar.markdown("- Fator de Segurança")
st.sidebar.markdown("- Lei de Hooke")
st.sidebar.markdown("- Círculo de Mohr")

opcao = st.selectbox("Escolha o cálculo:", [
    "Tensão Normal",
    "Deformação",
    "Tensão de Cisalhamento",
    "Fator de Segurança",
    "Lei de Hooke",
    "Círculo de Mohr",
])

if opcao == "Tensão Normal":
    st.info("**Tensão Normal** (σ = F/A): Calcula a tensão gerada por uma forca aplicada perpendicularmente a uma seção transversal.")
    F = st.number_input("Força (N):")
    A = st.number_input("Área (m2):", value=1.0)
    if st.button("Calcular"):
        resultado = F / A
        st.success(f"Tensão Normal: {resultado:.2f} Pa")

elif opcao == "Deformação":
    st.info("**Deformação** (ε = δ/L): Variação relativa do comprimento de um material quando submetido a uma força.")
    delta = st.number_input("Deslocamento (m):")
    L = st.number_input("Comprimento (m):", value=1.0)
    if st.button("Calcular"):
        resultado = delta / L
        st.success(f"Deformação: {resultado:.4f}")

elif opcao == "Tensão de Cisalhamento":
    st.info("**Tensão de Cisalhamento** (τ = V/A): Tensão gerada por forças que atuam paralelamente a seção transversal, como um corte.")
    V = st.number_input("Força cortante (N):")
    A = st.number_input("Área (m2):", value=1.0)
    if st.button("Calcular"):
        resultado = V / A
        st.success(f"Tensão de Cisalhamento: {resultado:.2f} Pa")

elif opcao == "Fator de Segurança":
    st.info("**Fator de Segurança** (FS = σ_ruptura / σ_aplicada): Indica a margem de segurança entre a tensão que rompe o material e a tensão real aplicada.")
    R = st.number_input("Tensão de ruptura (Pa):")
    AP = st.number_input("Tensão aplicada (Pa):", value=1.0)
    if st.button("Calcular"):
        resultado = R / AP
        st.success(f"Fator de Segurança: {resultado:.2f}")

elif opcao == "Lei de Hooke":
    st.info("**Lei de Hooke** (σ = E x ε): Relação linear entre tensão e deformação no regime elástico — quanto maior a deformação, maior a tensão.")
    E = st.number_input("Módulo de elasticidade (Pa):", value=200000000000.0)
    epsilon = st.number_input("Deformação máxima:", value=0.01)
    if st.button("Calcular"):
        resultado = E * epsilon
        st.success(f"Lei de Hooke: {resultado:.2f} Pa")
        epsilon_valores = np.linspace(0, epsilon, 100)
        sigma_valores = E * epsilon_valores
        fig, ax = plt.subplots()
        ax.plot(epsilon_valores, sigma_valores / 1e6)
        ax.set_xlabel("Deformação")
        ax.set_ylabel("Tensão (MPa)")
        ax.set_title("Lei de Hooke - Tensão x Deformação")
        ax.grid(True)
        st.pyplot(fig)
elif opcao == "Círculo de Mohr":
    st.info("**Círculo de Mohr**: Representação gráfica de todos os estados de tensão em diferentes ângulos de um ponto de um material.")
    sigma_x = st.number_input("Tensão normal em X (Pa):")
    sigma_y = st.number_input("Tensão normal em Y (Pa):")
    tau_xy = st.number_input("Tensão de Cisalhamento (Pa):")
    if st.button("Calcular"):
        centro = (sigma_x + sigma_y) / 2
        raio = (((sigma_x - sigma_y) / 2) ** 2 + tau_xy ** 2) ** 0.5
        sigma_max = centro + raio
        sigma_min = centro - raio
        st.success(f"Tensão principal máxima: {sigma_max:.2f} Pa")
        st.success(f"Tensão principal mínima: {sigma_min:.2f} Pa")
        st.success(f"Tensão de Cisalhamento máxima: {raio:.2f} Pa")

        import numpy as np
        theta = np.linspace(0, 2 * np.pi, 100)
        x = centro + raio * np.cos(theta)
        y = raio * np.sin(theta)

        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.plot(sigma_x, tau_xy, 'ro', label='Ponto A')
        ax.plot(sigma_y, -tau_xy, 'bo', label='Ponto B')
        ax.plot(sigma_max, 0, 'g^', label='Tensão max')
        ax.plot(sigma_min, 0, 'g^', label='Tensão min')
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.set_xlabel("Tensão Normal (Pa)")
        ax.set_ylabel("Tensão de Cisalhamento (Pa)")
        ax.set_title("Círculo de Mohr")
        ax.legend()
        ax.grid(True)
        ax.set_aspect('equal')
        st.pyplot(fig)