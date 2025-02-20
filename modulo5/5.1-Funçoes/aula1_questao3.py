#Escreva um programa em Python que utiliza a biblioteca random para gerar um número
#  aleatório entre 1 e 10 e peça ao usuário para adivinhar o número. Forneça
#  feedback se o palpite é muito alto, muito baixo ou correto. Interrompa a
#  execução somente quando o usuário acertar o palpite.

import random

n = random.randint(0,10)

while True:
    palpite = int(input("Digite um número de 0 a 10:"))

    if palpite > n:
        print("Muito alto, tente novamente!")
    elif palpite < n:
        print("Muito baixo, tente novamente!")
    else: 
        print("Correto!")
        break