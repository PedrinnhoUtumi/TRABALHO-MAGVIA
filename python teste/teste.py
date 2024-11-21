a = b'\xaa\xbb\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00h\x01'

print(len(a))
import serial.tools.list_ports

# Listar todas as portas seriais
def listar_portas_seriais():
    portas = serial.tools.list_ports.comports()
    if portas:
        print("Portas seriais disponíveis:")
        for porta in portas:
            print(f"{porta.device}: {porta.description}")
    else:
        print("Nenhuma porta serial encontrada.")

# Chama a função para listar as portas seriais
listar_portas_seriais()
