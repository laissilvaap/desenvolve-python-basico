lista = []

quantlista = int(input("Quantos elementos terá na lista (mínimo 4): "))


for i in range(quantlista):
    if quantlista < 4 : 
        print ("Erro! Quantidade de elementos abaixo do desejado.")
        break
    if quantlista >= 4 :
        lista.append(int(input("Digite o elemento da lista : ")))

#•A lista original
print ("A lista original : ",lista)
 #•Os 3 primeiros elementos
print ("Os 3 primeiros elementos: ",lista[0:3])
# •Os 2 últimos elementos
print ("Os 2 últimos elementos: ",lista[-2:])
#•A lista invertida (do fim para o começo)
print ("A lista invertida: ",lista[::-1])
#•Os elementos de índice par 
pares = [lista[i] for i in range(len(lista)) if i % 2 == 0]
print ("Os elementos de índice pares :",pares)
#•Os elementos de índice ímpar 
impares = [lista[i] for i in range(len(lista)) if i % 2 != 0]
print ("Os elementos de índice ímpares: ",impares)
