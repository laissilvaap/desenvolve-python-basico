#Entrada de dados
idade = int(input("Digite sua idade:"))
jogos = input("Você já jogou pelo menos 3 jogos de tabuleiro?")
vitorias = int(input("Quantos jogos já venceu?"))

#Processamento
resultado = (idade >= 16 and idade <= 18) and (jogos == 'True' and vitorias >= 1)

#Saída de dados
print (f"Apto para ingressar no clube de jogos: {resultado}")