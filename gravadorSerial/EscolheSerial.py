from tkinter import *

class EscolheSerial:
    def __init__(self, interface, mandaSinal):
        self.interface = interface
        self.mandaSinal = mandaSinal
        self.guardaBobina = None
        
    def criarMenuButton(self, texto, janela):
        # Criando o frame onde o menu vai ser exibido
        frame = Frame(janela, bg=self.interface.cinza)
        
        # Criando o Menubutton e empacotando
        self.menuButton = Menubutton(frame, text=texto, bg=self.interface.cinzaClaro, fg=self.interface.branco)
        self.menuButton.pack(pady=10)  # O Menubutton usa pack(), então será posicionado dentro do frame
        
        menu = Menu(self.menuButton, tearoff=0)
        self.menuButton.config(menu=menu)
        
        # Adicionando opções ao menu do Menubutton
        menu.add_command(label="Placa Potência", command=lambda: self.selecionar_bobina("Placa Potência"))
        menu.add_command(label="Placa Temperatura", command=lambda: self.selecionar_bobina("Placa Temperatura"))
        menu.add_command(label="Placa Bobina", command=lambda: self.selecionar_bobina("Placa Bobina"))
        
        frame.pack(pady=5)  # Empacota o frame na janela, abaixo dos outros widgets
        
    def configMenuButton(self):
        # Inicializando o MenuButton
        self.bobina1 = self.criarMenuButton("Escolher Placa", self.interface.janelaMandaSinal)
    
    def selecionar_bobina(self, bobina):
        # Alterando o texto do Menubutton ao invés de destruí-lo
        if bobina == "Placa Potência":
            self.menuButton.config(text="Placa Potência")  # Alterando o texto
            print("Você selecionou a Placa Potência")
        
        elif bobina == "Placa Temperatura":
            self.menuButton.config(text="Placa Temperatura")  # Alterando o texto
            print("Você selecionou a Placa Temperatura")
        
        else:
            self.menuButton.config(text="Placa Bobina")  # Alterando o texto
            print("Você selecionou a Placa Bobina")
        
        # Atualizando a variável que guarda a bobina selecionada
        self.guardaBobina = bobina
        self.mandaSinal.atualizaBobina(bobina)
