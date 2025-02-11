# Entrada de dados
distancia = float(input("Digite a distância em Km:"))
peso = float(input("Digite o peso em Kg:"))

#Processamento
if distancia <= 100:
    tarifa = 1  
elif 101 <= distancia <= 300:
    tarifa = 1.50  
else:
    tarifa = 2  
if peso <= 10: 
    frete = tarifa * peso  
else:
     frete = tarifa * peso + 10 

#Saída de dados
print(f"O valor do frete é: R${frete:.2f}")

 