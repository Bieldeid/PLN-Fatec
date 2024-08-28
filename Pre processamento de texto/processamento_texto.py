import re

def pre_processa_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]','',texto)
    palavras = texto.split()

    return palavras;

texto = input("Digite seu comentário sobre o produto: \n")
print(pre_processa_texto(texto))