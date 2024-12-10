import serial
import serial.tools.list_ports
import threading

class GravadorSerial:
    def __init__(self):
        self.ser = None  
        self.msg = None
        self.portasUSB = []

    def listaPortas(self):
        portas = serial.tools.list_ports.comports()
        if portas:
            print("Portas seriais disponíveis:")
            for porta in portas:
                if "USB" in porta.description or "ttyUSB" in porta.device or "ttyACM" in porta.device:
                    print(f"{porta.device}: {porta.description}")
                    self.portasUSB.append(porta.device)
            return [self.portasUSB]
        else:
            print("Nenhuma porta serial encontrada.")
            return []

    def abrirPorta(self, porta):
        if self.ser and self.ser.is_open:
            print("A porta serial já está aberta.")
        else:
            self.ser = serial.Serial(port=porta, baudrate=115200, bytesize=8, parity="N", stopbits=1, timeout=0.2)
            if self.ser.is_open:
                print(f"Porta {porta} aberta com sucesso.")

    def mensagensParaEnviar(self, info=[]):
        
        self.listaPortas()
        if self.portasUSB:
            porta = self.portasUSB[0]
            self.abrirPorta(porta)

            def enviarMensagem():
                msgBytes = bytes(info)
                self.ser.write(msgBytes)
                print("=========================================================================================================================================================================================================")
                print(" MINHA MENSAGEM:")  
                print(msgBytes)
                print("=========================================================================================================================================================================================================")
                              
                self.msg = self.ser.read(64)
                
                print("=========================================================================================================================================================================================================")
                print(" RESPOSTA:")  
                print(self.msg)
                print("=========================================================================================================================================================================================================")
            thread = threading.Thread(target=enviarMensagem)
            thread.start()
            thread.join()  

        return self.msg