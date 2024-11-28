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
        
    def mensagensParaEnviar(self, info = []):
        def enviarMensagem():
            msgBytes = bytes(info)
            self.ser.write(msgBytes)
            print(msgBytes)
            
            self.msg = self.ser.read(64)
            
            print(self.msg)
            

        thread = threading.Thread(target = enviarMensagem)
        thread.start()
        thread.join()
        
        return self.msg

    
# import serial
# import serial.tools.list_ports
# import threading

# class GravadorSerial:
#     def __init__(self):
#         self.ser = None  
#         self.msg = None

#     def listaPortas(self):
#         portas = serial.tools.list_ports.comports()
#         if portas:
#             print("Portas seriais disponíveis:")
#             for porta in portas:
#                 print(f"{porta.device}: {porta.description}")
#             return [porta.device for porta in portas]
#         else:
#             print("Nenhuma porta serial encontrada.")
#             return []

#     def abrirPorta(self, porta):
#         if self.ser and self.ser.is_open:
#             print("A porta serial já está aberta.")
#         else:
#             self.ser = serial.Serial(port=porta, baudrate=115200, bytesize=8, parity="N", stopbits=1, timeout=1)
#             if self.ser.is_open:
#                 print(f"Porta {porta} aberta com sucesso.")

#     def mensagensParaEnviar(self, info=[]):
#         portas = self.listaPortas()
#         if portas:
#             porta = portas[0]
#             self.abrirPorta(porta)

#             def enviarMensagem():
#                 msgBytes = bytes(info)
#                 print(f"Enviando: {msgBytes}")
#                 self.ser.write(msgBytes)
                
#                 self.msg = self.ser.read(64)
#                 print(f"Resposta recebida: {self.msg}")

#             thread = threading.Thread(target=enviarMensagem)
#             thread.start()
#             thread.join()  
            

#         return self.msg