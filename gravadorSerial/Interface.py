from tkinter import *
from tkinter import Tk
from tkinter import ttk


class Interface:
    def __init__(self, root):
        self.root = root
        mandaSinal = MandaSinal(self)
        self.cores()
        self.configTela()
        self.criaAbas()
        self.configAba()
        mandaSinal.configMandaSinal()
        
    def cores(self):
        self.preto = "#0D0D0D"
        self.cinzaEscuro = "#262626"
        self.cinza = "#404040"
        self.cinzaClaro = "#737373"
        self.branco = "#ffffff"
        
    def configTela(self):
        self.root.title("Interface")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        
    def criaAbas(self):
        self.abas = ttk.Notebook(self.root) 
        self.abas.grid(row=0, column=0, sticky="nsew")
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
    def configAba(self):
        self.janelaMandaSinal = Frame(self.abas, bg=self.cinza) 
        self.abas.add(self.janelaMandaSinal, text="Config Serial")

class MandaSinal:    
    def __init__(self, interface):
        self.interface = interface
        
    def criarEntry(self, texto, numeroEntry, janela):
        frame = Frame(janela, bg=self.interface.cinza)
        label = Label(frame, text=texto, bg=self.interface.cinza, fg=self.interface.branco)
        label.pack(pady=(10, 0))
        entry = Entry(frame, bg=self.interface.cinzaClaro, fg=self.interface.branco, textvariable=numeroEntry)
        entry.pack(pady=(0, 10)) 
        frame.pack(pady=5) 
    
    def criarLabel(self, texto, numeroEntry, janela):
        frame = Frame(janela, bg=self.interface.cinza)
        label = Label(frame, text=texto, bg=self.interface.cinza, fg=self.interface.branco)
        label = Label(frame, textvariable=numeroEntry, bg=self.interface.cinza, fg=self.interface.branco)
        label.pack(pady=(10, 0))
        frame.pack(pady=5) 
        
    def criarButton(self, texto, janela, comando = 0):
        frame = Frame(janela, bg=self.interface.cinza)
        button = Button(frame, bg=self.interface.cinzaClaro, fg=self.interface.branco, text=texto, command=comando)
        button.pack(pady=10) 
        frame.pack(pady=5) 
        
    def configMandaSinal(self):
        self.numeroLote = IntVar() 
        self.numeroDia = IntVar()
        self.numeroMes = IntVar()
        self.numeroAno = IntVar()
        
        self.lote = self.criarEntry("Lote", self.numeroLote, self.interface.janelaMandaSinal)
        self.dia = self.criarEntry("Dia", self.numeroDia, self.interface.janelaMandaSinal)
        self.mes = self.criarEntry("Mês", self.numeroMes, self.interface.janelaMandaSinal)
        self.ano = self.criarEntry("Ano", self.numeroAno, self.interface.janelaMandaSinal)
        
        self.enviar = self.criarButton("Enviar", self.interface.janelaMandaSinal)