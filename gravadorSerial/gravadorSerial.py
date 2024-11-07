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
        self.msg = None
        self.msgEstruturada = None
        
    def mensagensParaEnviar(self, info = []):
        def enviarMensagem():
            msgBytes = bytes(info)
            self.ser.write(msgBytes)
            print(msgBytes)
            

            self.msg = self.ser.read(64)
            
            self.msgEstruturada = """
            
            
            
            
            """
            
            print(self.msg)
    
        thread = threading.Thread(target = enviarMensagem)
        thread.start()
        thread.join()
        
    