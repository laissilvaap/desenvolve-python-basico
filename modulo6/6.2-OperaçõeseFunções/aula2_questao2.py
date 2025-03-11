import random

num_elementos = random.randint(5, 20)

elementos = []
for i in range(num_elementos):
    x = random.randint(1, 10)
    elementos.append(x)

print (elementos)
print ("A soma dos valores da lista é: ",sum(elementos))
print("A média dos valores da lista é: ",sum(elementos)/len(elementos)) 
