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
horas_feriado = 8
horas_devendo = 8
horas_adiantadas = 0
data_inicio = "19/04/2024"
data_fim = datetime.now().strftime('%d/%m/%Y')

total_horas = calcular_horas_por_semana(horas_por_dia, data_inicio, data_fim)   

quantidade_feita = total_horas - horas_feriado - horas_devendo + horas_adiantadas

agora = datetime.now()

if agora.hour >= 17:
    print(f"Você completou {quantidade_feita} horas hoje! Parabéns!")
    print(f"Faltam {400 - quantidade_feita} horaas para completar o estágio!")
else:
    print(f"Você completará {quantidade_feita} horas hoje! Parabéns!")
    print(f"Faltarão {400 - quantidade_feita} horaas para completar o estágio!")
    