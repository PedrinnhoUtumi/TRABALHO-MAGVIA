from serialApp import SerialApp
ser = SerialApp()
ser.update_Port()
ser.serialPort.port = "COM3"
ser.serialPort.baudrate = 9600
ser.connect_Serial()
contador = 0 
while (1):
    ser.read_Serial
    if contador >= 10:
        break
    ser.serialPort.write(contador)
    contador += 1
ser.close_Serial()
