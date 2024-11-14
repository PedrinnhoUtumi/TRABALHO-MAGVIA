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
        self.msgEstruturada = None
        self.placaByte = None
        
    def atualizaBobina(self, bobina):
        self.bobina = bobina
        print(f"Bobina atualizada para: {bobina}")
        
    def enviarBytes(self):
        try:
            pedirStatus = 0x00
            definirStatus = 0x05
            
            # Obtendo os dados do formulário
            self.lote = self.numeroLote.get()
            self.numeroVersao = self.versaoPlacaNumero.get()
            data = self.dateEntry.get_date()

            if self.lote > 255 or self.numeroVersao > 255:
                messagebox.showerror("Erro", "Coloque números referentes à 2 Bytes/2 Bits (0 à 255)")
                return

            dia = data.day
            mes = data.month
            ano = data.year % 100

            # Determina o tipo de placa (bobina)
            if self.bobina == "Placa Potência":
                self.placaByte = 0x01
            elif self.bobina == "Placa Temperatura":
                self.placaByte = 0x02
            elif self.bobina == "Placa Bobina":
                self.placaByte = 0x03
            else:
                messagebox.showerror("Erro", "Bobina não encontrada")
                return

            fill = [0x00] 
            opcode = definirStatus

            # Envio do comando, depende do opcode
            if opcode == definirStatus:
                cabecalho = [0xAA, 0xBB, 0x00, self.placaByte, opcode]
                def checksum():
                    return sum(fill + [self.placaByte, 5, int(self.lote), dia, mes, ano, 170, 187, self.numeroVersao])

                # Envia os dados
                self.gravadorSerial.mensagensParaEnviar(info = cabecalho + (fill * 3) + [self.lote, dia, mes, ano, self.numeroVersao] + (fill * 49) + [checksum() & 0x00FF] + [checksum() >> 8])

            elif opcode == pedirStatus:
                cabecalho = [0xAA, 0xBB, 0x00, self.placaByte, opcode]
                def checksum():
                    return sum(fill + [self.placaByte, opcode, 170, 187])

                # Envia os dados
                self.gravadorSerial.mensagensParaEnviar(info = cabecalho + (fill * 57) + [checksum() & 0x00FF] + [checksum() >> 8])

            else:
                messagebox.showerror("Erro", "Algo está errado")
            
            # Atualiza a mensagem estruturada
            self.msgEstruturada = f"""
    Cabeçalho: {self.gravadorSerial.msg[:4]}  
    Lote: {self.gravadorSerial.msg[20]} 
    Dia: {self.gravadorSerial.msg[21]} 
    Mês: {self.gravadorSerial.msg[22]} 
    Ano: {self.gravadorSerial.msg[23]} 
    Versão: {int.from_bytes(self.gravadorSerial.msg[24:26], byteorder="little")} 
    FirmWare: {int.from_bytes(self.gravadorSerial.msg[26:28], byteorder="little")} 
    qmtdPulsos: {int.from_bytes(self.gravadorSerial.msg[16:20], byteorder="little")}
            """
            
            # Certifique-se de que a labelLoteData e a resposta estão sendo criadas e atualizadas corretamente
            if self.labelLoteData:
                self.labelLoteData.config(text=f"Lote: {self.lote} | Dia: {dia} | Mês: {mes} | Ano: {ano}")
                
                # Habilita o Text para edição antes de atualizar
                self.resposta.config(state=NORMAL)
                
                # Limpa e insere o novo texto
                self.resposta.delete(1.0, END)
                self.resposta.insert(END, f"{'bobina' if self.placaByte == 0x03 else 'Temperatura' if self.placaByte == 0x02 else 'Potência'}: {self.msgEstruturada}")
                
                # Volta o estado do Text para DISABLED
                self.resposta.config(state=DISABLED)
            else:
                frame = Frame(self.interface.janelaMandaSinal, bg=self.interface.cinza)
                self.labelLoteData = Label(frame, text=f"Lote: {self.lote} | Dia: {dia} | Mês: {mes} | Ano: {ano} | Versão: {self.numeroVersao}", bg=self.interface.cinzaClaro, fg=self.interface.branco)
                self.labelLoteData.pack(pady=(10, 0))
                frame.pack(pady=5)

                frame2 = Frame(self.interface.janelaMandaSinal, bg=self.interface.cinza)
                frame2.pack(pady=5, fill="both", expand=True)

                scrollbar = Scrollbar(frame2)
                scrollbar.pack(side="right", fill="y")

                self.resposta = Text(frame2, bg=self.interface.cinzaClaro, fg=self.interface.branco, wrap=WORD, yscrollcommand=scrollbar.set, height=10, width=40)
                self.resposta.pack(side="left", fill="both", expand=True)

                scrollbar.config(command=self.resposta.yview)

                # Habilita o Text para edição antes de atualizar
                self.resposta.config(state=NORMAL)

                # Insere o texto
                self.resposta.insert(END, f"{'Placa: Bobina' if self.placaByte == 0x03 else 'Placa: Temperatura' if self.placaByte == 0x02 else 'Placa: Potência'}: {self.msgEstruturada}")

                # Volta o estado para DISABLED
                self.resposta.config(state=DISABLED)

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
        
    def criarLabel(self, texto, resposta, janela):
        frame = Frame(janela, bg=self.interface.cinza)
        label = Label(frame, text=texto, bg=self.interface.cinza, fg=self.interface.branco)
        label.pack(pady=(10, 0))
        label2 = Label(frame, text=resposta,bg=self.interface.cinzaClaro, fg=self.interface.branco, width = 12, borderwidth = 2)
        label2.pack(pady=(0, 10)) 
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

        self.report = self.criarLabel("Report", "Ok", self.interface.janelaMandaSinal)
