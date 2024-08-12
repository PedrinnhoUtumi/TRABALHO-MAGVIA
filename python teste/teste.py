velocidade = int(input("valor: "))
tempo = int(input("valor: "))

if velocidade >= -100 and velocidade <= 100: 
    if tempo >= 0 and tempo <= 200:
        resultado = velocidade * (2 * tempo)
        print(f"Resultado: {resultado}")