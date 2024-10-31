from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry

from GravadorSerial import GravadorSerial
import serial

class MandaSinal:    
    def __init__(self, interface):
        self.interface = interface
        self.gravadorSerial = GravadorSerial()
        
    def enviarBytes(self):
        try:
            self.lote = self.numeroLote.get()
            data = self.dateEntry.get_date()

            dia = data.day
            mes = data.month
            ano = data.year % 100

            self.gravadorSerial.mensagensParaEnviar(info = [self.lote, dia, mes, ano])
            
            frame = Frame(self.interface.janelaMandaSinal, bg=self.interface.cinza)
            label = Label(frame, text=f"lote: {self.lote} | dia: {dia} | mês: {mes} | ano: {ano}", bg=self.interface.cinzaClaro, fg=self.interface.branco)
            label.pack(pady=(10, 0))
            frame.pack(pady=5) 
        except serial.SerialException:
            print("Erro ao conectar ao serial")
        
    def criarEntry(self, texto, numeroEntry, janela):
        frame = Frame(janela, bg=self.interface.cinza)
        label = Label(frame, text=texto, bg=self.interface.cinza, fg=self.interface.branco)
        label.pack(pady=(10, 0))
        entry = Entry(frame, bg=self.interface.cinzaClaro, fg=self.interface.branco, textvariable=numeroEntry)
        entry.pack(pady=(0, 10)) 
        frame.pack(pady=5) 
        
    def criarDateEntry(self, texto, janela):
        frame = Frame(janela, bg=self.interface.cinza)
        label = Label(frame, text=texto, bg=self.interface.cinza, fg=self.interface.branco)
        label.pack(pady=(10, 0))
        self.dateEntry = DateEntry(frame, bg=self.interface.cinzaClaro, fg=self.interface.branco, width = 12, borderwidth = 2)
        self.dateEntry.pack(pady=(0, 10)) 
        frame.pack(pady=5) 
        
    def criarButton(self, texto, janela, comando):
        frame = Frame(janela, bg=self.interface.cinza)
        button = Button(frame, bg=self.interface.cinzaClaro, fg=self.interface.branco, text=texto, command=comando)
        button.pack(pady=10) 
        frame.pack(pady=5) 
        
    def configMandaSinal(self):
        self.numeroLote = IntVar() 

        self.lote = self.criarEntry("Lote", self.numeroLote, self.interface.janelaMandaSinal)
        self.data = self.criarDateEntry("Data", self.interface.janelaMandaSinal)
        
        self.enviar = self.criarButton("Enviar", self.interface.janelaMandaSinal, self.enviarBytes)
    
