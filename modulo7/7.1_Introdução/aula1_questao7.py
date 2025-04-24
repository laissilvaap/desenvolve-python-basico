import random

def encrypt(lista_nomes):
    # Gera um número aleatório entre 1 e 10 para a chave
    chave = random.randint(1,10)
    nomes_criptografados = []
    
    for nome in lista_nomes:
        nome_cripto = ""
        for caractere in nome:
            # Criptografa caracteres no intervalo 33-126
            if 33 <= ord(caractere) <= 126:
                novo_codigo = ord(caractere) + chave  # Move o caractere para frente
                if novo_codigo > 126:  # Garante que fique dentro do intervalo visível
                    novo_codigo = 33 + (novo_codigo - 127)
                novo_caractere= chr(novo_codigo)
            else:
                novo_caractere = novo_caractere # Conserva caracteres fora do intervalo
            nome_cripto += novo_caractere
        nomes_criptografados.append(nome_cripto)
    
    return nomes_criptografados, chave

# Teste
nomes = ['Luana', 'Ju', 'Davi', 'Vivi', 'Pri', 'Luiz']
nomes_encriptados, chave = encrypt(nomes)

# Saída de dados
print("Nomes criptografados:", nomes_encriptados)
print("Chave de criptografia:", chave)
