import re

texto = input('Digite uma mensagem: \n')

def normaliza_texto(texto):
    dicionario_corrigido ={
        "vc": "você",
        "eh": "é",
        "mto": "muito",
        "mt": "muito",
        "blz": "beleza",
        "pdp": "pode pá",
        "tbm": "também",
        "tb": "também",
        "pq": "porque",
        "n": "não",
        "s": "sim",
        "tlg": "tá ligado"
    }

    girias_expressoes = ["blz", "pdp", "tlg", "XD", ":)", ">:["]

    palavras = texto.split()
    palavras_normalizadas = [dicionario_corrigido.get(palavras,palavras) for palavras in palavras]

    palavras_final = [palavras for palavras in palavras_normalizadas if palavras not in girias_expressoes]

    texto_normalizado = " ".join(palavras_final)

    return texto_normalizado

print (normaliza_texto(texto))

