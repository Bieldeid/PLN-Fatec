import numpy as np

qnt_alunos = int(input ("Quantos alunos serão avaliados: \n"))
qnt_alunos = qnt_alunos + 1;
print("\n")

alunos = np.arange(1, (qnt_alunos))

qnt_secao = int(input("Quantas seções existem na prova: \n"))
qnt_secao =  qnt_secao + 1
print("\n")

secoes = np.arange(1, (qnt_secao))
lista_peso = []

for x in secoes:
    peso = float(input (f"Digite o peso da {x}º seção: "))
    lista_peso.append(peso)
    print("\n")

array_peso = np.array(lista_peso)

soma_pesos = np.sum(array_peso)
if soma_pesos == 10:
    print ("Pesos válidos \n")
else:
    print(f"A soma dos pesos é: {soma_pesos}. Ela precisa ser 10! \n")
    exit()

notas_matriz = []

for aluno in alunos:
    lista_notas = []
    print("\n")
    print(f"Digite as notas do {aluno}º aluno:")
    for secao in secoes:
        nota = float(input(f"Digite a nota da {secao}º seção: "))
        lista_notas.append(nota)
    notas_matriz.append(lista_notas)



notas_e_alunos = np.array(notas_matriz)
dimensao_notas = notas_e_alunos.reshape(alunos.size, secoes.size)

def calcularNotas (dimensao_notas, peso_notas):
    calculo = dimensao_notas * peso_notas
    soma_notas = np.sum(calculo, axis=1)
    nota_final = soma_notas / 10
    return nota_final

calculo_notas = calcularNotas(dimensao_notas, array_peso)
print(calculo_notas.reshape(alunos.size, 1))
