frase = input("Digite uma frase: ") 
palavra_objetivo = input("Digite a palavra objetivo da frase: ") 
objetivo = sorted(palavra_objetivo) 

lst_palavras = frase.lower().split() 
for palavra in lst_palavras: 
    if sorted(palavra) == objetivo: 
        print (palavra)