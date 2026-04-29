import tkinter as tk
from tkinter import ttk

def calcular():
    F = float(entry1.get())
    A = float(entry2.get())
    resultado = F / A
    label_resultado.config(text=f"Resultado: {resultado:.2f} Pa")

def deformacao():
    delta = float(entry1.get())
    L = float(entry2.get())
    resultado = delta / L
    label_resultado.config(text=f"Deformação: {resultado:.4f}")

def tensao_cisalhamento():
    V = float(entry1.get())
    A = float(entry2.get())
    resultado = V / A
    label_resultado.config(text=f"Tensão de cisalhamento: {resultado:.2f} Pa") 

def fator_seguranca():
    R = float(entry1.get())
    AP = float(entry2.get())
    resultado = R / AP
    label_resultado.config(text=f"Fator de segurança: {resultado:.2f}")

def executar_calculo():
    opcao = combo.get()
    if opcao == "Tensão Normal":
        calcular()
    elif opcao == "Deformação":
        deformacao()
    elif opcao == "Tensão de cisalhamento":
        tensao_cisalhamento()
    elif opcao == "Fator de segurança":
        fator_seguranca()

def atualizar_labels(event):
    opcao = combo.get()
    if opcao == "Tensão Normal":
        label1.config(text="Força (N):")
        label2.config(text="Área (m²):")
    elif opcao == "Deformação":
        label1.config(text="Deslocamento (m):")
        label2.config(text="Comprimento (m):")
    elif opcao == "Tensão de cisalhamento":
        label1.config(text="Digite a força cortante(N):")
        label2.config(text="Digite a área (m²):") 
    elif opcao == "Fator de segurança":
        label1.config(text="Digite a tensão de ruptura (Pa):")  
        label2.config(text="Digite a tensão aplicada (Pa):")

        

janela = tk.Tk()
janela.title("Calculadora de Resistência de Materiais")
janela.geometry("400x300")

tk.Label(janela, text="Calculadora de Resistência de Materiais", font=("Arial", 12, "bold")).pack(pady=10)

combo = ttk.Combobox(janela, values=[
"Tensão Normal", 
"Deformação",
"Tensão de cisalhamento",
"Fator de Segurança",
], width=35)
combo.current(0)
combo.pack(pady=5)
combo.bind("<<ComboboxSelected>>", atualizar_labels)

label1 = tk.Label(janela, text="Força (N):")
label1.pack()
entry1 = tk.Entry(janela, width=20)
entry1.pack(pady=3)

label2 = tk.Label(janela, text="Área (m²):")
label2.pack()
entry2 = tk.Entry(janela, width=20)
entry2.pack(pady=3)

tk.Button(janela, text="Calcular", command=executar_calculo, bg="blue", fg="white", width=15).pack(pady=10)
label_resultado = tk.Label(janela, text="Resultado: ", font=("Arial", 11))
label_resultado.pack()

janela.mainloop()