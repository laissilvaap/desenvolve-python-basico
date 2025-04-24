frase = input(str("Digite uma frase:"))
count_espaço = 0

for i in range(len(frase)):
    if frase[i] in ' ':
        count_espaço += 1
    
print("Espaços em branco: ",count_espaço)
    

