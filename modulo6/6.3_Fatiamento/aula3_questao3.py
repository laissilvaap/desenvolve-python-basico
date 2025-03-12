import random
#Gerando os números aleatórios
aleatorios = []
for i in range(20):
    x = random.randint(-10, 10)
    aleatorios.append(x)
print ("Original: ",aleatorios)

#Encontrando o intervalo com a maior quantidade negativos
maior_intervalo = []
atual_intervalo = []

for numero in aleatorios:
    if numero < 0:
        atual_intervalo.append(numero)
    else:
        if len(atual_intervalo) > len(maior_intervalo):
            maior_intervalo = atual_intervalo
        atual_intervalo = []

# Verificando o último intervalo
if len(atual_intervalo) > len(maior_intervalo):
    maior_intervalo = atual_intervalo

# Deletando o intervalo com a maior quantidade de números negativos
for num in maior_intervalo:
    del aleatorios[aleatorios.index(num)]

print("Editada:", aleatorios)
