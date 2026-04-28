import tkinter as tk

def calcular():
    F = float(entry1.get())
    A = float(entry2.get())
    resultado = F / A
    label_resultado.config(text=f"Resultado: {resultado:.2f} Pa")
janela = tk.Tk()
janela.title("Calculadora de Resistência de Materiais")
janela.geometry("400x300")
tk.Label(janela, text="Calculadora de Resistência de Materiais", font=("Arial", 12, "bold")).pack(pady=10)
tk.Label(janela, text="Força (N):").pack()
entry1 = tk.Entry(janela, width=20)
entry1.pack(pady=3)
tk.Label(janela, text="Área (m²):").pack()
entry2 = tk.Entry(janela, width=20)
entry2.pack(pady=3)
tk.Button(janela, text="Calcular", command=calcular, bg="blue", fg="white", width=15).pack(pady=10)
label_resultado = tk.Label(janela, text="Resultado: ", font=("Arial", 11))
label_resultado.pack()

janela.mainloop()