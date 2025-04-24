import re

def limpar_cpf(cpf):
    # Remove pontos e traço do CPF
    return re.sub(r'\D', '', cpf)

def calcular_digito(cpf_numeros, peso_inicial):
    # Calcula um dígito para verificar o CPF
    soma = 0
    peso = peso_inicial
    for num in cpf_numeros:
        soma += int(num) * peso
        peso -= 1

    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def validar_cpf(cpf):
    # Valida o CPF 
    cpf = limpar_cpf(cpf)  # Remove caracteres não numéricos

    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"
    
    # Obtém os primeiros 9 dígitos
    cpf_base = cpf[:9]

    # Calcula os dígitos verificadores
    primeiro_digito = calcular_digito(cpf_base, 10)
    segundo_digito = calcular_digito(cpf_base + str(primeiro_digito), 11)

    # Verifica se os dígitos calculados batem com os fornecidos
    if cpf[-2:] == f"{primeiro_digito}{segundo_digito}":
        return "Válido!"
    else:
        return "Inválido"

# Entrada 
fornecer_cpf = input("Digite um CPF (XXX.XXX.XXX-XX): ")

# Resultado
print("CPF", validar_cpf(fornecer_cpf))
