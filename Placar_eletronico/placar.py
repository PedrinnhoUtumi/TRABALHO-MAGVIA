from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime, timedelta 
import serial.tools.list_ports
import threading
from PIL import Image, ImageTk
import serial
import pickle

class Interface():
    def __init__(self, root): #Aqui é onde eu conecto/crio tudo na minha função construtora
        self.ser = None
        self.ser2 = None
        self.root = root
        self.hr = 0         
        self.min = 0
        self.seg = 0
        self.milisseg = 0
        self.placarLocal = IntVar()
        self.placarLocal.set(0)
        self.placarLocalSubs = IntVar()
        self.placarLocalSubs.set(0)
        self.placarTempo = IntVar()
        self.placarTempo.set(1)
        self.localFools = IntVar()
        self.localFools.set(0)
        self.placarVisitanteSubs = IntVar()
        self.placarVisitanteSubs.set(0)
        self.awayFools = IntVar()
        self.awayFools.set(0)
        self.set1 = IntVar()
        self.set1.set(0)
        self.set2 = IntVar()
        self.set2.set(0)
        self.placarVisitante = IntVar()
        self.placarVisitante.set(0)
        self.tempo_correndo = False
        self.cronometro = StringVar()
        self.cronometro.set("0:00:00.0")
        self.texto_entry = StringVar()
        self.texto_entry2 = StringVar()
        self.ativa = StringVar()
        self.esporte = StringVar()
        self.contador = None
        self.tempo = ""
        self.tempo_extra = timedelta()
        self.check = BooleanVar()
        self.check.set(True)
        self.check2 = BooleanVar()
        self.check2.set(True)
        self.blue = "blue"
        self.aqua = "aqua"
        self.purple = "purple"
        self.black = "black"
        self.white = "white"
        self.root.bind("<Control-p>", lambda event: self.using_serial(True))
        self.root.bind("<Control-l>", lambda event: self.using_serial(False))
        self.root.bind("<Control-m>", self.show_serial)
        self.root.bind("<space>", self.start_timer)
        self.root.bind("0", self.zero)
        self.root.bind("<Control-u>", lambda event: self.pause(1))
        self.root.bind("<Control-i>", lambda event: self.pause(2))
        self.root.bind("<Control-o>", lambda event: self.pause(3))
        self.config_tela()
        self.frames()
        self.botao()
        self.load_state()
        self.load_state2()
        self.using_serial()
        self.using_serial2()
        self.open_enter()
        self.open_enter2()

    def config_tela(self): #Aqui é onde eu configuro as informações da app
        self.root.title("Placar Eletrônico") #Configura titulo
        self.root.configure(background = self.purple) #Configura cor de fundo
        self.root.geometry("1100x1100") #Configura tamanho inicial do app
        self.root.resizable(True, True) #Configura sua responsividade
        self.root.minsize(width = 700, height = 700) #Configura tamanho minimo do app
        
    def frames(self):  #Aqui é onde eu configuro frames e abas do app
        self.notebook = ttk.Notebook(self.root) #Cria abas
        self.notebook.pack(fill=BOTH, expand=True)
        
        self.frame1wid = Frame(self.notebook, bg = self.purple) #Configura aba 1
        self.notebook.add(self.frame1wid, text = "Placar")
        
        self.frame2wid = Frame(self.notebook, bg = self.purple) #Configura aba 2
        self.notebook.add(self.frame2wid, text = "Configurações")
        
        self.frame3wid = Frame(self.notebook, bg = self.purple) #Configura aba 3
        self.notebook.add(self.frame3wid, text = "Escalação")
        
        self.frame4wid = Frame(self.notebook, bg = self.purple) #Configura aba 4
        self.notebook.add(self.frame4wid, text = "24 Seg")

        self.frame5wid = Frame(self.notebook, bg = self.purple) #Configura aba 5
        self.notebook.add(self.frame5wid, text = "Jornal")
        
        #Configura os frames na aba 1
        imagem = Image.open("Placar_eletronico\magvia.png")
        imagem_redimensionada = imagem.resize((100, 100), Image.LANCZOS)
        self.foto = ImageTk.PhotoImage(imagem_redimensionada)
        
        self.frameLado = Label(self.frame1wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2, font = ("Courier New", 48, "bold"))
        self.frameLado.place(relx = 0.01, rely = 0.05, relwidth = 0.12, relheight = 0.8)
        
        self.frameLadoLabel = Label(self.frameLado, bg = self.aqua, font = ("Courier New", 12, "bold"), fg = self.black, text = "Funções")
        self.frameLadoLabel.place(relx = 0.14, rely = 0.05, relwidth = 0.7, relheight = 0.05)
        
        self.frame1 = Label(self.frame1wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2, textvariable = self.cronometro, font = ("Courier New", 48, "bold"))
        self.frame1.place(relx = 0.15, rely = 0.05, relwidth = 0.75, relheight = 0.2) #Cronometro
        
        self.frameFoto = Label(self.frame1, image = self.foto, bg = self.aqua)
        self.frameFoto.place(relx = 0.8, rely = 0.05, relwidth = 0.2, relheight = 0.5)
        
        self.entry_texto1 = Entry(self.frame1wid, textvariable=self.texto_entry, font=("Courier New", 12, "bold"), bg = self.purple, fg = self.white)
        self.entry_texto1.place(relx=0.15, rely=0.3, relwidth=0.2, relheight=0.05) #Nome do time da casa
        
        self.frameLocalLabel = Label(self.frame1wid, textvariable = self.placarLocal, bg = self.aqua, font = ("Courier New", 48, "bold"), highlightbackground = self.blue, highlightthickness = 2, cursor = "hand1")
        self.frameLocalLabel.place(relx = 0.15, rely = 0.35, relwidth = 0.2, relheight = 0.2) #Placar do time da casa
        self.frameLocalLabel.bind("<Button-1>", lambda event: self.plus(1)) #Função do placar
        
        self.frameLocalSubs = Label(self.frame1wid, textvariable = self.placarLocalSubs, bg = self.aqua, font = ("Courier New", 12, "bold"), highlightbackground = self.blue, highlightthickness = 2, cursor = "hand1")
        self.frameLocalSubs.place(relx = 0.363, rely = 0.35, relwidth = 0.05, relheight = 0.05) #Placar das substituições do time da casa
        self.frameLocalSubs.bind("<Button-1>", lambda event: self.plus(9)) #Função do placar das substituições
        
        self.localSubsText = Label(self.frame1wid, text="Subs", bg = self.purple, font=("Courier New", 12, "bold"), fg = self.white)
        self.localSubsText.place(relx=0.363, rely=0.4, relwidth=0.05, relheight=0.02) #Texto escrito "Subs"
        
        self.frameLocalFools = Label(self.frame1wid, textvariable = self.localFools, bg = self.aqua, font = ("Courier New", 12, "bold"), highlightbackground = self.blue, highlightthickness = 2, cursor = "hand1")
        self.frameLocalFools.place(relx = 0.15, rely = 0.57, relwidth = 0.2, relheight = 0.05) #Placar das faltas do time da casa
        self.frameLocalFools.bind("<Button-1>", lambda event: self.plus(4)) #Função do placar das faltas
        
        self.localFoolsText = Label(self.frame1wid, text="Faltas", bg = self.purple, font=("Courier New", 12, "bold"), fg = self.white)
        self.localFoolsText.place(relx=0.15, rely=0.63, relwidth=0.2, relheight=0.02) #Texto escrito "Faltas"
        
        self.time = Label(self.frame1wid, text="Tempo", bg = self.purple, font=("Courier New", 24, "bold"), fg = self.white)
        self.time.place(relx=0.425, rely=0.3, relwidth=0.2, relheight=0.05) #Texto escrito "Tempo"
        
        self.frameTime = Label(self.frame1wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2, font = ("Courier New", 48, "bold"), textvariable = self.placarTempo, cursor = "hand1")
        self.frameTime.place(relx = 0.425, rely = 0.35, relwidth = 0.2, relheight = 0.2) #Tempo/Periodo
        self.frameTime.bind("<Button-1>", lambda event: self.plus(3)) #Função do placar do tempo
        
        self.frameSet1 = Label(self.frame1wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2, font = ("Courier New", 12, "bold"), textvariable = self.set1, cursor = "hand1") 
        self.frameSet1.place(relx = 0.425, rely = 0.57, relwidth = 0.07, relheight = 0.05) #Placar dos sets do time da casa
        self.frameSet1.bind("<Button-1>", lambda event: self.plus(6)) #Função do placar dos sets do time da casa
        
        self.set1Label = Label(self.frame1wid, text="Set", bg = self.purple, font=("Courier New", 10, "bold"), fg = self.white)
        self.set1Label.place(relx=0.43, rely=0.62, relwidth=0.05, relheight=0.03) #Texto escrito "Set"
        
        self.frameSet2 = Label(self.frame1wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2, font = ("Courier New", 12, "bold"), textvariable = self.set2, cursor = "hand1") 
        self.frameSet2.place(relx = 0.555, rely = 0.57, relwidth = 0.07, relheight = 0.05) #Placar dos sets do time visitante
        self.frameSet2.bind("<Button-1>", lambda event: self.plus(7)) #Função do placar dos sets do time visitante
        
        self.set2Label = Label(self.frame1wid, text="Set", bg = self.purple, font=("Courier New", 10, "bold"), fg = self.white)
        self.set2Label.place(relx=0.57, rely=0.62, relwidth=0.05, relheight=0.03) #Texto escrito "Set"
        
        self.entry_texto = Entry(self.frame1wid, textvariable=self.texto_entry2, font=("Courier New", 12, "bold"), bg = self.purple, fg = self.white)
        self.entry_texto.place(relx=0.70, rely=0.3, relwidth=0.2, relheight=0.05) #Nome do time visitante
        
        self.frameVisitante = Label(self.frame1wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2, font = ("Courier New", 48, "bold"), textvariable = self.placarVisitante, cursor = "hand1")
        self.frameVisitante.place(relx = 0.70, rely = 0.35, relwidth = 0.2, relheight = 0.2) #Placar time visitante
        self.frameVisitante.bind("<Button-1>", lambda event: self.plus(2)) #Função do placar do time visitante
        
        self.frameAwaySubs = Label(self.frame1wid, textvariable = self.placarVisitanteSubs, bg = self.aqua, font = ("Courier New", 12, "bold"), highlightbackground = self.blue, highlightthickness = 2, cursor = "hand1")
        self.frameAwaySubs.place(relx = 0.637, rely = 0.35, relwidth = 0.05, relheight = 0.05) #Placar das substituições do time visitante
        self.frameAwaySubs.bind("<Button-1>", lambda event: self.plus(10)) #Função do placar das substituições
        
        self.awaySubsText = Label(self.frame1wid, text="Subs", bg = self.purple, font=("Courier New", 12, "bold"), fg = self.white)
        self.awaySubsText.place(relx=0.637, rely=0.4, relwidth=0.05, relheight=0.02) #Texto escrito "Subs"

        
        self.frameAwayFools = Label(self.frame1wid, textvariable = self.awayFools, bg = self.aqua, font = ("Courier New", 12, "bold"), highlightbackground = self.blue, highlightthickness = 2, cursor = "hand1")
        self.frameAwayFools.place(relx = 0.70, rely = 0.57, relwidth = 0.2, relheight = 0.05) #Placar das faltas do time visitante
        self.frameAwayFools.bind("<Button-1>", lambda event: self.plus(5)) #Função do placar das faltas do time visitante
        
        self.AwayFoolsText = Label(self.frame1wid, text="Faltas", bg = self.purple, font=("Courier New", 12, "bold"), fg = self.white)
        self.AwayFoolsText.place(relx=0.70, rely=0.63, relwidth=0.2, relheight=0.02) #Texto escrito "Faltas"
        
        self.frame2 = Label(self.frame1wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2)
        self.frame2.place(relx = 0.15, rely = 0.65, relwidth = 0.75, relheight = 0.2) #Botões variados
        
        #Configura os frames na aba 2
        self.frame1wid2Label = Label(self.frame2wid, bg = self.purple, font = ("Courier New", 12, "bold"), fg = self.white, text = "Esporte")
        self.frame1wid2Label.place(relx = 0.15, rely = 0.2, relwidth = 0.2, relheight = 0.2) 
        
        self.frame2wid2Label = Label(self.frame2wid, bg = self.purple, font = ("Courier New", 12, "bold"), fg = self.white, text = "Cronômetro")
        self.frame2wid2Label.place(relx = 0.15, rely = 0.5, relwidth = 0.2, relheight = 0.2) 
        
        self.frame3wid2Label = Label(self.frame2wid, bg = self.purple, font = ("Courier New", 12, "bold"), fg = self.white, text = "Mudar tema")
        self.frame3wid2Label.place(relx = 0.425, rely = 0.2, relwidth = 0.2, relheight = 0.2) 
        
        self.frame4wid2Label = Label(self.frame2wid, bg = self.purple, font = ("Courier New", 12, "bold"), fg = self.white, text = "Comunicação Serial")
        self.frame4wid2Label.place(relx = 0.4, rely = 0.5, relwidth = 0.25, relheight = 0.2) 
        
        self.frame5wid2Label = Label(self.frame2wid, bg = self.purple, font = ("Courier New", 12, "bold"), fg = self.white, text = "Atalhos")
        self.frame5wid2Label.place(relx = 0.7, rely = 0.2, relwidth = 0.2, relheight = 0.2) 
        
        self.frame6wid2Label = Label(self.frame2wid, bg = self.purple, font = ("Courier New", 12, "bold"), fg = self.white, text = "Atalhos")
        self.frame6wid2Label.place(relx = 0.7, rely = 0.5, relwidth = 0.2, relheight = 0.2) 
        
        self.frame1wid2 = Label(self.frame2wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2, font = ("Courier New", 48, "bold"))
        self.frame1wid2.place(relx = 0.15, rely = 0.05, relwidth = 0.2, relheight = 0.2) 
        
        self.frame2wid2 = Label(self.frame2wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2)
        self.frame2wid2.place(relx = 0.15, rely = 0.65, relwidth = 0.2, relheight = 0.2) 
        
        self.frame3wid2 = Label(self.frame2wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2, font = ("Courier New", 48, "bold"))
        self.frame3wid2.place(relx = 0.425, rely = 0.05, relwidth = 0.2, relheight = 0.2) 
        
        self.frame4wid2 = Label(self.frame2wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2)
        self.frame4wid2.place(relx = 0.425, rely = 0.65, relwidth = 0.2, relheight = 0.2) 
        
        self.frame5wid2 = Label(self.frame2wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2, font = ("Courier New", 48, "bold"))
        self.frame5wid2.place(relx = 0.7, rely = 0.05, relwidth = 0.2, relheight = 0.2) 
        
        self.frame6wid2 = Label(self.frame2wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2)
        self.frame6wid2.place(relx = 0.7, rely = 0.65, relwidth = 0.2, relheight = 0.2) 
        
        #Configura os frames da aba 3
        self.frame1wid3Label = Label(self.frame3wid, bg = self.purple, fg = self.white, text = "Time Local Esquerda")
        self.frame1wid3Label.place(relx = 0.05, rely = 0.01, relwidth = 0.15, relheight = 0.05)
        
        self.frame1wid3 = Label(self.frame3wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2)
        self.frame1wid3.place(relx = 0.05, rely = 0.05, relwidth = 0.4, relheight = 0.75)
        
        self.frame2wid3Label = Label(self.frame3wid, bg = self.purple, fg = self.white, text = "Time Visitante Direita")
        self.frame2wid3Label.place(relx = 0.5, rely = 0.01, relwidth = 0.15, relheight = 0.05)
        
        self.frame2wid3 = Label(self.frame3wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2)
        self.frame2wid3.place(relx = 0.5, rely = 0.05, relwidth = 0.4, relheight = 0.75)
        
        #Configura os frames da aba 4
        self.frame1wid4Label = Label(self.frame4wid, bg = self.purple, fg = self.white, text = "Serial dos 24 seg")
        self.frame1wid4Label.place(relx = 0.05, rely = 0.01, relwidth = 0.15, relheight = 0.05)
        
        self.frame1wid4 = Label(self.frame4wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2)
        self.frame1wid4.place(relx = 0.05, rely = 0.05, relwidth = 0.4, relheight = 0.75)
        
        self.frame2wid4Label = Label(self.frame4wid, bg = self.purple, fg = self.white, text = "Terminal")
        self.frame2wid4Label.place(relx = 0.5, rely = 0.01, relwidth = 0.15, relheight = 0.05)
        
        self.frame2wid4 = Label(self.frame4wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2)
        self.frame2wid4.place(relx = 0.5, rely = 0.05, relwidth = 0.4, relheight = 0.75)

        self.framecithec = Label(self.frame2wid4, bg = self.aqua, fg = self.black, text = "TERMINAL 24 SEG.", font = ("Courier New", 24, "bold"))
        self.framecithec.place(relx = 0, rely = 0.15, relwidth = 0.9, relheight = 0.05)

        self.framecithec2 = Label(self.frame2wid4, bg = self.aqua, fg = self.black, text = "CITHEC - V.12/16", font = ("Courier New", 24, "bold"))
        self.framecithec2.place(relx = 0, rely = 0.25, relwidth = 0.9, relheight = 0.05)

        self.frame1frame2wid4 = Label(self.frame2wid4, bg = self.aqua, fg = self.black, text = "A", font = ("Courier New", 24, "bold"))
        self.frame1frame2wid4.place (relx = 0, rely = 0.35, relwidth = 0.2, relheight = 0.05)
        
        self.frame2frame2wid4 = Label(self.frame2wid4, bg = self.aqua, fg = self.black, text = "Programa", font = ("Courier New", 12, "bold"))
        self.frame2frame2wid4.place (relx = 0.35, rely = 0.35, relwidth = 0.2, relheight = 0.05)
        
        self.frame3frame2wid4 = Label(self.frame2wid4, bg = self.aqua, fg = self.black, text = "Mostra", font = ("Courier New", 12, "bold"))
        self.frame3frame2wid4.place (relx = 0.7, rely = 0.35, relwidth = 0.2, relheight = 0.05)
        
        self.frame4frame2wid4 = Label(self.frame2wid4, bg = self.aqua, fg = self.black, text = "F1", font = ("Courier New", 24, "bold"))
        self.frame4frame2wid4.place (relx = 0, rely = 0.45, relwidth = 0.2, relheight = 0.05)
        
        self.frame5frame2wid4 = Label(self.frame2wid4, bg = self.aqua, fg = self.black, text = "F2", font = ("Courier New", 24, "bold"))
        self.frame5frame2wid4.place (relx = 0.35, rely = 0.45, relwidth = 0.2, relheight = 0.05)
        
        self.frame6frame2wid4 = Label(self.frame2wid4, bg = self.aqua, fg = self.black, text = "F3", font = ("Courier New", 24, "bold"))
        self.frame6frame2wid4.place (relx = 0.7, rely = 0.45, relwidth = 0.2, relheight = 0.05)
        
        self.frame7frame2wid4 = Label(self.frame2wid4, bg = self.aqua, fg = self.black, text = "F4", font = ("Courier New", 24, "bold"))
        self.frame7frame2wid4.place (relx = 0, rely = 0.55, relwidth = 0.2, relheight = 0.05)
        
        self.frame8frame2wid4 = Label(self.frame2wid4, bg = self.aqua, fg = self.black, text = "F5", font = ("Courier New", 24, "bold"))
        self.frame8frame2wid4.place (relx = 0.35, rely = 0.55, relwidth = 0.2, relheight = 0.05)
        
        self.frame9frame2wid4 = Label(self.frame2wid4, bg = self.aqua, fg = self.black, text = "60s", font = ("Courier New", 24, "bold"))
        self.frame9frame2wid4.place (relx = 0.7, rely = 0.55, relwidth = 0.2, relheight = 0.05)
        
        self.frame10frame2wid4 = Label(self.frame2wid4, bg = self.aqua, fg = self.black, text = "Camp", font = ("Courier New", 12, "bold"))
        self.frame10frame2wid4.place (relx = 0, rely = 0.65, relwidth = 0.2, relheight = 0.05)
        
        self.frame11frame2wid4 = Label(self.frame2wid4, bg = self.aqua, fg = self.black, text = "T. Prog.", font = ("Courier New", 12, "bold"))
        self.frame11frame2wid4.place (relx = 0.35, rely = 0.65, relwidth = 0.2, relheight = 0.05)
        
        self.frame12frame2wid4 = Label(self.frame2wid4, bg = self.aqua, fg = self.black, text = "24s", font = ("Courier New", 24, "bold"))
        self.frame12frame2wid4.place (relx = 0.7, rely = 0.65, relwidth = 0.2, relheight = 0.05)
        
        self.frame13frame2wid4 = Label(self.frame2wid4, bg = self.aqua, fg = self.black, text = "Para", font = ("Courier New", 12, "bold"))
        self.frame13frame2wid4.place (relx = 0, rely = 0.75, relwidth = 0.2, relheight = 0.05)
        
        self.frame14frame2wid4 = Label(self.frame2wid4, bg = self.aqua, fg = self.black, text = "Anda", font = ("Courier New", 12, "bold"))
        self.frame14frame2wid4.place (relx = 0.35, rely = 0.75, relwidth = 0.2, relheight = 0.05)
        
        self.frame15frame2wid4 = Label(self.frame2wid4, bg = self.aqua, fg = self.black, text = "14s", font = ("Courier New", 24, "bold"))
        self.frame15frame2wid4.place (relx = 0.7, rely = 0.75, relwidth = 0.2, relheight = 0.05)

        self.labelspacebar = Label(self.frame2wid4, bg = self.aqua, fg = self.black, text = "Barra de espaço ativa?", font = ("Courier New", 12, "bold"))
        self.labelspacebar.place(relx = 0, rely = 0.85, relwidth = 0.6, relheight = 0.05)
        
        self.framecronoframe1wid4 = Label(self.frame1wid4, bg = self.aqua, textvariable = self.cronometro, font = ("Courier New", 36, "bold"))
        self.framecronoframe1wid4.place(relx = 0.13, rely = 0.45, relwidth = 0.75, relheight = 0.2) #Cronometro
        
        #Configura frames da aba 5
        self.frame1wid5Label = Label(self.frame5wid, bg = self.purple, fg = self.white, text = "Mensagem", font = ("Courier New", 12, "bold"))
        self.frame1wid5Label.place(relx = 0.05, rely = 0.01, relwidth = 0.5, relheight = 0.05)
        
        self.frame1wid5 = Text(self.frame5wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2, wrap = "none", autoseparators = True)
        self.frame1wid5.place(relx = 0.05, rely = 0.05, relwidth = 0.5, relheight = 0.65)
        
        self.frame2wid5Label = Label(self.frame5wid, bg = self.purple, fg = self.white, text = "Escalação Local", font = ("Courier New", 12, "bold"))
        self.frame2wid5Label.place(relx = 0.05, rely = 0.7, relwidth = 0.5, relheight = 0.05)
        
        self.frame2wid5 = Label(self.frame5wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2)
        self.frame2wid5.place(relx = 0.05, rely = 0.75, relwidth = 0.5, relheight = 0.05)
        
        self.frame1frame2wid5 = Text(self.frame2wid5, bg = self.white, wrap = "none")
        self.frame1frame2wid5.place(relx = 0.05, rely = 0.05, relwidth = 0.8, relheight = 0.35)
        
        self.frame2frame2wid5 = Text(self.frame2wid5, bg = self.white, wrap = "none")
        self.frame2frame2wid5.place(relx = 0.05, rely = 0.55, relwidth = 0.8, relheight = 0.35)
        
        self.frame3wid5Label = Label(self.frame5wid, bg = self.purple, fg = self.white, text = "Escalação Visitante", font = ("Courier New", 12, "bold"))
        self.frame3wid5Label.place(relx = 0.05, rely = 0.8, relwidth = 0.5, relheight = 0.05)
        
        self.frame3wid5 = Label(self.frame5wid, bg = self.aqua, highlightbackground = self.blue, highlightthickness = 2)
        self.frame3wid5.place(relx = 0.05, rely = 0.85, relwidth = 0.5, relheight = 0.05)
        
        self.frame1frame3wid5 = Text(self.frame3wid5, bg = self.white, wrap = "none")
        self.frame1frame3wid5.place(relx = 0.05, rely = 0.05, relwidth = 0.8, relheight = 0.35)
        
        self.frame2frame3wid5 = Text(self.frame3wid5, bg = self.white, wrap = "none")
        self.frame2frame3wid5.place(relx = 0.05, rely = 0.55, relwidth = 0.8, relheight = 0.35)
        
        
    def botao(self):
        #Botôes de controle
        self.bt_start = Button(self.frameLado, text = "Iniciar", cursor = "clock", command = self.start_timer)
        self.bt_start.place(relx = 0.15, rely = 0.15, relwidth = 0.7, relheight = 0.03) #Iniciar cronômetro
        
        self.bt_zero = Button(self.frameLado, text = "Zerar", command = self.zero, cursor = "hand1")
        self.bt_zero.place(relx = 0.15, rely = 0.2, relwidth = 0.7, relheight = 0.03) #Zerar toda a página
        
        self.bt_pause = Button(self.frameLado, text = "Pausar", command = lambda: self.pause(1), cursor = "hand1")
        self.bt_pause.place(relx = 0.15, rely = 0.25, relwidth = 0.7, relheight = 0.03) #Pausar cronômetro
        
        self.bt_reniciar = Button(self.frameLado, text = "Reiniciar", command = lambda: self.pause(2), cursor = "hand1")
        self.bt_reniciar.place(relx = 0.15, rely = 0.3, relwidth = 0.7, relheight = 0.03) #Reinciar cronômetro
        
        self.bt_continue = Button(self.frameLado, text = "Continuar", cursor = "hand1", command = lambda: self.pause(3))
        self.bt_continue.place(relx = 0.15, rely = 0.35, relwidth = 0.7, relheight = 0.03) #Continuar cronômetro após pausa
        
        #Botôes do frame2 da aba 1
        self.bt_minus = Button(self.frame2, text = "-1", command = lambda: self.minus(1), cursor = "hand1")
        self.bt_minus.place(relx = 0.05, rely = 0.05, relwidth = 0.15, relheight = 0.15) #-1 ponto do time de casa

        self.plus_fool1 = Button(self.frame2, text = "+1 Falta time 1", cursor = "hand1", command = lambda: self.plus(4))
        self.plus_fool1.place(relx = 0.235, rely = 0.05, relwidth = 0.15, relheight = 0.15) #+1 falta do time de casa

        self.minus_fool1 = Button(self.frame2, text = "-1 Falta time 1", cursor = "hand1", command = lambda: self.minus(6))
        self.minus_fool1.place(relx = 0.235, rely = 0.25, relwidth = 0.15, relheight = 0.15) #-1 falta do time de casa

        self.plus_subs1 = Button(self.frame2, text = "+1 Sub time 1", cursor = "hand1", command = lambda: self.plus(9))
        self.plus_subs1.place(relx = 0.05, rely = 0.85, relwidth = 0.15, relheight = 0.15) #+1 substituição do time de casa

        self.minus_subs1 = Button(self.frame2, text = "-1 Sub time 1", cursor = "hand1", command = lambda: self.minus(8))
        self.minus_subs1.place(relx = 0.235, rely = 0.85, relwidth = 0.15, relheight = 0.15) #-1 substituição do time de casa

        self.plus_time = Button(self.frame2, text = "+1 Periodo", cursor = "hand1", command = lambda: self.plus(8))
        self.plus_time.place(relx = 0.42, rely = 0.25, relwidth = 0.15, relheight = 0.15) #+1 periodo
        
        self.minus_time = Button(self.frame2, text = "-1 Periodo", cursor = "hand1", command = lambda: self.minus(5))
        self.minus_time.place(relx = 0.42, rely = 0.45, relwidth = 0.15, relheight = 0.15) #-1 periodo

        self.plus_fool2 = Button(self.frame2, text = "+1 Falta time 2", cursor = "hand1", command = lambda: self.plus(5))
        self.plus_fool2.place(relx = 0.61, rely = 0.05, relwidth = 0.15, relheight = 0.15) #+1 falta do time visitante

        self.minus_fool2 = Button(self.frame2, text = "-1 Falta time 2", cursor = "hand1", command = lambda: self.minus(7))
        self.minus_fool2.place(relx = 0.61, rely = 0.25, relwidth = 0.15, relheight = 0.15) #+1 falta do time visitante
        
        self.plus_subs2 = Button(self.frame2, text = "+1 Sub time 2", cursor = "hand1", command = lambda: self.plus(10))
        self.plus_subs2.place(relx = 0.61, rely = 0.85, relwidth = 0.15, relheight = 0.15) #+1 substituição do time visitante
        
        self.minus_subs2 = Button(self.frame2, text = "-1 Sub time 2", cursor = "hand1", command = lambda: self.minus(9))
        self.minus_subs2.place(relx = 0.8, rely = 0.85, relwidth = 0.15, relheight = 0.15) #-1 substituição do time visitante

        self.plus_set1 = Button(self.frame2, text = "+1 Set time 1", cursor = "hand1", command = lambda: self.plus(6))
        self.plus_set1.place(relx = 0.235, rely = 0.45, relwidth = 0.15, relheight = 0.15) #+1 set do time da casa
        
        self.plus_set2 = Button(self.frame2, text = "+1 Set time 2", cursor = "hand1", command = lambda: self.plus(7))
        self.plus_set2.place(relx = 0.61, rely = 0.45, relwidth = 0.15, relheight = 0.15) #+1 set do time visitante
        
        self.minus_set1 = Button(self.frame2, text = "-1 Set time 1", cursor = "hand1", command = lambda: self.minus(3))
        self.minus_set1.place(relx = 0.235, rely = 0.65, relwidth = 0.15, relheight = 0.15) #-1 set do time da casa
        
        self.minus_set2 = Button(self.frame2, text = "-1 Set time 2", cursor = "hand1", command = lambda: self.minus(4))
        self.minus_set2.place(relx = 0.61, rely = 0.65, relwidth = 0.15, relheight = 0.15) #-1 set do time visitante
        
        self.plus1 = Button(self.frame2, text = "+1", command = lambda: self.plus(1), cursor = "hand1")
        self.plus1.place(relx = 0.05, rely = 0.25, relwidth = 0.15, relheight = 0.15) #+1 ponto do time de casa
        
        self.bt_plus2 = Button(self.frame2, text = "+2", command = lambda: self.plus2(1), cursor = "hand1")
        self.bt_plus2.place(relx = 0.05, rely = 0.45, relwidth = 0.15, relheight = 0.15) #+2 pontos do time de casa 
        
        self.bt_plus3 = Button(self.frame2, text = "+3", command = lambda: self.plus3(1), cursor = "hand1")
        self.bt_plus3.place(relx = 0.05, rely = 0.65, relwidth = 0.15, relheight = 0.15) #+3 pontos do time de casa
        
        self.bt_minus_visitante = Button(self.frame2, text = "-1", command = lambda: self.minus(2), cursor = "hand1")
        self.bt_minus_visitante.place(relx = 0.8, rely = 0.05, relwidth = 0.15, relheight = 0.15) #-1 ponto do time visitante
        
        self.plus_visitante = Button(self.frame2, text = "+1", command = lambda: self.plus(2), cursor = "hand1")
        self.plus_visitante.place(relx = 0.8, rely = 0.25, relwidth = 0.15, relheight = 0.15) #+1 ponto do time visitante
         
        self.bt_plus2_visitante = Button(self.frame2, text = "+2", command = lambda: self.plus2(2), cursor = "hand1")
        self.bt_plus2_visitante.place(relx = 0.8, rely = 0.45, relwidth = 0.15, relheight = 0.15) #+2 pontos do time visitante
        
        self.bt_plus3_visitante = Button(self.frame2, text = "+3", command = lambda: self.plus3(2), cursor = "hand1")
        self.bt_plus3_visitante.place(relx = 0.8, rely = 0.65, relwidth = 0.15, relheight = 0.15) #+3 pontos do time visitante
        
        #Botôes da aba 2
        self.bt_theme = Button(self.frame3wid2, text = "Tema azul", command = lambda: self.change_theme(1), cursor = "hand1")
        self.bt_theme.place(relx = 0.15, rely = 0.05, relwidth = 0.7, relheight = 0.15) #Mudar tema para verde
        
        self.bt_theme2 = Button(self.frame3wid2, text = "Tema roxo", command = lambda: self.change_theme(2), cursor = "hand1")
        self.bt_theme2.place(relx = 0.15, rely = 0.25, relwidth = 0.7, relheight = 0.15) #Mudar tema para roxo

        self.bt_theme3 = Button(self.frame3wid2, text = "Tema cinza", command = lambda: self.change_theme(3), cursor = "hand1")
        self.bt_theme3.place(relx = 0.15, rely = 0.45, relwidth = 0.7, relheight = 0.15) #Mudar tema para cinza

        self.bt_serial_open = Button(self.frame4wid2, text = "Abre serial", command = lambda: self.using_serial(True), cursor = "hand1")
        self.bt_serial_open.place(relx = 0.15, rely = 0.05, relwidth = 0.7, relheight = 0.15) #Abre a porta serial
        
        self.bt_serial_close = Button(self.frame4wid2, text = "Fecha serial", command = lambda: self.using_serial(False), cursor = "hand1")
        self.bt_serial_close.place(relx = 0.15, rely = 0.25, relwidth = 0.7, relheight = 0.15) #Fecha a porta serial 

        self.bt_choose_serial = Menubutton(self.frame4wid2, text = "Escolhe serial", cursor = "hand1", relief = "ridge")
        self.bt_choose_serial.place(relx = 0.15, rely = 0.45, relwidth = 0.7, relheight = 0.15) #Escolhe a porta serial
        self.menu = Menu(self.bt_choose_serial, tearoff = 0)
        self.bt_choose_serial.config(menu = self.menu)

        self.timeout = Spinbox(self.frame4wid2, from_ = 0, to = 1000, cursor = "hand1", background = self.aqua)
        self.timeout.place(relx = 0.15, rely = 0.65, relwidth = 0.7, relheight = 0.15)
        
        self.ativar2 = Checkbutton(self.frame4wid2, bg = self.aqua, text = "Abrir ao entrar", variable = self.check, command = self.save_state)
        self.ativar2.place(relx = 0.15, rely = 0.85, relwidth = 0.7, relheight = 0.15)
        
        self.bt_add1min = Button(self.frame2wid2, text = "+1 minuto", cursor = "hand1", command = lambda: self.handle_minute("add"))
        self.bt_add1min.place(relx = 0.15, rely = 0.05, relwidth = 0.7, relheight = 0.15) #Adiciona 1 minuto ao cronômetro

        self.bt_minus1min = Button(self.frame2wid2, text = "-1 minuto", cursor = "hand1", command = lambda: self.handle_minute("remove"))
        self.bt_minus1min.place(relx = 0.15, rely = 0.25, relwidth = 0.7, relheight = 0.15) #Remove 1 minuto ao cronômetro
        
        self.entry_time = Entry (self.frame2wid2, cursor = "hand1")
        self.entry_time.place(relx = 0.15, rely = 0.45, relwidth = 0.7, relheight = 0.15)

        self.front = Button(self.frame2wid2, text = "Anda para frente ⏩", cursor = "hand1")
        self.front.place(relx = 0.15, rely = 0.65, relwidth = 0.7, relheight = 0.15)

        self.back = Button(self.frame2wid2, text = "⏪ Anda pra trás", cursor = "hand1")
        self.back.place(relx = 0.15, rely = 0.85, relwidth = 0.7, relheight = 0.15)

        self.choose_game = Radiobutton(self.frame1wid2, cursor = "hand1", text = "Futebol", bg = self.aqua, variable = self.esporte, value = "Futebol")
        self.choose_game.place(relx = 0.15, rely = 0.05, relwidth = 0.7, relheight = 0.15)
        
        self.choose_game2 = Radiobutton(self.frame1wid2, cursor = "hand1", text = "Voleibol", bg = self.aqua, variable = self.esporte, value = "Voleibol")
        self.choose_game2.place(relx = 0.15, rely = 0.25, relwidth = 0.7, relheight = 0.15)
        
        self.choose_game3 = Radiobutton(self.frame1wid2, cursor = "hand1", text = "Basquete", bg = self.aqua, variable = self.esporte, value = "Basquete")
        self.choose_game3.place(relx = 0.15, rely = 0.45, relwidth = 0.7, relheight = 0.15)
        
        self.choose_game4 = Radiobutton(self.frame1wid2, cursor = "hand1", text = "Tênis de Mesa", bg = self.aqua, variable = self.esporte, value = "Tênis de Mesa")
        self.choose_game4.place(relx = 0.15, rely = 0.65, relwidth = 0.7, relheight = 0.15)
        
        self.choose_game5 = Radiobutton(self.frame1wid2, cursor = "hand1", text = "Outros", bg = self.aqua, variable = self.esporte, value = "Outros")
        self.choose_game5.place(relx = 0.15, rely = 0.85, relwidth = 0.7, relheight = 0.15)
        
        self.controles = Label(self.frame5wid2, bg = self.aqua, text = "Espaço = Inicia")
        self.controles.place(relx = 0.15, rely = 0.05, relwidth = 0.7, relheight = 0.15)
        
        self.controles = Label(self.frame5wid2, bg = self.aqua, text = "0 = Zerar")
        self.controles.place(relx = 0.15, rely = 0.25, relwidth = 0.7, relheight = 0.15)
        
        self.controles = Label(self.frame5wid2, bg = self.aqua, text = "Ctrl + u = Pausar")
        self.controles.place(relx = 0.15, rely = 0.45, relwidth = 0.7, relheight = 0.15)
        
        self.controles = Label(self.frame5wid2, bg = self.aqua, text = "Ctrl + i = Reiniciar")
        self.controles.place(relx = 0.15, rely = 0.65, relwidth = 0.7, relheight = 0.15)

        self.controles = Label(self.frame5wid2, bg = self.aqua, text = "Ctrl + o = Continuar")
        self.controles.place(relx = 0.15, rely = 0.85, relwidth = 0.7, relheight = 0.15)
        
        self.controls = Label(self.frame6wid2, bg = self.aqua, text = "Ctrl + p = Abre serial")
        self.controls.place(relx = 0.15, rely = 0.05, relwidth = 0.7, relheight = 0.15)
        
        self.controls = Label(self.frame6wid2, bg = self.aqua, text = "Ctrl + l = Fecha serial")
        self.controls.place(relx = 0.15, rely = 0.25, relwidth = 0.7, relheight = 0.15)
        
        self.controls = Label(self.frame6wid2, bg = self.aqua, text = "Ctrl + m = Mostra serial")
        self.controls.place(relx = 0.15, rely = 0.45, relwidth = 0.7, relheight = 0.15)
        
        self.controls = Label(self.frame6wid2, bg = self.aqua, text = "#")
        self.controls.place(relx = 0.15, rely = 0.65, relwidth = 0.7, relheight = 0.15)

        self.controls = Label(self.frame6wid2, bg = self.aqua, text = "#")
        self.controls.place(relx = 0.15, rely = 0.85, relwidth = 0.7, relheight = 0.15)
        
    #Botões da aba 4
        self.ativar = Checkbutton(self.frame2wid4, bg = self.aqua, text = "Ativar simulador 24 seg")
        self.ativar.place(relx = 0, rely = 0.05, relwidth = 0.5, relheight = 0.05)

        self.esppacoativa = Radiobutton(self.frame2wid4, bg = self.aqua, text = "14s", variable = self.ativa, value = "14s")
        self.esppacoativa.place(relx = 0, rely = 0.9, relwidth = 0.15, relheight = 0.05)
    
        self.esppacoativa2 = Radiobutton(self.frame2wid4, bg = self.aqua, text = "24s", variable = self.ativa, value = "24s")
        self.esppacoativa2.place(relx = 0.2, rely = 0.9, relwidth = 0.15, relheight = 0.05)
    
        self.esppacoativa3 = Radiobutton(self.frame2wid4, bg = self.aqua, text = "Prog", variable = self.ativa, value = "Prog")
        self.esppacoativa3.place(relx = 0.4, rely = 0.9, relwidth = 0.15, relheight = 0.05)
    
        self.esppacoativa4 = Radiobutton(self.frame2wid4, bg = self.aqua, text = "Para/Anda", variable = self.ativa, value = "Para/Anda")
        self.esppacoativa4.place(relx = 0.6, rely = 0.9, relwidth = 0.2, relheight = 0.05)
        
        self.bt_serial_open2 = Button(self.frame1wid4, text = "Abre serial", command = lambda: self.using_serial2(True), cursor = "hand1")
        self.bt_serial_open2.place(relx = 0.05, rely = 0.05, relwidth = 0.2, relheight = 0.05) #Abre a porta serial
        
        self.bt_serial_close2 = Button(self.frame1wid4, text = "Fecha serial", command = lambda: self.using_serial2(False), cursor = "hand1")
        self.bt_serial_close2.place(relx = 0.4, rely = 0.05, relwidth = 0.2, relheight = 0.05) #Fecha a porta serial 

        self.new_data2 = Button(self.frame1wid4, text = "Mostrar serial", command = self.show_serial2, cursor = "hand1")
        self.new_data2.place(relx = 0.75, rely = 0.05, relwidth = 0.2, relheight = 0.05)
        
        self.bt_choose_serial2 = Menubutton(self.frame1wid4, text = "Escolhe serial", cursor = "hand1", relief = "ridge")
        self.bt_choose_serial2.place(relx = 0.225, rely = 0.15, relwidth = 0.2, relheight = 0.05) #Escolhe a porta serial
        self.menu2 = Menu(self.bt_choose_serial2, tearoff = 0)
        self.bt_choose_serial2.config(menu = self.menu2)

        self.timeout2 = Spinbox(self.frame1wid4, from_ = 0, to = 1000, cursor = "hand1", background = self.aqua)
        self.timeout2.place(relx = 0.575, rely = 0.15, relwidth = 0.2, relheight = 0.05)

        self.ativar2 = Checkbutton(self.frame1wid4, bg = self.aqua, text = "Abrir ao entrar", variable = self.check2, command = self.save_state2)
        self.ativar2.place(relx = 0, rely = 0.25, relwidth = 0.5, relheight = 0.02)
        
        #Botões da aba 5
        self.enviar = Button(self.frame2wid5, text = "Enviar", cursor = "hand1")
        self.enviar.place(relx = 0.9, rely = 0.05, relwidth = 0.1, relheight = 0.35)
        
        self.limpar = Button(self.frame2wid5, text = "Limpar", cursor = "hand1")
        self.limpar.place(relx = 0.9, rely = 0.55, relwidth = 0.1, relheight = 0.35)
        
        self.enviar2 = Button(self.frame3wid5, text = "Enviar", cursor = "hand1")
        self.enviar2.place(relx = 0.9, rely = 0.05, relwidth = 0.1, relheight = 0.35)
        
        self.limpar2 = Button(self.frame3wid5, text = "Limpar", cursor = "hand1")
        self.limpar2.place(relx = 0.9, rely = 0.55, relwidth = 0.1, relheight = 0.35)
        
    def plus(self, team): #Definindo a função que vai adicionar os pontos, sets etc
        if self.esporte_validacao():
            if team == 1: 
                self.placarLocal.set(self.placarLocal.get() + 1)
            elif team == 2:
                self.placarVisitante.set(self.placarVisitante.get() + 1)
            elif team == 3:
                self.placarTempo.set(self.placarTempo.get() + 1)
            elif team == 4:
                self.localFools.set(self.localFools.get() + 1)
            elif team == 5:
                self.awayFools.set(self.awayFools.get() + 1)
            elif team == 6:
                self.set1.set(self.set1.get() + 1)
            elif team == 7:
                self.set2.set(self.set2.get() + 1)
            elif team == 8:
                self.placarTempo.set(self.placarTempo.get() + 1)
            elif team == 9:
                self.placarLocalSubs.set(self.placarLocalSubs.get() + 1)
            elif team == 10:
                self.placarVisitanteSubs.set(self.placarVisitanteSubs.get() + 1)
        self.serial_Port()
        
    def plus2(self, team): #Defiinindo a função que vai adicionar 2 pontos
        if self.esporte_validacao():
            if team == 1: 
                self.placarLocal.set(self.placarLocal.get() + 2)
            elif team == 2:
                self.placarVisitante.set(self.placarVisitante.get() + 2)            
        self.serial_Port()
        
    def plus3(self, team): #Defiinindo a função que vai adicionar 3 pontos
        if self.esporte_validacao():
            if team == 1: 
                self.placarLocal.set(self.placarLocal.get() + 3)
            elif team == 2:
                self.placarVisitante.set(self.placarVisitante.get() + 3)
        self.serial_Port()
    
    def minus(self, team): #Definindo a função que vai tirar pontos, sets etc
        if team == 1: 
            if self.validate(1):
                self.placarLocal.set(self.placarLocal.get() - 1)
        elif team == 2:
            if self.validate(2):
                self.placarVisitante.set(self.placarVisitante.get() - 1)
        elif team == 3:
            if self.validate(3):
                self.set1.set(self.set1.get() - 1)
        elif team == 4:
            if self.validate(4):
                self.set2.set(self.set2.get() - 1)
        elif team == 5:
            if self.validate(5):
                self.placarTempo.set(self.placarTempo.get() - 1)
        elif team == 6:
            if self.validate(6):
                self.localFools.set(self.localFools.get() - 1)
        elif team == 7:
            if self.validate(7):
                self.awayFools.set(self.awayFools.get() - 1)
        elif team == 8:
            if self.validate(8):
                self.placarLocalSubs.set(self.placarLocalSubs.get() - 1)
        elif team == 9:
            if self.validate(9):
                self.placarVisitanteSubs.set(self.placarVisitanteSubs.get() - 1)
        self.serial_Port()
        
    def update(self): #Para que nosso cronômetro comece a rodar
        if self.contador:
            tempo = datetime.now() - self.contador
            total_milliseg = int(tempo.total_seconds() * 10)
            hr, resto = divmod(total_milliseg, 36000)
            min, resto = divmod(resto, 600)
            seg, milisseg = divmod(resto, 10)
            self.cronometro.set(f"{int(hr):01}:{int(min):02}:{int(seg):02}.{int(milisseg):01}")
            self.root.after(100, self.serial_Port)
            self.root.after(100, self.update)
            
    def handle_minute(self, opcao):
        tempo = self.cronometro.get()
        hr, min, seg_milisseg = tempo.split(':')
        seg, milisseg = seg_milisseg.split('.')
        self.hr = int(hr)         
        self.min = int(min)
        self.seg = int(seg)
        self.milisseg = int(milisseg)
        if opcao == "add":
            self.min += 1            
            if self.min > 59:
                self.min = 0
                self.hr += 1  
        
        elif opcao == "remove":
            self.min -= 1   
            if self.min < 0: 
                self.min = 59
                self.hr -= 1 
            if self.hr < 0:  
                self.hr = 0
                self.min = 0   
        self.cronometro.set(f"{(self.hr):01}:{(self.min):02}:{(self.seg):02}.{(self.milisseg):01}")
        self.update()
        
    def start_timer(self, event=None):
        if not self.contador:
            self.contador = datetime.now()
            self.update()
            self.serial_Port()
            print("Iniciando...")
            if self.min != 0:
                self.contador = datetime.now() - timedelta(minutes = self.min)
                self.update()   
                    
    def zero(self, event = None): #Definindo tudo para seu número/caractere inicial
        self.placarLocal.set(0)
        self.placarTempo.set(1)
        self.placarVisitante.set(0)
        self.set1.set(0)
        self.set2.set(0)
        self.contador_pause = None
        self.cronometro.set("0:00:00.0")
        self.texto_entry.set("")
        self.texto_entry2.set("")
        self.localFools.set(0)
        self.awayFools.set(0)
        self.placarVisitanteSubs.set(0)
        self.hr = 0         
        self.min = 0
        self.seg = 0
        self.milisseg = 0
        self.placarLocalSubs.set(0)
        self.contador = None
        self.serial_Port()

    def pause(self, opcao, event = None):
        if opcao == 1: #Aqui vai pausar
            self.contador_pause = datetime.now() - self.contador
            self.contador = None
        elif opcao == 2: #Aqui vai reiniciar o cronômetro
            self.cronometro.set("0:00:00.0")
            self.contador = None
            self.contador_pause = None
            self.min = 0
        elif opcao == 3: #Continua o cronômetro se estiver pausado
            if self.contador_pause:
                self.contador = datetime.now() - self.contador_pause
                self.update()
                self.contador_pause = None
        self.serial_Port()
            
    def validate(self, opcao): #Serve para que os números não passem de seu mínimo permitido
        if opcao == 1:
            if self.placarLocal.get() <= 0:
                self.placarLocal.set(0)
                return False
        elif opcao == 2:
            if self.placarVisitante.get() <= 0:
                self.placarVisitante.set(0)
                return False
        elif opcao == 3:
            if self.set1.get() <= 0:
                self.set1.set(0)
                return False 
        elif opcao == 4:
            if self.set2.get() <= 0:
                self.set2.set(0)
                return False 
        elif opcao == 5:
            if self.placarTempo.get() <= 1:
                self.placarTempo.set(1)
                return False 
        elif opcao == 6:
            if self.localFools.get() <= 0:
                self.localFools.set(0)
                return False 
        elif opcao == 7:
            if self.awayFools.get() <= 0:
                self.awayFools.set(0)
                return False 
        elif opcao == 8:
            if self.placarLocalSubs.get() <= 0:
                self.placarLocalSubs.set(0)
                return False 
        elif opcao == 9:
            if self.placarVisitanteSubs.get() <= 0:
                self.placarVisitanteSubs.set(0)
                return False 
        return True
    
    def save_state(self):
        with open("save_state.pkl", "wb") as f:
            pickle.dump(self.check.get(), f)
            
    def load_state(self):
        try:
            with open("save_state.pkl", "rb") as f:
                estado = pickle.load(f)
                self.check.set(estado)
        except FileNotFoundError:
            self.check.set(False)  # Define o estado padrão como desativado caso o arquivo não exista
    
    def save_state2(self):
        with open("save_state2.pkl", "wb") as f:
            pickle.dump(self.check2.get(), f)
            
    def load_state2(self):
        try:
            with open("save_state2.pkl", "rb") as f:
                estado = pickle.load(f)
                self.check2.set(estado)
        except FileNotFoundError:
            self.check2.set(False)  # Define o estado padrão como desativado caso o arquivo não exista
                
    def change_theme(self, opcao): #Muda os temas
        if opcao == 1: #Tema azul
            cor1 = "#025959"
            cor2 = "#04BFBF"
            cor3 = "#04ADBF"
            self.frame1wid.config(bg = cor1, highlightbackground = cor1)
            self.frame1.config(bg = cor2, highlightbackground = cor1)
            self.frame2.config(bg = cor2, highlightbackground = cor1)
            self.frameTime.config(bg = cor2, highlightbackground = cor1)
            self.frameVisitante.config(bg = cor2, highlightbackground = cor1)
            self.frameLocalLabel.config(bg = cor2, highlightbackground = cor1)
            self.frameLocalFools.config(bg = cor2, highlightbackground = cor1)
            self.frameSet1.config(bg = cor2, highlightbackground = cor1)
            self.frameSet2.config(bg = cor2, highlightbackground = cor1)
            self.frameAwayFools.config(bg = cor2, highlightbackground = cor1)
            self.frameLocalSubs.config(bg = cor2, highlightbackground = cor1)
            self.frameAwaySubs.config(bg = cor2, highlightbackground = cor1)
            self.frameLado.config(bg = cor2, highlightbackground = cor1)
            self.frameFoto.config(bg = cor2)
            self.entry_time.config(bg = cor1, fg = cor3)
            self.entry_texto.config(bg = cor1, fg = cor3)
            self.entry_texto1.config(bg = cor1, fg = cor3)
            self.time.config(bg = cor1, fg = cor3)
            self.set1Label.config(bg = cor1, fg = cor3)
            self.set2Label.config(bg = cor1, fg = cor3)
            self.AwayFoolsText.config(bg = cor1, fg = cor3)
            self.localFoolsText.config(bg = cor1, fg = cor3)
            self.localSubsText.config(bg = cor1, fg = cor3)
            self.awaySubsText.config(bg = cor1, fg = cor3)
            self.frameLadoLabel.config(bg = cor2, fg = cor3)
        elif opcao == 2: #Tema roxo
            self.frame1wid.config(bg = self.purple, highlightbackground = self.blue)
            self.frame1.config(bg = self.aqua, highlightbackground = self.blue)
            self.frame2.config(bg = self.aqua, highlightbackground = self.blue)
            self.frameTime.config(bg = self.aqua, highlightbackground = self.blue)
            self.frameVisitante.config(bg = self.aqua, highlightbackground = self.blue)
            self.frameLocalLabel.config(bg = self.aqua, highlightbackground = self.blue)
            self.frameLocalFools.config(bg = self.aqua, highlightbackground = self.blue)
            self.frameSet1.config(bg = self.aqua, highlightbackground = self.blue)
            self.frameSet2.config(bg = self.aqua, highlightbackground = self.blue)
            self.frameAwayFools.config(bg = self.aqua, highlightbackground = self.blue)
            self.frameLocalSubs.config(bg = self.aqua, highlightbackground = self.blue)
            self.frameAwaySubs.config(bg = self.aqua, highlightbackground = self.blue)
            self.frameLado.config(bg = self.aqua, highlightbackground = self.blue)
            self.frameFoto.config(bg = self.aqua)
            self.entry_time.config(bg = self.purple, fg = self.white)
            self.entry_texto.config(bg = self.purple, fg = self.white)
            self.entry_texto1.config(bg = self.purple, fg = self.white)
            self.time.config(bg = self.purple, fg = self.white)
            self.set1Label.config(bg = self.purple, fg = self.white)
            self.set2Label.config(bg = self.purple, fg = self.white)
            self.AwayFoolsText.config(bg = self.purple, fg = self.white)
            self.localFoolsText.config(bg = self.purple, fg = self.white)
            self.localSubsText.config(bg = self.purple, fg = self.white)
            self.awaySubsText.config(bg = self.purple, fg = self.white)
            self.frameLadoLabel.config(bg = self.aqua, fg = self.black)
        elif opcao == 3: #Tema cinza
            cor1 = "#BFBFBF"
            cor2 = "#D92332"
            self.frame1wid.config(bg = cor1, highlightbackground = self.white)
            self.frame1.config(bg = self.white, highlightbackground = self.white)
            self.frame2.config(bg = self.white, highlightbackground = self.white)
            self.frameTime.config(bg = self.white, highlightbackground = self.white)
            self.frameVisitante.config(bg = self.white, highlightbackground = self.white)
            self.frameLocalLabel.config(bg = self.white, highlightbackground = self.white)
            self.frameLocalFools.config(bg = self.white, highlightbackground = self.white)
            self.frameSet1.config(bg = self.white, highlightbackground = self.white)
            self.frameSet2.config(bg = self.white, highlightbackground = self.white)
            self.frameAwayFools.config(bg = self.white, highlightbackground = self.white)
            self.frameLocalSubs.config(bg = self.white, highlightbackground = self.white)
            self.frameAwaySubs.config(bg = self.white, highlightbackground = self.white)
            self.frameLado.config(bg = self.white, highlightbackground = self.white)
            self.frameFoto.config(bg = self.white)
            self.entry_time.config(bg = cor1, fg = cor2)
            self.entry_texto.config(bg = cor1, fg = cor2)
            self.entry_texto1.config(bg = cor1, fg = cor2)
            self.time.config(bg = cor1, fg = cor2)
            self.set1Label.config(bg = cor1, fg = cor2)
            self.set2Label.config(bg = cor1, fg = cor2)
            self.AwayFoolsText.config(bg = cor1, fg = cor2)
            self.localFoolsText.config(bg = cor1, fg = cor2)
            self.localSubsText.config(bg = cor1, fg = cor2)
            self.awaySubsText.config(bg = cor1, fg = cor2)
            self.frameLadoLabel.config(bg = self.white, fg = cor2)
    
    def esporte_validacao(self):
        esporte = self.esporte.get()
        if self.placarTempo.get() >= 9:
            self.placarTempo.set(9)
            
        if esporte == "Tênis de Mesa":
            diferenca = abs(self.placarLocal.get() - self.placarVisitante.get())
            if diferenca >= 2:
                if self.placarLocal.get() >= 11:
                    self.placarLocal.set(0)
                    self.placarVisitante.set(0)
                    return False
                elif self.placarVisitante.get() >= 11:
                    self.placarVisitante.set(0)
                    self.placarLocal.set(0)
                    return False
            elif diferenca < 2:
                if self.placarLocal.get() >= 10 and self.placarVisitante.get() >= 10:
                    if diferenca >= 2:
                        self.placarLocal.set(0)
                        self.placarVisitante.set(0)
                        return False        
                    
        if esporte == "Futebol":
            if self.placarLocal.get() >= 99:
                self.placarLocal.set(99)
                return False
            elif self.placarVisitante.get() >= 99:
                self.placarVisitante.set(99)
                return False
        
        if esporte == "Voleibol":
            diferenca = abs(self.placarLocal.get() - self.placarVisitante.get())
            if diferenca >= 2:
                if self.placarLocal.get() >= 25:
                    self.placarLocal.set(0)
                    self.placarVisitante.set(0)
                    return False
                if self.placarVisitante.get() >= 25:
                    self.placarVisitante.set(0)
                    self.placarLocal.set(0)
                    return False
            elif diferenca < 2:
                if self.placarLocal.get() >= 24 and self.placarVisitante.get() >= 24:
                    if diferenca >= 2:
                        self.placarLocal.set(0)
                        self.placarVisitante.set(0)
                        return False
        
        if esporte == "Basquete":
            if self.placarLocal.get() >= 99:
                self.placarLocal.set(99)
                return False
            elif self.placarVisitante.get() >= 99:
                self.placarVisitante.set(99)
                return False
        
        if esporte == "Outros":
            if self.placarLocal.get() >= 99:
                self.placarLocal.set(99)
                return False
            elif self.placarVisitante.get() >= 99:
                self.placarVisitante.set(99)
                return False
        
        return True
    
    def serial_Port(self): #Faz a comunicação com a porta serial
        tempo = self.cronometro.get()
        hr, min, seg_milisseg = tempo.split(':')
        seg, milisseg = seg_milisseg.split('.')
        hr = int(hr)
        min = int(min)
        seg = int(seg)
        milisseg = int(milisseg)
        array_bytes = [
                    100,
                    40,
                    133,
                    23,
                    self.placarLocal.get(),
                    self.localFools.get(),
                    self.placarLocalSubs.get(),
                    self.set1.get(),
                    self.placarTempo.get(),
                    self.placarVisitante.get(),
                    self.awayFools.get(),
                    self.placarVisitanteSubs.get(),
                    self.set2.get(),
                    hr, 
                    min, 
                    seg, 
                    milisseg
                    ]
        
        def send(): #Função para enviar os dados pela porta serial
            if self.ser:
                arr_by = bytes(array_bytes)
                self.ser.write(arr_by)
                print(arr_by)
        thread = threading.Thread(target=send)
        thread.start()

    def using_serial(self, use_serial = None):
        try:
            if use_serial:
                self.ser = serial.Serial(
                    port = self.op.device, 
                    baudrate = 115200, 
                    bytesize = 8, 
                    parity = "N", 
                    stopbits = 1, 
                    timeout = int(self.timeout.get())/1000
                )
                self.menu.delete(0, "end")
                print("Sua porta serial está aberta✔")
                messagebox.showinfo("ABERTA✔", "Sua porta serial está aberta✔")
            else:
                self.ser = None
                print("Sua porta serial está fechada✘")
                self.options = list(serial.tools.list_ports.comports())
                for self.option in self.options:
                    self.menu.add_command(label = str(self.option), command = lambda op = self.option: self.select_serial(op))
                messagebox.showinfo("FECHADA✘", "Sua porta serial está fechada✘")
        except serial.SerialException:
            self.ser = None
            print("Não foi possível abrir a porta serial😔")
            messagebox.showerror("Erro", serial.SerialException)
            
    def using_serial2(self, use_serial = None):
        try:
            if use_serial:
                self.ser2 = serial.Serial(
                    port = self.op2.device, 
                    baudrate = 115200, 
                    bytesize = 8, 
                    parity = "N", 
                    stopbits = 1, 
                    timeout = int(self.timeout2.get())/1000
                )
                self.menu2.delete(0, "end")
                print("Sua porta serial está aberta✔")
                messagebox.showinfo("ABERTA✔", "Sua porta serial está aberta✔")
            else:
                self.ser2 = None
                print("Sua porta serial está fechada✘")
                self.options2 = list(serial.tools.list_ports.comports())
                for self.option2 in self.options2:
                    self.menu2.add_command(label = str(self.option2), command = lambda op2 = self.option2: self.select_serial2(op2))
                messagebox.showinfo("FECHADA✘", "Sua porta serial está fechada✘")
        except serial.SerialException:
            self.ser2 = None
            print("Não foi possível abrir a porta serial😔")
            messagebox.showerror("Erro", serial.SerialException)
        
    def select_serial(self, op):
        self.op = op
        print("Serial selecionada:", self.op)
        messagebox.showinfo("Serial selecionada:", self.op)
        
    def select_serial2(self, op2):
        self.op2 = op2
        print("Serial selecionada:", self.op2)
        messagebox.showinfo("Serial selecionada:", self.op2)

    def show_serial(self, event = None):
        messagebox.showinfo("Novas configurações", self.ser)
    
    def show_serial2(self, event = None):
        messagebox.showinfo("Novas configurações", self.ser2)
    
    def open_enter(self):
        try:
            if self.check.get():
                portas = serial.tools.list_ports.comports()
                for porta in portas:
                    try:
                        self.op = porta
                        self.using_serial(True)
                    except serial.SerialException:
                        messagebox.showinfo("Erro", "Nenhuma porta serial encontrada")
            else:
                print("Checkbutton 1 não está marcado")  
                messagebox.showinfo("FECHADA✘", "Sua porta serial está fechada✘")
                self.ser = None
        except serial.SerialException:
            print("Não foi possível abrir a porta serial😔")
            messagebox.showerror("Erro", serial.SerialException)
            self.ser = None
            
    def open_enter2(self):
        try:
            if self.check2.get():
                portas = serial.tools.list_ports.comports()
                for porta in portas:
                    try:
                        self.op2 = porta
                        self.using_serial2(True)
                    except serial.SerialException:
                        messagebox.showinfo("Erro", "Nenhuma porta serial encontrada")
            else:
                print("Checkbutton 2 não está marcado")  
                messagebox.showinfo("FECHADA✘", "Sua porta serial está fechada✘")
                self.ser2 = None
        except serial.SerialException:
            print("Não foi possível abrir a porta serial😔")
            messagebox.showerror("Erro", serial.SerialException)
            self.ser2 = None

if __name__ == "__main__": #Inicia o programa 
    root = Tk()
    app = Interface(root)
    root.mainloop()