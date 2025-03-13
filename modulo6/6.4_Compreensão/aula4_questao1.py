#pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
lista = list (range (20, 51))
print  ("Números pares entre 20 e 50: ", [n for n in lista if n % 2 == 0 ])

#quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
lista = list(range(1, 10))
quadrado = [n**2 for n in lista]
print ("Os quadrados dos valores de 1 a 9: ", quadrado)

#números entre 1 e 100 que sejam divisíveis por 7
lista = list(range(1, 101))
print ("Números divisíveis por de 1 a 100: ", [n for n in lista if n % 7 == 0])

#valores em range(0,30,3), escreva “par” ou “ímpar” dependendo da paridade do elemento (ex: [‘par’, ‘impar’,… , ‘impar’])
valor = ["par" if n % 2 == 0 else "ímpar" for n in range(0, 30, 3)]
print(valor)
