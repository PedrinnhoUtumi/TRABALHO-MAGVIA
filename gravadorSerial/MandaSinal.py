from tkinter import *
from tkcalendar import Calendar
from GravadorSerial import GravadorSerial
import datetime
import time
import serial
import threading


class MandaSinal:
    def __init__(self, interface):
        self.interface = interface
        self.gravadorSerial = GravadorSerial()
        self.POTENCIA = 0x01
        self.TEMPERATURA = 0x02
        self.BOBINA = 0x03
        self.TAMANHODARESPOSTA = 64
        self.abrirPorta = None
        self.placa = None
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
        self.label = None
        self.menu = None
        self.portas = self.gravadorSerial.listaPortas()
        self.interface.root.bind("<Return>", self.__gravaBytesNaSerial)
        
    def __nomeDaPlaca(self, placaNome):
        self.placa = placaNome
        
    def __criaTabelaComInformacoes(self, status):
        if status == True:
            self.__leRespostaDaSerial()
            if self.resposta:
                self.resposta.config(state=NORMAL, bg=self.interface.cinzaOlivaClaro, fg=self.interface.preto)
                
                self.resposta.delete(1.0, END) 
                
                self.resposta.insert(END, f"{'Placa Bobina' if self.placaByte == self.BOBINA else 'Placa Temperatura' if self.placaByte == self.TEMPERATURA else 'Placa Potência'}: {self.msgEstruturada}")
                
                self.resposta.config(state=DISABLED)
            else:        
                frame = Frame(self.interface.janelaMandaSinal, bg=self.interface.cinzaOliva)
                frame.pack(pady=5, fill="both", expand=True)
                
                self.scrollbar = Scrollbar(frame)
                self.scrollbar.pack(side="right", fill="y")
                
                self.resposta = Text(frame, bg=self.interface.cinzaOlivaClaro, fg=self.interface.preto, wrap=WORD, yscrollcommand=self.scrollbar.set, height=10, width=40)
                self.resposta.pack(side="left", fill="both", expand=True)

                self.scrollbar.config(command=self.resposta.yview)

                self.resposta.config(state=NORMAL)

                self.resposta.insert(END, f"{'Placa Bobina' if self.placaByte == self.BOBINA else 'Placa Temperatura' if self.placaByte == self.TEMPERATURA else 'Placa Potência'}: {self.msgEstruturada}")
                self.resposta.config(state=DISABLED)
        else:
            if self.resposta:
                self.resposta.config(state=NORMAL, bg=self.interface.vermelho, fg=self.interface.branco)
                
                self.resposta.delete(1.0, END) 
                self.resposta.insert(END, "Erro na conexão com a serial")
                self.resposta.config(state=DISABLED)
                
            else:
                return
      
    def __leRespostaDaSerial(self):
        if self.placaByte == self.POTENCIA:
            if len(self.gravadorSerial.msg) == self.TAMANHODARESPOSTA:
                self.msgEstruturada = f"""
    Lote: {self.gravadorSerial.msg[54]} 
    Dia: {self.gravadorSerial.msg[55]} 
    Mês: {self.gravadorSerial.msg[56]} 
    Ano: {(self.gravadorSerial.msg[57] + 1970)} 
    Versão: {int.from_bytes(self.gravadorSerial.msg[58:60], byteorder="little")} 
    FirmWare: {int.from_bytes(self.gravadorSerial.msg[60:62], byteorder="little")} 
                """
            else:
                return
        
        elif self.placaByte == self.TEMPERATURA:
            if len(self.gravadorSerial.msg) == self.TAMANHODARESPOSTA:
                self.msgEstruturada = f"""
    Lote: {self.gravadorSerial.msg[54]} 
    Dia: {self.gravadorSerial.msg[55]} 
    Mês: {self.gravadorSerial.msg[56]} 
    Ano: {(self.gravadorSerial.msg[57] + 1970)} 
    Versão: {int.from_bytes(self.gravadorSerial.msg[58:60], byteorder="little")} 
    FirmWare: {int.from_bytes(self.gravadorSerial.msg[60:62], byteorder="little")} 
                """
            else:
                return
        
        elif self.placaByte == self.BOBINA:
            if len(self.gravadorSerial.msg) == self.TAMANHODARESPOSTA:
                self.msgEstruturada = f"""
    Lote: {self.gravadorSerial.msg[20]} 
    Dia: {self.gravadorSerial.msg[21]} 
    Mês: {self.gravadorSerial.msg[22]} 
    Ano: {(self.gravadorSerial.msg[23] + 1970)} 
    Versão: {int.from_bytes(self.gravadorSerial.msg[24:26], byteorder="little")} 
    FirmWare: {int.from_bytes(self.gravadorSerial.msg[26:28], byteorder="little")} 
    qntdPulsos: {int.from_bytes(self.gravadorSerial.msg[16:20], byteorder="little")}
                """
            else:
                return
        
        else:
            return    
           
    def __gravaBytesNaSerial(self, event = None):
        if not self.gravadorSerial.ser or not self.gravadorSerial.ser.is_open:
            self.__editaLabel("Impossível de gravar: serial desconectada✘", [self.report])
            self.__editaLabel("Desconectado", [self.conectadoOuNao], novaCorBG=self.interface.vermelho, novaCorFG=self.interface.branco)
            self.__criaTabelaComInformacoes(False)
            return  
        
        try:
            definirSerial = 0x05
            
            self.lote = self.numeroLote.get()
            self.numeroVersao = self.versaoPlacaNumero.get()
            self.numeroVersao2 = self.versaoPlacaNumero2.get()
            data = self.calendar.get_date()

            if self.lote > 255 or self.numeroVersao > 255 or self.numeroVersao2 > 255:
                self.__editaLabel("Erro: Coloque números referentes à 2 Bytes(0 à 255)", [self.report])
                return
            
            dia, mes, ano = map(int, data.split('/'))

            ano = int(ano)
            mes = int(mes)
            dia = int(dia)
            
            self.dia = dia
            self.mes = mes
            self.ano = ano % 100
            
            epochAno = ano - 1970
            if self.placa == "Placa Potência":
                self.placaByte = self.POTENCIA
            elif self.placa == "Placa Temperatura":
                self.placaByte = self.TEMPERATURA
            elif self.placa == "Placa Bobina":
                self.placaByte = self.BOBINA
            else:
                self.__editaLabel("Impossível de gravar: serial desconectada✘", [self.report])
                self.__criaTabelaComInformacoes(False)
                return

            fill = [0x00] 
            opcode = definirSerial

            if opcode == definirSerial:
                cabecalho = [0xAA, 0xBB, 0x00, self.placaByte, opcode]
                def __checksum():
                    return sum(fill + [self.placaByte, 5, int(self.lote), self.dia, self.mes, epochAno, 170, 187, self.numeroVersao, self.numeroVersao2])
                
                self.gravadorSerial.mensagensParaEnviar(porta = self.abrirPorta, info = cabecalho + (fill * 3) + [self.lote, self.dia, self.mes, epochAno, self.numeroVersao, self.numeroVersao2] + (fill * 48) + [__checksum() & 0x00FF] + [__checksum() >> 8])

            else:
                self.__editaLabel("Impossível de gravar: serial desconectada✘", [self.report])
                self.__criaTabelaComInformacoes(False)
            
            if len(self.gravadorSerial.msg) == self.TAMANHODARESPOSTA:
                self.__leRespostaDaSerial()
                self.__editaLabel("Informações gravadas com sucesso✔", [self.report])
                self.__editaLabel("Conectado", [self.conectadoOuNao], novaCorBG=self.interface.verde, novaCorFG=self.interface.preto)
                self.__criaTabelaComInformacoes(True)
            else:
                self.__editaLabel("Impossível de gravar: serial desconectada✘", [self.report])
                self.__criaTabelaComInformacoes(False)
                
        except serial.SerialException:
            self.__editaLabel("Impossível de gravar: serial desconectada✘", [self.report])
            self.__criaTabelaComInformacoes(False)

    def __leOqueTemDentroDaSerial(self):
        if not self.gravadorSerial.ser or not self.gravadorSerial.ser.is_open:
            self.__editaLabel("Impossível de ler: serial desconectada✘", [self.report])
            self.__editaLabel("Desconectado", [self.conectadoOuNao], novaCorBG=self.interface.vermelho, novaCorFG=self.interface.branco)
            self.__criaTabelaComInformacoes(False)
            return  
        
        pedirStatus = 0
        opcode = pedirStatus
        fill = [0x00]
        self.placaByte = 1


        for i in range(1, 4):
            if opcode == pedirStatus:
                cabecalho = [0xAA, 0xBB, 0x00, self.placaByte, opcode]
                def __checksum():
                    return sum(fill + [self.placaByte, opcode, 170, 187])

                try:
                    self.gravadorSerial.mensagensParaEnviar(porta = self.abrirPorta, info=cabecalho + (fill * 57) + [__checksum() & 0x00FF] + [__checksum() >> 8])
                    if self.gravadorSerial.ser.is_open:
                        if not self.gravadorSerial.portasUSB:
                            self.__editaLabel("Impossível de ler: serial desconectada✘", [self.report])
                            self.__criaTabelaComInformacoes(False)
                            raise serial.SerialException
                        elif len(self.gravadorSerial.msg) != 0 and self.gravadorSerial.portasUSB != []:
                            if i == 1:
                                self.placaNome = "Placa Potência"
                            elif i == 2:
                                self.placaNome = "Placa Temperatura"
                            elif i == 3:
                                self.placaNome = "Placa Bobina"
                            
                            self.__nomeDaPlaca(self.placaNome)
                            self.__editaLabel("Placa identificada com sucesso✔", [self.report])
                            self.__editaLabel("Conectado", [self.conectadoOuNao], novaCorBG=self.interface.verde, novaCorFG=self.interface.preto)
                            self.__criaTabelaComInformacoes(True)
                            break
                        else:
                            self.__editaLabel("Impossível de ler: serial desconectada✘", [self.report])
                            self.__criaTabelaComInformacoes(False)
                            raise serial.SerialException
                    else:
                        self.__editaLabel("Impossível de ler: serial desconectada✘", [self.report])
                        self.__criaTabelaComInformacoes(False)
                        raise serial.SerialException
                except serial.SerialException as e:
                    self.__editaLabel(f"Impossível de ler: serial desconectada✘", [self.report])
                    self.__editaLabel("Desconectado", [self.conectadoOuNao], novaCorBG=self.interface.vermelho, novaCorFG=self.interface.branco)
                    self.__criaTabelaComInformacoes(False)
            self.placaByte += 1
        self.__leRespostaDaSerial()      
    
    def __criaEntry(self, texto, numeroEntry, janela):
        frame = Frame(janela, bg=self.interface.cinzaOliva)
        label = Label(frame, text=texto, bg=self.interface.cinzaOliva, fg=self.interface.branco)
        label.pack(pady=(5, 0), padx=10)
        
        self.entry = Entry(frame, bg=self.interface.cinzaOlivaClaro, fg=self.interface.preto, textvariable=numeroEntry, width = 16)
        self.entry.pack(pady=(0, 10), padx=10) 
        frame.pack(pady=5, side=TOP, anchor="e") 
        
    def __criaCalendar(self, texto, janela):
        frame = Frame(janela, bg=self.interface.cinzaOliva)
        label = Label(frame, text=texto, bg=self.interface.cinzaOliva, fg=self.interface.branco)
        label.pack(pady=(10, 0), padx=10)
        self.calendar = Calendar(frame, bg=self.interface.cinzaOlivaClaro, fg=self.interface.preto, width = 12, borderwidth = 2, mindate=datetime.date(1970, 1, 1), maxdate=datetime.date(2225, 12, 31), selectmode='day', date_pattern='dd/mm/yyyy')
        self.calendar.pack(pady=(0, 10), padx=10) 
        frame.pack(pady=5, side=TOP, anchor="nw") 
        
    def __criaLabel(self, resposta, janela, tamanho, corBG, corFG, corFGTitulo = None, corBGTitulo = None, texto = None, semTitulo = None):
        if semTitulo == True:
            frame = Frame(janela, bg=self.interface.cinzaOliva)
            label = Label(frame, text=resposta, bg=corBG, fg=corFG, width=tamanho, borderwidth=2)
            label.pack(pady=(0, 0))
            frame.pack(pady=2) 
        else:
            frame = Frame(janela, bg=self.interface.cinzaOliva)
            titulo = Label(frame, text=texto, bg=corBGTitulo, fg=corFGTitulo)
            titulo.pack(pady=(0, 0))
            label = Label(frame, text=resposta, bg=corBG, fg=corFG, width=tamanho, borderwidth=2)
            label.pack(pady=(0, 0))
            frame.pack(pady=2) 
            
        return label
    
    def __editaLabel(self, resposta, labels = [], novaCorBG = None, novaCorFG = None):
        for label in labels:
            label.config(text=resposta)
            label.config(bg = novaCorBG, fg = novaCorFG) 
    
    def __criaButton(self, texto, janela, comando, tamanho, cursor):
        frame = Frame(janela, bg=self.interface.cinzaOliva)
        button = Button(frame, bg=self.interface.cinzaOlivaClaro, fg=self.interface.preto, text=texto, command=comando, width=tamanho, cursor=cursor, relief="flat")
        button.pack(pady=(0, 10), padx=10) 
        frame.pack(pady=6, side=TOP, anchor="center") 
        
    def __criaMenuComOpcoesDePortas(self, janela):
        self.opcoes = Menubutton(janela, text="Escolha Serial", cursor="hand1", relief="flat", bg=self.interface.cinzaOlivaClaro, fg=self.interface.preto)
        self.opcoes.pack(pady=(0, 10), padx=10)
        self.menu = Menu(self.opcoes, tearoff=0)
        self.opcoes.config(menu=self.menu)
        
        for porta in self.portas:
            self.menu.add_command(label=str(porta), command=lambda porta=porta: self.__selecionaSerial(porta))
            
    def atualizaMenuPortas(self):
        self.menu.delete(0, 'end')
        self.gravadorSerial.listaPortas()
        portasAdicionadas = set()
        for porta in self.gravadorSerial.portasUSB:
            if porta not in portasAdicionadas:
                self.menu.add_command(label=str(porta), command=lambda porta=porta: self.__selecionaSerial(porta))
                portasAdicionadas.add(porta)
        if not self.gravadorSerial.portasUSB:
            self.__editaLabel(f"Impossível de ler: serial desconectada✘", [self.report])
            self.__editaLabel("Desconectado", [self.conectadoOuNao], novaCorBG=self.interface.vermelho, novaCorFG=self.interface.branco)
            self.__criaTabelaComInformacoes(False)
            return 
                        
    def __selecionaSerial(self, porta):
        def conexao():    
            try:
                self.abrirPorta = porta
                if self.gravadorSerial.ser and self.gravadorSerial.ser.is_open:
                    self.gravadorSerial.ser.close()
                    time.sleep(1)    
                        
                self.__editaLabel("Conectando...", [self.conectadoOuNao], novaCorBG=self.interface.amarelo, novaCorFG=self.interface.preto)
                self.gravadorSerial.ser = serial.Serial(self.abrirPorta, baudrate=115200, bytesize=8, parity="N", stopbits=1, timeout=0.2) 
                if self.gravadorSerial.ser.is_open:
                    self.__editaLabel("Conectado", [self.conectadoOuNao], novaCorBG=self.interface.verde, novaCorFG=self.interface.preto)
                                
                else:
                    self.__editaLabel("Desconectado", [self.conectadoOuNao], novaCorBG=self.interface.vermelho, novaCorFG=self.interface.branco)

            except serial.SerialException:
                self.__editaLabel("Desconectado", [self.conectadoOuNao], novaCorBG=self.interface.vermelho, novaCorFG=self.interface.branco)
                self.__editaLabel("Erro ao abrir a porta serial", [self.report])
                self.__criaTabelaComInformacoes(False)
                self.gravadorSerial.ser = None 
        threading.Thread(target=conexao, daemon=True).start()
        
        
    def configMandaSinal(self):
        self.numeroLote = IntVar() 
        self.versaoPlacaNumero = IntVar()
        self.versaoPlacaNumero2 = IntVar()

        framePrincipal = Frame(self.interface.janelaMandaSinal, bg=self.interface.cinzaOliva)
        framePrincipal.pack(pady=10, padx=10)

        frameEsquerda = Frame(framePrincipal, bg=self.interface.cinzaOliva)
        frameEsquerda.pack(side="left", padx=10)

        self.escolheSerial = self.__criaMenuComOpcoesDePortas(frameEsquerda)
        self.ler = self.__criaButton("Identificar Placa", frameEsquerda, self.__leOqueTemDentroDaSerial, tamanho = 12, cursor = "hand1")
        self.conectadoOuNao = self.__criaLabel("Desconectado", frameEsquerda, 12, corBG=self.interface.vermelho, corFG=self.interface.branco, semTitulo=True)
        self.data = self.__criaCalendar("Data", frameEsquerda)

        frameDireita = Frame(framePrincipal, bg=self.interface.cinzaOliva)
        frameDireita.pack(side="left", padx=10)

        self.lote = self.__criaEntry("Lote", self.numeroLote, frameDireita)
        self.versaoPlaca = self.__criaEntry("Versão da Placa 1", self.versaoPlacaNumero, frameDireita)
        self.versaoPlaca2 = self.__criaEntry("Versão da Placa 2", self.versaoPlacaNumero2, frameDireita)
        self.enviar = self.__criaButton("Gravar Dados", frameDireita, self.__gravaBytesNaSerial, tamanho = 12, cursor = "hand1")
        
        self.report = self.__criaLabel("", self.interface.janelaMandaSinal, 60, self.interface.cinzaOlivaClaro, self.interface.preto, corFGTitulo=self.interface.branco , corBGTitulo=self.interface.cinzaOliva, texto="Relatório", semTitulo=False)
        