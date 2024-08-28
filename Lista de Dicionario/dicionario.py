'''
1) Crie uma lista de dicionários
'''

d1 = {  "Autor": "Joao",
        "Comentario": "Estou tão feliz hoje!",
        "Sentimento": "Positivo" }

d2 = {  "Autor": "Maria",
        "Comentario": "Este filme é tão triste. ",
        "Sentimento": "Negativo" }

d3 = {  "Autor": "Carlos",
        "Comentario": "Que dia chuvoso entediante...",
        "Sentimento": "Positivo" }

d4 = {  "Autor": "Ana",
        "Comentario": "Adorei a nova música da banda! ",
        "Sentimento": "Negativo" }

d5 = {  "Autor": "Roberto",
        "Comentario": "Eureka, consegui resolver este problema",
        "Sentimento": "Positivo" }

lista_dicionarios = [d1, d2, d3, d4, d5]

'''
2) Faça uma rotina para totalizar a quantidade de comentários negativos e comentários positivos
'''
qnt_comentarios_positivos = 0
qnt_comentarios_negativos = 0

for x in lista_dicionarios:
    #print(f"Sentimento: {x['Sentimento']}")
    if x['Sentimento'] == "Positivo":
        qnt_comentarios_positivos +=  1
    if x['Sentimento'] == "Negativo":
        qnt_comentarios_negativos +=  1

print ("Quantidade de comentários positivos: ", qnt_comentarios_positivos)
print ("Quantidade de comentários negativos: ", qnt_comentarios_negativos)

'''
3) Calcule e mostre na tela a proporção de cada sentimento em relação ao total de comentários
'''

total_comentarios =  len(lista_dicionarios)

proporcao_positivos = qnt_comentarios_positivos / total_comentarios
proporcao_negativos = qnt_comentarios_negativos / total_comentarios

print (f"Proporção de comentários positivos: {proporcao_positivos:.2f}")
print (f"Proporção de comentários negativos: {proporcao_negativos:.2f}")

'''
4) Faça uma rotina para mostrar apenas os comentários positivos
'''

print ("Comentários positivos:")
for x in lista_dicionarios:
    if x['Sentimento'] == "Positivo":
        print(x['Comentario'])
#O comentário "Que dia chuvoso entediante..." ser positivo é preocupante...

'''
5) Adicione uma chave em cada dicionário chamado sentimento_valor que conterá 0 se o sentimento for negativo ou 1 se o sentimento for positivo
'''

for x in lista_dicionarios:
    if x['Sentimento'] == "Negativo":
        x["sentimento_valor"] = 0
    else:
        x["sentimento_valor"] = 1

print(lista_dicionarios)




