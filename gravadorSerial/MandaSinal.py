from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry, Calendar
from EscolheSerial import EscolheSerial
from GravadorSerial import GravadorSerial
import datetime
import serial

class MandaSinal:
    def __init__(self, interface):
        self.interface = interface
        self.gravadorSerial = GravadorSerial()
        self.escolheSerial = EscolheSerial(interface, self) 
        self.bobina = None
        self.labelLoteData = None
        self.msgEstruturada = None
        self.dia = None
        self.mes = None
        self.ano = None
        self.lote = None
        self.numeroVersao = None
        self.placaByte = None
        self.placaNome = ""
        self.criarRespostaCerta = Label()
        self.interface.root.bind("<Return>", self.enviarBytes)
        
    def atualizaBobina(self, bobina):
        self.bobina = bobina
        print(f"Placa Atual: {bobina}")
        
    def atualizarMenuButton(self, placaNome):
        self.escolheSerial.menuButton.config(text=placaNome)
        self.bobina = placaNome
        
    def criaTabelaComInformacoes(self):
        if self.labelLoteData:
            self.labelLoteData.config(text=f"Lote: {self.lote} | Dia: {self.dia} | Mês: {self.mes} | Ano: {self.ano} | Versão: {self.numeroVersao}")
            
            self.resposta.config(state=NORMAL)
            
            self.resposta.delete(1.0, END)
            self.resposta.insert(END, f"{'Placa Bobina' if self.placaByte == 0x03 else 'Placa Temperatura' if self.placaByte == 0x02 else 'Placa Potência'}: {self.msgEstruturada}")
            
            self.resposta.config(state=DISABLED)
            
        else:
            frame = Frame(self.interface.janelaMandaSinal, bg=self.interface.cinzaOliva)
            self.labelLoteData = Label(frame, text=f"Lote: {self.lote} | Dia: {self.dia} | Mês: {self.mes} | Ano: {self.ano} | Versão: {self.numeroVersao}", bg=self.interface.cinzaOlivaClaro, fg=self.interface.branco)
            self.labelLoteData.pack(pady=(10, 0))
            frame.pack(pady=5)

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
                    
    def enviarBytes(self, event = None): 
        try:
            definirSerial = 0x05
            
            self.lote = self.numeroLote.get()
            self.numeroVersao = self.versaoPlacaNumero.get()
            data = self.dateEntry.get_date()

            if self.lote > 255 or self.numeroVersao > 255:
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
                    return sum(fill + [self.placaByte, 5, int(self.lote), self.dia, self.mes, epochAno, 170, 187, self.numeroVersao])

                self.gravadorSerial.mensagensParaEnviar(info = cabecalho + (fill * 3) + [self.lote, self.dia, self.mes, epochAno, self.numeroVersao] + (fill * 49) + [checksum() & 0x00FF] + [checksum() >> 8])

            else:
                messagebox.showerror("Erro", "Algo está errado")
            
            self.msgEstruturada = f"""
    Lote: {self.gravadorSerial.msg[20]} 
    Dia: {self.gravadorSerial.msg[21]} 
    Mês: {self.gravadorSerial.msg[22]} 
    Ano: {(self.gravadorSerial.msg[23] + 1970)} 
    Versão: {int.from_bytes(self.gravadorSerial.msg[24:26], byteorder="little")} 
    FirmWare: {int.from_bytes(self.gravadorSerial.msg[26:28], byteorder="little")} 
    qmtdPulsos: {int.from_bytes(self.gravadorSerial.msg[16:20], byteorder="little")}
            """
            
            self.criaTabelaComInformacoes()

        except serial.SerialException:
            print("Erro ao conectar ao serial")

    def lerSerial(self):
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
                    
                    self.atualizarMenuButton(self.placaNome)
                    
                    self.criaTabelaComInformacoes()

            self.placaByte += 1

    def criarEntry(self, texto, numeroEntry, janela):
        frame = Frame(janela, bg=self.interface.cinzaOliva)
        label = Label(frame, text=texto, bg=self.interface.cinzaOliva, fg=self.interface.branco)
        label.pack(pady=(10, 0))
        self.entry = Entry(frame, bg=self.interface.cinzaOlivaClaro, fg=self.interface.branco, textvariable=numeroEntry)
        self.entry.pack(pady=(0, 10)) 
        frame.pack(pady=5) 
        
    def criarDateEntry(self, texto, janela):
        frame = Frame(janela, bg=self.interface.cinzaOliva)
        label = Label(frame, text=texto, bg=self.interface.cinzaOliva, fg=self.interface.branco)
        label.pack(pady=(10, 0))
        self.dateEntry = Calendar(frame, bg=self.interface.cinzaOlivaClaro, fg=self.interface.branco, width = 12, borderwidth = 2, mindate=datetime.date(1970, 1, 1), maxdate=datetime.date(9999, 12, 31), selectmode='day', date_pattern='dd/mm/yyyy')
        self.dateEntry.pack(pady=(0, 10)) 
        frame.pack(pady=5) 
        
    def criarLabel(self, texto, resposta, janela):
        frame = Frame(janela, bg=self.interface.cinzaOliva)
        label = Label(frame, text=texto, bg=self.interface.cinzaOliva, fg=self.interface.branco)
        label.pack(pady=(10, 0))
        label2 = Label(frame, text=resposta,bg=self.interface.cinzaOlivaClaro, fg=self.interface.branco, width = 12, borderwidth = 2)
        label2.pack(pady=(0, 10)) 
        frame.pack(pady=5) 
        
    def criarButton(self, texto, janela, comando):
        frame = Frame(janela, bg=self.interface.cinzaOliva)
        button = Button(frame, bg=self.interface.cinzaOlivaClaro, fg=self.interface.branco, text=texto, command=comando)
        button.pack(pady=10) 
        frame.pack(pady=5) 
        
    def configMandaSinal(self):
        self.numeroLote = IntVar() 
        self.versaoPlacaNumero = IntVar()
        
        self.lote = self.criarEntry("Lote", self.numeroLote, self.interface.janelaMandaSinal)
        self.versaoPlaca = self.criarEntry("Versão da Placa", self.versaoPlacaNumero, self.interface.janelaMandaSinal)
        self.data = self.criarDateEntry("Data", self.interface.janelaMandaSinal)
        
        self.ler = self.criarButton("Identificar Placa", self.interface.janelaMandaSinal, self.lerSerial)
        self.enviar = self.criarButton("Gravar Dados", self.interface.janelaMandaSinal, self.enviarBytes)
