from tkinter import *

class EscolheSerial:
    def __init__(self, interface, mandaSinal):
        self.interface = interface
        self.mandaSinal = mandaSinal
        self.guardaBobina = None
        self.menuButton = Menubutton()  
        
    def criarMenuButton(self, texto, janela):
        frame = Frame(janela, bg=self.interface.cinzaOliva)
        
        self.menuButton = Menubutton(frame, text=texto, bg=self.interface.cinzaOlivaClaro, fg=self.interface.branco)
        self.menuButton.pack(pady=10)  
        
        menu = Menu(self.menuButton, tearoff=0)
        self.menuButton.config(menu=menu)
        
        menu.add_command(label="Placa Potência", command=lambda: self.selecionarBobina("Placa Potência"))
        menu.add_command(label="Placa Temperatura", command=lambda: self.selecionarBobina("Placa Temperatura"))
        menu.add_command(label="Placa Bobina", command=lambda: self.selecionarBobina("Placa Bobina"))
        
        frame.pack(pady=5) 
        
    def configMenuButton(self):
        self.bobina1 = self.criarMenuButton("Escolher Placa", self.interface.janelaMandaSinal)
    
    def selecionarBobina(self, bobina):
        
        if bobina == "Placa Potência":
            self.menuButton.config(text="Placa Potência")  
            print("Você selecionou a Placa Potência")
        
        elif bobina == "Placa Temperatura":
            self.menuButton.config(text="Placa Temperatura")  
            print("Você selecionou a Placa Temperatura")
        
        else:
            self.menuButton.config(text="Placa Bobina")  
            print("Você selecionou a Placa Bobina")
        
        self.guardaBobina = bobina
        self.mandaSinal.atualizaBobina(bobina)
