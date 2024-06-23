from datetime import datetime, timedelta
def calcular_horas_por_semana(horas_por_dia, data_inicio, data_fim):
    data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y')
    data_fim = datetime.strptime(data_fim, '%d/%m/%Y')
    
    total_horas = 0
    data = data_inicio
    while data <= data_fim:
        if data.weekday() in [0, 3, 4]:  # 0 = segunda-feira, 3 = quinta-feira, 4 = sexta-feira
            total_horas += horas_por_dia
        data += timedelta(days=1)
    return total_horas 

horas_por_dia = 4
data_inicio = "19/04/2024"
data_fim = datetime.now().strftime('%d/%m/%Y')

total_horas = calcular_horas_por_semana(horas_por_dia, data_inicio, data_fim)

horas_feriado = 4
horas_devendo = 0

print("O total de horas é:", total_horas - horas_feriado - horas_devendo)