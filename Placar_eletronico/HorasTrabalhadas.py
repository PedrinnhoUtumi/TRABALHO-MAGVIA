from datetime import datetime

def calcular_horas_por_semana(horas_por_dia, dias_por_semana, data_inicio, data_fim):
    data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y')
    data_fim = datetime.strptime(data_fim, '%d/%m/%Y')
    semanas_totais = (data_fim - data_inicio).days // 7
    dias_totais = semanas_totais * dias_por_semana
    horas_totais = dias_totais * horas_por_dia
    return horas_totais

horas_por_dia = 4
dias_por_semana = 3
data_inicio = "19/04/2024"
data_fim = datetime.now().strftime('%d/%m/%Y')

total_horas = calcular_horas_por_semana(horas_por_dia, dias_por_semana, data_inicio, data_fim)

horas_feriado = 4
horas_devendo = 8

print("O total de horas é:", total_horas - horas_feriado - horas_devendo)
