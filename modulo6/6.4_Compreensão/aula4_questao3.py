horas_trabalhadas = [40, 37, 45, 40, 40, 48]  
ganho_por_hora = 20  
hora_extra = 25  
                   
# Calcula os pagamentos 
pagamentos = [(ganho_por_hora * min(horas, 40)) + (hora_extra * max(0, horas - 40)) 
    for horas in horas_trabalhadas]

print(pagamentos)
