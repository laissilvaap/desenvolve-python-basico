n = int(input("Digite o número de respondentes:"))
soma = 0
cont = 0

while cont < n:
    print (cont)
    idade = int(input("Digite a idade:"))
    soma += idade
    media = idade
    cont += 1
    
print (f"A média das idades é {soma / 3} anos.")