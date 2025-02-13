n1 = float(input("Digite o valor de nota1:"))
n2 = float(input("Digite o valor de nota2:"))
n3 = float(input("Digite o valor de nota3:"))
m = (n1 + n2 + n3) / 3

while True:
    print (m)
    if m >= 60:
        print ("Aprovado") 
    elif m >= 40:
        print ("Recuperação")
    else:
        print ("Reprovado")
    break
print("Fim")