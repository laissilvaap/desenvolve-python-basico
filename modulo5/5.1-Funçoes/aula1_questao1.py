#Desenvolva um programa em Python que peça ao usuário para inserir dois números
#  decimais e calcule a diferença absoluta entre esses dois números. Utilize a 
# função nativa abs para garantir que o resultado seja sempre positivo e round 
# para arredondar o resultado para duas casas decimais.

n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))

diferença = abs(n1 - n2)
resultado = round(diferença, 2)
print("A diferença absoluta entre os números é:",resultado)