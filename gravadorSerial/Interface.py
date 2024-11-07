from tkinter import *
from tkinter import ttk
from MandaSinal import MandaSinal
from EscolheSerial import EscolheSerial

class Interface:
    def __init__(self, root):
        self.root = root
        self.mandaSinal = MandaSinal(self)
        self.escolheSerial = EscolheSerial(self, self.mandaSinal)
        
        self.cores()
        self.configTela()
        self.criaAbas()
        self.configAba()
        #self.configMsg()
        
        self.escolheSerial.configMenuButton()
        self.mandaSinal.configMandaSinal()
    def cores(self):
        self.preto = "#0D0D0D"
        self.cinzaEscuro = "#262626"
        self.cinza = "#404040"
        self.cinzaClaro = "#737373"
        self.branco = "#ffffff"
        
    def configTela(self):
        self.root.title("Gravador Serial")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
    def criaAbas(self):
        self.abas = ttk.Notebook(self.root) 
        self.abas.grid(row=0, column=0, sticky="nsew")
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
    def configAba(self):
        self.janelaMandaSinal = Frame(self.abas, bg=self.cinza) 
        self.abas.add(self.janelaMandaSinal, text="Gravador serial")
    

        