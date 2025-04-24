# solicita o nome do usuário
nome = input("Digite seu nome: ")

# percorre o nome e imprime em formato de escada
for i in range(1, len(nome) + 1):
    print(nome[:i])
