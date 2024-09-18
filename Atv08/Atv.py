import numpy as np

qnt_alunos = int(input ("Quantos alunos serão avaliados: \n"))
qnt_alunos = qnt_alunos + 1;

alunos = np.arange(1, (qnt_alunos))
print (alunos)

qnt_secao = int(input("Quantas seções existem na prova: \n"))
qnt_secao =  qnt_secao + 1

secoes = np.arange(1, (qnt_secao))
lista_peso = []

for x in secoes:
    peso = float(input (f"Digite o peso da {x}º seção: "))
    lista_peso.append(peso)

array_peso = np.array(lista_peso)

soma_pesos = np.sum(array_peso)
if soma_pesos == 10:
    print ("Pesos válidos")
else:
    print(f"A soma dos pesos é: {soma_pesos}. Ela precisa ser 10!")


