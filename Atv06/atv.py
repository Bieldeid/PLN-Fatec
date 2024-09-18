import numpy as np

dados_meteorologicos = np.array([25, 26, 27, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12])

media = np.mean(dados_meteorologicos)
maxima= np.max(dados_meteorologicos)
minima= np.min(dados_meteorologicos)
desvio = np.std(dados_meteorologicos)

print(dados_meteorologicos)
print("Desvio: ",desvio)
print("Media: ",media)
print("Máxima: ",maxima)
print("Minima: ",minima)
