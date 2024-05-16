import threading
import time
import serial

def serial_Port(): # Faz a comunicação com a porta serial
    def send(): # Função que manda os dados para a porta serial
        i = 0
        while True:
            bytes_enviar = str(i).encode()
            print("Valor a ser enviado:", i)  # Mostrar o valor antes de enviar
            ser.write(bytes_enviar)
            time.sleep(1)  # Reduzi o tempo de sleep para 1 segundo para facilitar o teste
            ser.flush()
            i += 1  # Incrementar o valor para o próximo envio

    thread = threading.Thread(target=send)
    thread.start()
ser = serial.Serial("COM5", 115200, 8, "N", 1, 0.05)
serial_Port()