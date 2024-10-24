import serial
import time
import struct

def create_CheckSum(cmd):

    # Calculate checksum over the first 38 bytes
    checksum = sum(cmd[:62]) & 0xFFFF
    checksum_bytes = struct.pack('<H', checksum)

    #checksum_bytes = b'\x00\x00'
    cmd = cmd + (checksum_bytes)

    return cmd

def printBobina(msg):

    # Convert bytes to integers using int.from_bytes()
    Address = msg[:4]
    adc1 = int.from_bytes(msg[4:6], byteorder='little')
    adc2 = int.from_bytes(msg[6:8], byteorder='little')
    adc3 = int.from_bytes(msg[8:10], byteorder='little')
    adc4 = int.from_bytes(msg[10:12], byteorder='little')
    adc5 = int.from_bytes(msg[12:14], byteorder='little')
    adc6 = int.from_bytes(msg[14:16], byteorder='little')
    QtdPulsos = msg[16:20]
    SerialNumberLSB = msg[20:24]
    SerialNumberMSB = msg[24:28]
    QtdErros = msg[28:32]
    fill = msg[32:40]
    fill64 = msg[40:62]
    CheckSum = msg[62:64]

    # Prints
    print("#########################################################################################")
    print(cmd) 
    print(msg)

    print("")
    print("Address.....: ",Address)
    print("ADCs: ", adc1, " / ", adc2,  " / ", adc3,  " / ", adc4,  " / ", adc5,  " / ", adc6)
    print("QtdPulsos...: ",QtdPulsos)
    print("SerialNumber: ",SerialNumberLSB)
    print("SerialNumber: ",SerialNumberMSB)
    print("QtdErros....: ",QtdErros)
    print("Checksum....: ",CheckSum)

# Example usage:,
header = b'\xAA\xBB\x00\x03'
opcode_value = 0    # 1 - inc / 2 - setserial / 3 - setpulses
data_value = 0
data2_value = 0

if(opcode_value != 0):
    cmd = struct.pack('<III', opcode_value, data_value, data2_value)
    cmd = header + cmd + b'\x00'*(24) + b'\x00'*(22)

else:
    cmd = struct.pack('<I', opcode_value)
    cmd = header + cmd + b'\x00'*(32) + b'\x00'*(22)

cmd = create_CheckSum(cmd)

ser = serial.Serial("COM5", 115200,8,"N",1,0.5)

while True:
    time.sleep(0.5)
    ser.write(cmd)
    msg=ser.read(64)

    printBobina(msg)


