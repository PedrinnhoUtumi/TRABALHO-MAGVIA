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
        self.portasUSB = []
        if portas:
            for porta in portas:
                if "USB" in porta.description or "ttyUSB" in porta.device or "ttyACM" in porta.device:
                    self.portasUSB.append(porta.device)
            return self.portasUSB
        else:
            return []

    def __abrePorta(self, porta):
        if self.ser and self.ser.is_open:
            return
        else:
            self.ser = serial.Serial(port=porta, baudrate=115200, bytesize=8, parity="N", stopbits=1, timeout=0.2)
            if self.ser.is_open:
                return
    
    def mensagensParaEnviar(self, porta, info=[]):
        
        self.listaPortas()
        if self.portasUSB:
            porta = porta
            self.__abrePorta(porta)
            def enviaMensagem():
                msgBytes = bytes(info)
                self.ser.write(msgBytes)
                print("=========================================================================================================================================================================================================")
                print(" MINHA MENSAGEM:\n")  
                print(msgBytes)
                print("=========================================================================================================================================================================================================")
                              
                self.msg = self.ser.read(64)
                
                print("=========================================================================================================================================================================================================")
                print(" RESPOSTA:\n")  
                print(self.msg)
                print("=========================================================================================================================================================================================================")
            thread = threading.Thread(target=enviaMensagem)
            thread.start()
            thread.join()  

        return self.msg