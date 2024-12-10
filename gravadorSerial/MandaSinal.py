from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar, Calendar
from GravadorSerial import GravadorSerial
import datetime
import serial

class MandaSinal:
    def __init__(self, interface):
        self.interface = interface
        self.gravadorSerial = GravadorSerial()
        self.bobina = None
        self.resposta = None
        self.msgEstruturada = None
        self.dia = None
        self.mes = None
        self.ano = None
        self.lote = None
        self.numeroVersao = None
        self.numeroVersao2 = None
        self.placaByte = None
        self.placaNome = ""
        self.criarRespostaCerta = Label()
        self.interface.root.bind("<Return>", self.gravaBytesNaSerial)
        
    def nomeDaPlaca(self, placaNome):
        self.bobina = placaNome
        
    def criaTabelaComInformacoes(self): 
        self.leRespostaDaSerial()
        if self.resposta:
            self.resposta.config(state=NORMAL)
            
            self.resposta.delete(1.0, END) 
            
            self.resposta.insert(END, f"{'Placa Bobina' if self.placaByte == 0x03 else 'Placa Temperatura' if self.placaByte == 0x02 else 'Placa Potência'}: {self.msgEstruturada}")
            
            self.resposta.config(state=DISABLED)
        else:
            frame2 = Frame(self.interface.janelaMandaSinal, bg=self.interface.cinzaOliva)
            frame2.pack(pady=5, fill="both", expand=True)

            scrollbar = Scrollbar(frame2)
            scrollbar.pack(side="right", fill="y")

            self.resposta = Text(frame2, bg=self.interface.cinzaOlivaClaro, fg=self.interface.branco, wrap=WORD, yscrollcommand=scrollbar.set, height=10, width=40)
            self.resposta.pack(side="left", fill="both", expand=True)

            scrollbar.config(command=self.resposta.yview)

            self.resposta.config(state=NORMAL)
            
            self.resposta.insert(END, f"{'Placa Bobina' if self.placaByte == 0x03 else 'Placa Temperatura' if self.placaByte == 0x02 else 'Placa Potência'}: {self.msgEstruturada}")
            self.resposta.config(state=DISABLED)
    
    def leRespostaDaSerial(self):
        if self.placaByte == 1:
            return
        
        elif self.placaByte == 2:
            return
        
        elif self.placaByte == 3:
            self.msgEstruturada = f"""
    Lote: {self.gravadorSerial.msg[20]} 
    Dia: {self.gravadorSerial.msg[21]} 
    Mês: {self.gravadorSerial.msg[22]} 
    Ano: {(self.gravadorSerial.msg[23] + 1970)} 
    Ano unix: {(self.gravadorSerial.msg[23])} 
    Versão: {int.from_bytes(self.gravadorSerial.msg[24:26], byteorder="little")} 
    FirmWare: {int.from_bytes(self.gravadorSerial.msg[26:28], byteorder="little")} 
    qmtdPulsos: {int.from_bytes(self.gravadorSerial.msg[16:20], byteorder="little")}
                """
        
        else:
            return    
           
    def gravaBytesNaSerial(self, event = None): 
        try:
            definirSerial = 0x05
            
            self.lote = self.numeroLote.get()
            self.numeroVersao = self.versaoPlacaNumero.get()
            self.numeroVersao2 = self.versaoPlacaNumero2.get()
            data = self.calendar.get_date()

            if self.lote > 255 or self.numeroVersao > 255 or self.numeroVersao2 > 255:
                messagebox.showerror("Erro", "Coloque números referentes à 2 Bytes/2 Bits (0 à 255)")
                return
            
            dia, mes, ano = map(int, data.split('/'))
            print(f"Data Selecionada: {data}")

            ano = int(ano)
            mes = int(mes)
            dia = int(dia)
            
            self.dia = dia
            self.mes = mes
            self.ano = ano % 100
            
            epochAno = ano - 1970
            
            if self.bobina == "Placa Potência":
                self.placaByte = 0x01
            elif self.bobina == "Placa Temperatura":
                self.placaByte = 0x02
            elif self.bobina == "Placa Bobina":
                self.placaByte = 0x03
            else:
                messagebox.showerror("Erro", "Placa não encontrada")
                return

            fill = [0x00] 
            opcode = definirSerial

            if opcode == definirSerial:
                cabecalho = [0xAA, 0xBB, 0x00, self.placaByte, opcode]
                def checksum():
                    return sum(fill + [self.placaByte, 5, int(self.lote), self.dia, self.mes, epochAno, 170, 187, self.numeroVersao, self.numeroVersao2])
                
                self.gravadorSerial.mensagensParaEnviar(info = cabecalho + (fill * 3) + [self.lote, self.dia, self.mes, epochAno, self.numeroVersao, self.numeroVersao2] + (fill * 48) + [checksum() & 0x00FF] + [checksum() >> 8])

            else:
                messagebox.showerror("Erro", "Algo está errado")
            
            self.leRespostaDaSerial()
            self.criaTabelaComInformacoes()

        except serial.SerialException:
            print("Erro ao conectar ao serial")


    def leOqueTemDentroDaSerial(self):
        pedirStatus = 0
        opcode = pedirStatus
        fill = [0x00]
        self.placaByte = 1

        for i in range(1, 4):
            if opcode == pedirStatus:
                cabecalho = [0xAA, 0xBB, 0x00, self.placaByte, opcode]
                def checksum():
                    return sum(fill + [self.placaByte, opcode, 170, 187])

                self.gravadorSerial.mensagensParaEnviar(info=cabecalho + (fill * 57) + [checksum() & 0x00FF] + [checksum() >> 8])
                if len(self.gravadorSerial.msg) != 0:
                    if i == 1:
                        messagebox.showinfo("Placa ", "Placa mudada para: Placa Potência")
                        self.placaNome = "Placa Potência"
                    elif i == 2:
                        messagebox.showinfo("Placa ", "Placa mudada para: Placa Temperatura")
                        self.placaNome = "Placa Temperatura"
                    elif i == 3:
                        messagebox.showinfo("Placa ", "Placa mudada para: Placa Bobina")
                        self.placaNome = "Placa Bobina"
                        
                    else:
                        messagebox.showerror("Placa ", "Placa: Erro ao encontrar placa")
                        break
                    
                    self.nomeDaPlaca(self.placaNome)
                    
                    self.criaTabelaComInformacoes()

            self.placaByte += 1
        self.leRespostaDaSerial()
    
    def criaEntry(self, texto, numeroEntry, janela):
        frame = Frame(janela, bg=self.interface.cinzaOliva)
        label = Label(frame, text=texto, bg=self.interface.cinzaOliva, fg=self.interface.branco)
        label.pack(pady=(10, 0))
        self.entry = Entry(frame, bg=self.interface.cinzaOlivaClaro, fg=self.interface.branco, textvariable=numeroEntry)
        self.entry.pack(pady=(0, 10)) 
        frame.pack(pady=5) 
        
    def criaCalendar(self, texto, janela):
        frame = Frame(janela, bg=self.interface.cinzaOliva)
        label = Label(frame, text=texto, bg=self.interface.cinzaOliva, fg=self.interface.branco)
        label.pack(pady=(10, 0))
        self.calendar = Calendar(frame, bg=self.interface.cinzaOlivaClaro, fg=self.interface.branco, width = 12, borderwidth = 2, mindate=datetime.date(1970, 1, 1), maxdate=datetime.date(2225, 12, 31), selectmode='day', date_pattern='dd/mm/yyyy')
        self.calendar.pack(pady=(0, 10)) 
        frame.pack(pady=5) 
        
    def criaLabel(self, texto, resposta, janela):
        frame = Frame(janela, bg=self.interface.cinzaOliva)
        label = Label(frame, text=texto, bg=self.interface.cinzaOliva, fg=self.interface.branco)
        label.pack(pady=(10, 0))
        label2 = Label(frame, text=resposta,bg=self.interface.cinzaOlivaClaro, fg=self.interface.branco, width = 12, borderwidth = 2)
        label2.pack(pady=(0, 10)) 
        frame.pack(pady=5) 
        
    def criaButton(self, texto, janela, comando):
        frame = Frame(janela, bg=self.interface.cinzaOliva)
        button = Button(frame, bg=self.interface.cinzaOlivaClaro, fg=self.interface.branco, text=texto, command=comando)
        button.pack(pady=10) 
        frame.pack(pady=5) 
        
    def configMandaSinal(self):
        self.numeroLote = IntVar() 
        self.versaoPlacaNumero = IntVar()
        self.versaoPlacaNumero2 = IntVar()
        
        self.lote = self.criaEntry("Lote", self.numeroLote, self.interface.janelaMandaSinal)
        self.versaoPlaca = self.criaEntry("Versão da Placa", self.versaoPlacaNumero, self.interface.janelaMandaSinal)
        self.versaoPlaca2 = self.criaEntry("Versão da Placa", self.versaoPlacaNumero2, self.interface.janelaMandaSinal)
        self.data = self.criaCalendar("Data", self.interface.janelaMandaSinal)
        
        self.ler = self.criaButton("Identificar Placa", self.interface.janelaMandaSinal, self.leOqueTemDentroDaSerial)
        self.enviar = self.criaButton("Gravar Dados", self.interface.janelaMandaSinal, self.gravaBytesNaSerial)