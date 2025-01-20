from tkinter import *
from tkinter import ttk
from MandaSinal import MandaSinal

class Interface:
    def __init__(self, root):
        self.root = root
        self.mandaSinal = MandaSinal(self)
        
        self.cores()
        self.configTela()
        self.criaAbas()
        self.configAba()
        
        self.mandaSinal.configMandaSinal()
        
    def cores(self):
        self.pretoOliva = "#0D0B07"       
        self.carvao = "#262118"  
        self.cinzaOliva = "#595856"        
        self.cinzaOlivaClaro = "#8C8B88"  
        self.branco = "#ffffff"       
        self.cinzaClaro = "#BFBFBD"
        self.preto = "#090909"
        
    def configTela(self):
        self.root.title("Gravador Serial")
        self.root.geometry("500x550")
        self.root.resizable(False, False)
        
    def criaAbas(self):
        self.abas = ttk.Notebook(self.root) 
        self.abas.grid(row=0, column=0, sticky="nsew")
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
    def configAba(self):
        self.janelaMandaSinal = Frame(self.abas, bg=self.cinzaOliva) 
        self.abas.add(self.janelaMandaSinal, text="Gravador serial")

        self.configuracoes = Frame(self.abas, bg=self.cinzaOliva) 
        self.abas.add(self.configuracoes, text="Configurações")
    