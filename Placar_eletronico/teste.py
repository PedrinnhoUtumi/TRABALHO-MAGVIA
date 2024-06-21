from datetime import datetime

# Exemplo de string que representa o tempo
cronometro_str = "2024-06-21 15:30:45.123456"

# Formato da string
formato = '%Y-%m-%d %H:%M:%S.%f'

# Converter a string para datetime
contador = datetime.strptime(cronometro_str, formato)

# Extrair apenas horas, minutos, segundos e milissegundos
horas = contador.hour
minutos = contador.minute
segundos = contador.second
milissegundos = int(contador.microsecond / 1000)  # Convertendo microssegundos para milissegundos

# Formatar como desejado (por exemplo, HH:MM:SS.mmm)
tempo_formatado = f"{horas:02}:{minutos:02}:{segundos:02}.{milissegundos:03}"

print(f'Tempo formatado: {tempo_formatado}')
