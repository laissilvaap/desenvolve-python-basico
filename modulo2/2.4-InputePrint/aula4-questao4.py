#Leitura/Entrada de dados
valor = int(input("Digite o valor:"))

#Processamento
##Quantidade de notas de 100
notas_100 = valor // 100
##Quanto resta
valor = valor % 100
##Quantidade de notas 50
notas_50 = valor // 50
##Quanto resta
valor = valor % 50
##Quantidade notas de 20
notas_20 = valor // 20
##Resta
valor = valor % 20
##Notas de 10
notas_10 = valor // 10
##Resta 
valor = valor % 10
##Notas de 5
notas_5 = valor // 5
##Resta 
valor = valor % 5
##Notas de 2
notas_2 = valor // 2
##Resta 
valor = valor % 2
## Restante
notas_1 = valor

#Saída de dados/Impressão
print(f"{notas_100} nota(s) de 100")
print(f"{notas_50} nota(s) de 50")
print(f"{notas_20} nota(s) de 20")
print(f"{notas_10} nota(s) de 10")
print(f"{notas_5} nota(s) de 5")
print(f"{notas_2} nota(s) de 2")
print(f"{notas_1} nota(s) de 1")
