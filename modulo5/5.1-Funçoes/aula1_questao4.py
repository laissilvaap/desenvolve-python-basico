#Escreva um programa em Python que utiliza a biblioteca datetime para exibir a 
# data e hora atuais com a formatação apresentada a seguir:

#Data: 15/03/2023 
#Hora: 14:05

from datetime import datetime
from pytz import timezone

data_atual = datetime.now()
hora_atual = datetime.now()
fuso_horario = timezone("America/Sao_Paulo")
hora_sao_paulo = hora_atual.astimezone(fuso_horario)
data_sao_paulo = data_atual.astimezone(fuso_horario)
data_sao_paulo_em_texto = data_sao_paulo.strftime("%d/%m/%Y")
hora_sao_paulo_em_texto = hora_sao_paulo.strftime("%H:%M")
print("Data: ",data_sao_paulo_em_texto)
print("Hora: ",hora_sao_paulo_em_texto)




