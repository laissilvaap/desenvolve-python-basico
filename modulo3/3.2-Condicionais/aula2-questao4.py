#Entrada de dados
classe = input("Escolha a classe (guerreiro, mago ou arqueiro):")
força = int(input("Digite os pontos de força (de 1 a 20):"))
magia = int(input("Digite os pontos de magia (de 1 a 20):"))

#Processamento
resultado = (classe == 'guerreiro' and força >= 15 and magia <= 10) or (classe == 'mago' and força <= 10 and magia >= 15) or (classe == 'arqueiro' and força >= 5 and força <= 15 and magia >= 5 and magia <= 15)

#Saída de dados
print (f"Pontos de atributo consistentes com a classe escolhida: {resultado}")
