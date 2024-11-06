from tkinter import *

class EscolheSerial:
    def __init__(self, interface):
        self.interface = interface
        
    def criarMenuButton(self, texto, janela):
        frame = Frame(janela, bg=self.interface.cinza)
        menuButton = Menubutton(frame, text=texto, bg=self.interface.cinzaClaro, fg=self.interface.branco)
        menuButton.pack(pady=(10, 0))
        
        menu = Menu(menuButton, tearoff=0)  
        menuButton.config(menu=menu)  
        
        menu.add_command(label="Bobina 1", command=lambda: self.selecionar_bobina("Placa Potência"))
        menu.add_command(label="Bobina 2", command=lambda: self.selecionar_bobina("Placa Temperatura"))  
        menu.add_command(label="Bobina 3", command=lambda: self.selecionar_bobina("Placa Bobina")) 
        
         
        
        frame.pack(pady=5) 

    def configMenuButton(self):
        self.bobina1 = self.criarMenuButton("Escolher Bobina", self.interface.janelaMandaSinal)

def selecionar_bobina(self, bobina):
    match bobina:
        case "Placa Potência":
            # Ação para Bobina 1
            print("Você selecionou a Placa Potência")
            # Coloque aqui o código para lidar com a "Placa Potência"
        case "Placa Temperatura":
            # Ação para Bobina 2
            print("Você selecionou a Placa Temperatura")
            # Coloque aqui o código para lidar com a "Placa Temperatura"
        case "Placa Bobina":
            # Ação para Bobina 3
            print("Você selecionou a Placa Bobina")
            # Coloque aqui o código para lidar com a "Placa Bobina"
        case _:
            # Caso o valor não seja um dos esperados
            print(f"Bobina desconhecida: {bobina}")

