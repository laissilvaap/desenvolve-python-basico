def substituir_vogais(frase):
    vogais = "AEIOUaeiou"
    for vogal in vogais:
        frase = frase.replace(vogal, "*") # Substitui a vogal pelo *
    return frase

# Entrada
frase = input("Digite uma frase: ")

# Saída
print("Frase editada:", substituir_vogais(frase))
