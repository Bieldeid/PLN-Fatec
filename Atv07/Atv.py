import numpy as np

altura = np.array([1.65, 1.75, 1.80, 1.70, 1.68, 1.72, 1.78, 1.60, 1.85, 1.73, 1.69, 1.75, 1.62, 1.80, 1.77, 1.68, 1.79, 1.81, 1.76, 1.74])
peso = np.array([65, 70, 75, 80, 60, 68, 72, 58, 90, 72, 65, 70, 55, 78, 79, 62, 85, 88, 70, 75])

imc = peso/altura

muito_abaixo = 0
abaixo = 0
normal = 0
sobrepeso = 0
obesidade_grau_1 = 0
obesidade_grau_2 = 0
obesidade_grau_3 = 0
for x in imc:
    if x < 16.9:
        print(f"IMC: {x:.2f} - Muito abaixo do peso")
        muito_abaixo = muito_abaixo + 1;
    elif x >= 17 and x < 18.4:
        print(f"IMC: {x:.2f} - Abaixo do peso")
        abaixo = abaixo + 1;
    elif x >= 18.5 and x < 24.9:
        print(f"IMC: {x:.2f} - Peso normal")
        normal = normal + 1;
    elif x >= 25 and x < 29.9:
        print(f"IMC: {x:.2f} - Sobrepeso")
        sobrepeso = sobrepeso + 1;
    elif x >= 30 and x < 34.9:
        print(f"IMC: {x:.2f} - Obesidade grau I")
        obesidade_grau_1 = obesidade_grau_1 + 1;
    elif x >= 35 and x < 39.9:
        print(f"IMC: {x:.2f} - Obesidade grau II (severa)")
        obesidade_grau_2 = obesidade_grau_2 + 1;
    else:
        print(f"IMC: {x:.2f} - Obesidade grau III")
        obesidade_grau_3 = obesidade_grau_3 + 1;

print("Quantidade muito abaixo do peso: ", muito_abaixo)
print("Quantidade abaixo do peso: ", abaixo)
print("Quantidade de peso normal: ", normal)
print("Quantidade obsidade Grau I: ", obesidade_grau_1)
print("Quantidade obsidade Grau II: ", obesidade_grau_2)
print("Quantidade obsidade Grau III: ", obesidade_grau_3)