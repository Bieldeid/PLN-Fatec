# -*- coding: utf-8 -*-
"""Atv10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d4RFDh_cDiLLECVzYBjAzIrOGKEP8CBg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('population.csv')

anos = df['Year'].tolist()
populacao_urbana = df['Urban Population'].tolist()

x = np.array(anos)
y = np.array(populacao_urbana)

x = (x - np.mean(x)) / np.std(x)
y = (y - np.mean(y)) / np.std(y)

def funcao_linear(x,w,b):
    return (w * x) + b

w = 0.1
b = 0

y_hat = funcao_linear(x,w,b)

plt.scatter(x,y,color='blue', label='Dados Reais')
plt.plot(x,y_hat, color='red', label='Regressão Linear')

plt.xlabel('Ano')
plt.ylabel('População Urbana')
plt.legend()
plt.show()

def custo(y, y_hat):
    m = len(y)
    custo = np.sum((y_hat - y) ** 2) / (2 * m)
    return custo

custo_inicial = custo(y, y_hat)
print(f'Custo inicial: {custo_inicial}')

def novo_w(w, x, y, y_hat, learn_rate):
    m = len(y)
    derivada = np.sum((y_hat - y) * x) / m
    w = w - learn_rate * derivada
    return w

def novo_b(b, x, y, y_hat, learn_rate):
    m = len(y)
    derivada = np.sum(y_hat - y) / m
    b = b - learn_rate * derivada
    return b

w = 0.1
b = 0
learn_rate = 0.001
num_iteracoes = 30

for i in range(num_iteracoes):

    y_hat = funcao_linear(x, w, b)

    custo_atual = custo(y, y_hat)

    w = novo_w(w, x, y, y_hat, learn_rate)
    b = novo_b(b, x, y, y_hat, learn_rate)

    print(f'Iteração {i+1}: w = {w}, b = {b}, Custo = {custo_atual}')

y_hat_otimizado = funcao_linear(x, w, b)


plt.scatter(x, y, color='blue', label='Dados Reais')

plt.plot(x, y_hat_otimizado, color='red', label='Regressão Linear Otimizada')

plt.xlabel('Ano')
plt.ylabel('População Urbana')
plt.legend()
plt.show()