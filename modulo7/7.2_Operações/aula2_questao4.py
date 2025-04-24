def validador_senha(senha):
    # Verifica o comprimento mínimo de 8 caracteres
    if len(senha) < 8:
        return "Senha inválida: deve ter pelo menos 8 caracteres."

    # Verifica se contém pelo menos uma letra maiúscula
    possui_maiuscula = False
    for char in senha:
        if char.isupper():
            possui_maiuscula = True
            break
    if not possui_maiuscula:
        return "Senha inválida: deve conter pelo menos uma letra maiúscula."

    # Verifica se contém pelo menos uma letra minúscula
    possui_minuscula = False
    for char in senha:
        if char.islower():
            possui_minuscula = True
            break
    if not possui_minuscula:
        return "Senha inválida: deve conter pelo menos uma letra minúscula."

    # Verifica se contém pelo menos um número
    possui_numero = False
    for char in senha:
        if char.isdigit():
            possui_numero = True
            break
    if not possui_numero:
        return "Senha inválida: deve conter pelo menos um número."

    # Verifica se contém pelo menos um caractere especial
    possui_caractere_especial = False
    for char in senha:
        if char in "@#$%^&*!":
            possui_caractere_especial = True
            break
    if not possui_caractere_especial:
        return "Senha inválida: deve conter pelo menos um caractere especial (@, #, $, etc.)."

    return "Senha válida!"

# Teste 
senha = input("Digite uma senha para validar: ")
print(validador_senha(senha))
