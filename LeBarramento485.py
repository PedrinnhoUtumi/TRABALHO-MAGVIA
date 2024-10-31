import serial
import time
import struct
import math

def printTemp(msg):
    # Convert bytes to integers using int.from_bytes()
    Address = msg[:4]
    adc1 = int.from_bytes(msg[4:6], byteorder='little')
    adc2 = int.from_bytes(msg[6:8], byteorder='little')
    adc3 = int.from_bytes(msg[8:10], byteorder='little')
    adc4 = int.from_bytes(msg[10:12], byteorder='little')
    adc5 = int.from_bytes(msg[12:14], byteorder='little')
    adc6 = int.from_bytes(msg[14:16], byteorder='little')
    adc7 = int.from_bytes(msg[16:18], byteorder='little')
    adc8 = int.from_bytes(msg[18:20], byteorder='little')
    adc9 = int.from_bytes(msg[20:22], byteorder='little')
    adc10 = int.from_bytes(msg[22:24], byteorder='little')
    adc11 = int.from_bytes(msg[24:26], byteorder='little')
    CoolerPWM0Lido = int.from_bytes(msg[26:27], byteorder='little')
    CoolerPWM1Lido = int.from_bytes(msg[27:28], byteorder='little')
    BombaPWM0Lido = int.from_bytes(msg[28:29], byteorder='little')
    BombaPWM1Lido = int.from_bytes(msg[29:30], byteorder='little')
    CoolerFreq0 = int.from_bytes(msg[30:32], byteorder='little')
    CoolerFreq1 = int.from_bytes(msg[32:34], byteorder='little')
    SensorFluxoFreq = int.from_bytes(msg[34:36], byteorder='little')
    PerifericosOnOff = int.from_bytes(msg[36:38], byteorder='little')
    Fill = msg[38:40]
    CheckSum = msg[40:42]

    # Prints

    if(Address != b'\xAA\xBB\x00\x02'):
        return
    
    print(msg)
    print("")
    print("Address.....: ",Address)
    print("ADCs: ", adc1, " / ", adc2,  " / ", adc3,  " / ", adc4,  " / ", adc5,  " / ", adc6,  " / ", adc7,  " / ", adc8,  " / ", adc9,  " / ", adc10,  " / ", adc11)
    print("CoolerPWM0: ",CoolerPWM0Lido)
    print("CoolerPWM1: ",CoolerPWM1Lido)
    print("BombaPWM0: ",BombaPWM0Lido)
    print("BombaPWM1: ",BombaPWM1Lido)
    print("CoolerFreq0: ",CoolerFreq0)
    print("CoolerFreq1: ",CoolerFreq1)
    print("SensorFluxoFreq: ",SensorFluxoFreq)
    print("PerifericosOnOff: ",PerifericosOnOff)
    print("Fill: ",Fill)
    print("Checksum....: ",CheckSum)

ser = serial.Serial("COM5", 115200,8,"N",1,0.05)

while True:
    
    
    msg=ser.read(42)

    #lprint(msg)

    printTemp(msg)
