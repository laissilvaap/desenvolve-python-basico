#Entrada
produto1 = (input("Digite o nome do produto 1:"))
#calça
preço1 = float(input("Digite o preço unitário do produto 1:"))
#199.90
quantidade1 = int(input("Digite a quantidade do produto 1:"))
#3
produto2 = (input("Digite o nome do produto 2:"))
#camisa
preço2 = float(input("Digite o preço unitário do produto 2:"))
#49.95
quantidade2 = int(input("Digite a quantidade do produto 2:"))
#10
produto3 = (input("Digite o nome do produto 3:"))
#cinto
preço3 = float(input("Digite o preço unitário do produto 3:"))
#25
quantidade3 = int(input("Digite a quantidade do produto 3:"))
#3

#Processamento
valor = (preço1 * quantidade1) + (preço2 * quantidade2) + (preço3 * quantidade3)

#Saída
print (f"Total: R${valor:,.2f}")
#1,174.20


