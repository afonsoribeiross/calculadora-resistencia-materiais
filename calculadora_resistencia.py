# Calculadora de Resistência de Materiais

def tensao_normal(forca, area):
    return forca / area

def deformacao(delta, comprimento):
    return delta / comprimento

def lei_hooke(modulo_elasticidade, deformacao):
    return modulo_elasticidade * deformacao

print("=== Calculadora de Resistência de Materiais ===")
print()

# Tensão normal
F = float(input("Digite a força (N): "))
A = float(input("Digite a área (m²): "))
sigma = tensao_normal(F, A)
print(f"Tensão normal: {sigma:.2f} Pa")
print()

# Deformação
delta = float(input("Digite o deslocamento (m): "))
L = float(input("Digite o comprimento original (m): "))
epsilon = deformacao(delta, L)
print(f"Deformação: {epsilon:.4f}")
print()

# Lei de Hooke
E = float(input("Digite o módulo de elasticidade (Pa): "))
sigma_hooke = lei_hooke(E, epsilon)
print(f"Tensão pela Lei de Hooke: {sigma_hooke:.2f} Pa")