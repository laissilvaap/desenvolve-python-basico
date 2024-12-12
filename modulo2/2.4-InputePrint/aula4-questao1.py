#Leitura/Entrada de dados
comprimento = int(input("Digite o comprimento do terreno em metros:"))
largura = int(input("Digite a largura do terreno em metros:"))
preco_m2 = float(input("Digite o preço em reais por m2:"))
#Processamento de dados
area_m2 = comprimento * largura
preco_total = area_m2 * preco_m2
#Impressão/Saída de dados
print (f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}.")