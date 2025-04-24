# Entrada 
numero = input(str("Digite o número de celular: "))

#se tiver 8 digitos acrescenta o 9
if len(numero) == 8:
        numero = "9" + numero

# acrescenta o separador
if len(numero) == 9 and numero[0] == "9":
        print ("Número completo: ",numero[:5] + '-' + numero[5:]) #saída