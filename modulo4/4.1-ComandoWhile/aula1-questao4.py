n = float(input("Digite um valor para n:"))
maior = 0

while n > 0:
    x = float(input("Digite o valor de x:"))
    if x > maior:
        maior = x
    n = n - 1

print ("O maior número é",maior)


