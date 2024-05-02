import serial
import serial.tools.list_ports

class SerialApp():
    def __init__(self):
        self.serialPort = serial.Serial()
        self.baudrate = [9600, 115200]
        self.portList = []
        
    def update_Port(self):
        self.portList = [port.device for port in serial.tools.list_ports.comports()]
        print(self.portList)
        
    def connect_Serial(self):
        try:
            self.serialPort.open()
        except:
            print("Erro ao tentar abrir a serial")
            
    def read_Serial(self):
        data_Read = self.serialPort.read(10).decode("UTF-8")
        print(data_Read)
        
    def send_Serial(self, data):
        if (self.serialPort.isOpen()):
            data_Send = str(self.data) + "\n"
            self.serialPort.write(data_Send.encode())
            self.serialPort.flushOutput()
            
    def close_Serial(self):
        self.serialPort.close()