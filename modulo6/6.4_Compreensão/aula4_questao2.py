# A lista de vogais da frase, ordenada alfabeticamente
#  A lista de consoantes da frase (remova espaços em branco)

frase = input("Digite uma frase: ")

vogais = sorted([letra for letra in frase if letra in "aeiouAEIOU"])
consoantes = [letra for letra in frase if letra not in "aeiouAEIOU " and letra != " "]

print("Vogais ordenadas:", vogais)
print("Consoantes:", consoantes)
