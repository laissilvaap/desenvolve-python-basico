def converter_data(data):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    # Divide a data em dia, mês e ano
    dia, mes, ano = data.split("/")
    dia, mes = int(dia), int(mes)
        
    if 1 <= mes <= 12:
        return f"Você nasceu em {dia} de {meses[mes - 1]} de {ano}."
    else:
        return "Mês inválido."

# Entrada
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Saída
print(converter_data(data_nascimento))
