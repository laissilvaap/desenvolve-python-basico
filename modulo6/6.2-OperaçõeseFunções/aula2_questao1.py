import random

aleatorios = []
for i in range(20):
    x = random.randint(-100, 100)
    aleatorios.append(x)

print (sorted(aleatorios))
print (aleatorios)
print ("O maior valor está no índice: ", aleatorios.index(max(aleatorios)))
print ("O menor valor está no índice: ", aleatorios.index(min(aleatorios)))