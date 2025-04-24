import string

def limpar_texto(texto):
    # Remove pontuação, espaços e converte para minúsculas
    return "".join(char.lower() for char in texto if char.isalnum())

def eh_palindromo(frase):
     # Verifica a frase limpa de trás pra frente
    frase_limpa = limpar_texto(frase)
    return frase_limpa == frase_limpa[::-1]

while True:
    frase = input("Digite uma frase (ou 'Fim' para sair): ") # Entrada
    
    if frase.lower() == "fim": # Encerra o programa caso o usuário digite "fim"
        print("Programa encerrado.")
        break
    
    # Saída
    if eh_palindromo(frase):
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")
