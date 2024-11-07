from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry

from GravadorSerial import GravadorSerial
import serial

class MandaSinal:    
    def __init__(self, interface):
        self.interface = interface
        self.gravadorSerial = GravadorSerial()
        self.bobina = None
        self.labelLoteData = None
        
    def atualizaBobina(self, bobina):
        self.bobina = bobina
        print(f"Bobina atualizada para: {bobina}")
        
    def enviarBytes(self):
        try:
            self.lote = self.numeroLote.get()
            self.numeroVersao = self.versaoPlacaNumero.get()
            data = self.dateEntry.get_date()

            if self.lote > 255 or self.numeroVersao > 255:
                messagebox.showerror("Erro", "Coloque números referentes à 2 Bytes/2 Bits (0 à 255)")
                print("Coloque números referentes à 2 Bytes/2 Bits (0 à 255)")
                return
            
            dia = data.day
            mes = data.month
            ano = data.year % 100

            if self.bobina == "Placa Potência":
                placaByte = 0x01
            elif self.bobina == "Placa Temperatura":
                placaByte = 0x02
            elif self.bobina == "Placa Bobina":
                placaByte = 0x03
            else:
                messagebox.showerror("Erro", "Bobina não encontrada")
            
            fill = [0x00] * 3
            
            opcode = 5
            
            

            cabecalho = [0xAA, 0xBB, 0x00, placaByte, opcode]
            def checksum():
                return sum(fill + [placaByte, 5, int(self.lote), dia, mes, ano, 170, 187, self.numeroVersao])
            
            print(checksum())
            
            self.gravadorSerial.mensagensParaEnviar(info = cabecalho + fill + [self.lote, dia, mes, ano, self.numeroVersao] + (fill * 16) + [0x00] + [checksum() & 0x00FF] + [checksum() >> 8])
            
            if self.labelLoteData:
                self.labelLoteData.config(text=f"Lote: {self.lote} | Dia: {dia} | Mês: {mes} | Ano: {ano}")
                self.resposta.config(text=f"Resposta: {self.gravadorSerial.msg}")
                
            else:
                frame = Frame(self.interface.janelaMandaSinal, bg=self.interface.cinza)
                self.labelLoteData = Label(frame, text=f"Lote: {self.lote} | Dia: {dia} | Mês: {mes} | Ano: {ano} | Versão: {self.numeroVersao}", bg=self.interface.cinzaClaro, fg=self.interface.branco)
                self.labelLoteData.pack(pady=(10, 0))
                frame.pack(pady=5)
                
                frame2 = Frame(self.interface.janelaMandaSinal, bg=self.interface.cinza)
                self.resposta = Label(frame, text=f"resposta: {self.gravadorSerial.msg}", bg=self.interface.cinzaClaro, fg=self.interface.branco, wraplength=300)
                self.resposta.pack(pady=(10, 0))
                frame2.pack(pady=5)
                
        except serial.SerialException:
            print("Erro ao conectar ao serial")
        
    def criarEntry(self, texto, numeroEntry, janela):
        frame = Frame(janela, bg=self.interface.cinza)
        label = Label(frame, text=texto, bg=self.interface.cinza, fg=self.interface.branco)
        label.pack(pady=(10, 0))
        self.entry = Entry(frame, bg=self.interface.cinzaClaro, fg=self.interface.branco, textvariable=numeroEntry)
        self.entry.pack(pady=(0, 10)) 
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
        self.versaoPlacaNumero = IntVar()
        
        
        self.lote = self.criarEntry("Lote", self.numeroLote, self.interface.janelaMandaSinal)
        self.versaoPlaca = self.criarEntry("Versão da Placa", self.versaoPlacaNumero, self.interface.janelaMandaSinal)
        self.data = self.criarDateEntry("Data", self.interface.janelaMandaSinal)
        
        self.enviar = self.criarButton("Enviar", self.interface.janelaMandaSinal, self.enviarBytes)
    
