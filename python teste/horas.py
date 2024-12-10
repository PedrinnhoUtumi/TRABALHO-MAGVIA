from datetime import datetime, timedelta

def calcular_horas_por_semana(horas_por_dia, data_inicio, data_fim):
    data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y')
    data_fim = datetime.strptime(data_fim, '%d/%m/%Y')
    
    total_horas = 0
    data = data_inicio
    while data <= data_fim:
        if data.weekday() in [0, 3, 4]:
            total_horas += horas_por_dia
        data += timedelta(days = 1)
    return total_horas 

horas_por_dia = 4
horas_feriado = 0
horas_devendo = 0
horas_adiantadas = 0
data_inicio = "19/04/2024"
data_fim = datetime.now().strftime('%d/%m/%Y')
# data_fim = "10/12/2024"

total_horas = calcular_horas_por_semana(horas_por_dia, data_inicio, data_fim)   

quantidade_feita = total_horas - horas_feriado - horas_devendo + horas_adiantadas - 4

agora = datetime.now()

if agora.hour >= 17:
    print(f"Você completou {quantidade_feita} horas hoje! Parabéns!")
    print(f"Faltam {400 - quantidade_feita} horas para completar o estágio!")
    
elif total_horas >= 400:
    print("VOCÊ COMPLETOU O ESTÁGIOOOOOOO")

else:                     
    print(f"Você completará {quantidade_feita} horas hoje! Parabéns!")
    print(f"Faltarão {400 - quantidade_feita} horas para completar o estágio!")
    