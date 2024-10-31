import serial
import serial.tools.list_ports
import threading

class GravadorSerial:
    def __init__(self):
        self.ser = serial.Serial(
                port = "COM3", 
                baudrate = 115200, 
                bytesize = 8, 
                parity = "N", 
                stopbits = 1, 
                timeout = 1
            )
        
    def mensagensParaEnviar(self, info = []):
        def enviarMensagem():
            msgBytes = bytes(info)
            self.ser.write(msgBytes)
            print(msgBytes)

        thread = threading.Thread(target = enviarMensagem)
        thread.start()
        
    