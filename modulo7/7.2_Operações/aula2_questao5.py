import random

def embaralhar_palavras(frase):
    palavras = frase.split()  # Divide a frase em palavras
    frase_embaralhada = []

    for palavra in palavras:
        # Se a palavra tiver mais de 3 caracteres, embaralha suas letras 
        if len(palavra) > 3:
            primeira_letra = palavra[0]
            ultima_letra = palavra[-1]
            meio = palavra[1:-1]
            # Embaralha as letras internas
            meio_embaralhado = list(meio)
            random.shuffle(meio_embaralhado)
            meio_embaralhado = ''.join(meio_embaralhado)
            # Reconstrói a palavra com o primeiro e último caractere fixos
            nova_palavra = primeira_letra + meio_embaralhado + ultima_letra
            frase_embaralhada.append(nova_palavra)
        else:
            # Se a palavra tiver 3 ou menos caracteres, mantém ela como está
            frase_embaralhada.append(palavra)

    # Retorna a frase com as palavras embaralhadas
    return ' '.join(frase_embaralhada)


frase = input("Digite uma frase para embaralhar: ") # Entrada
print(embaralhar_palavras(frase)) # Saída

