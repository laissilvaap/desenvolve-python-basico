#Entrada de dados
genero = input("Digite seu gênero (feminino ou masculino):")
idade = int(input("Digite sua idade:"))
tempo = int(input("Digite o tempo trabalhado:"))

#Processamento
a = (genero == 'feminino' and idade >= 60) or (genero == 'masculino' and idade >= 65)
b = tempo >= 30
c = idade >= 60 and tempo >= 25
resultado = a or b or c

#Saída de dados
print (f"Pode aposentar: {resultado}")