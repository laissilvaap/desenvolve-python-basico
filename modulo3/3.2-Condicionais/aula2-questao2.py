#Entrada de dados
idade_juliana = int(input("Digite a idade de Juliana:"))
idade_cris = int(input("Digite a idade de Cris:"))

#Processamento
resultado = idade_juliana > 17 or idade_cris > 17

#Saída de dados
print (f"Podem entrar no bar? {resultado}")