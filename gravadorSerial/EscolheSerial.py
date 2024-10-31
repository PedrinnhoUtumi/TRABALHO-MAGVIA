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
        
        menu.add_command(label="Bobina 1", command=lambda: self.selecionar_bobina("Bobina 1"))
        menu.add_command(label="Bobina 2", command=lambda: self.selecionar_bobina("Bobina 2"))  
        menu.add_command(label="Bobina 3", command=lambda: self.selecionar_bobina("Bobina 3"))  
        
        frame.pack(pady=5) 

    def configMenuButton(self):
        self.bobina1 = self.criarMenuButton("Escolher Bobina", self.interface.janelaMandaSinal)

    def selecionar_bobina(self, bobina):
        print(f"Você selecionou: {bobina}")
