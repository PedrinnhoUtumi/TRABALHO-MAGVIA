from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta 
import time
import threading
import serial



class Interface():
    def __init__(self, root): #Aqui é onde eu conecto/crio tudo na minha função construtora
        self.ser = None
        self.root = root
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
        self.columnsEntrys = 7
        self.linhasEntrys = 15
        self.esporte = StringVar()
        self.contador = None
        self.tempo_extra = timedelta()
        self.config_tela()
        self.frames()
        self.botao()
        self.using_serial()

    def config_tela(self): #Aqui é onde eu configuro as informações da app
        self.root.title("Placar Eletrônico") #Configura titulo
        self.root.configure(background = "purple") #Configura cor de fundo
        self.root.geometry("1100x1100") #Configura tamanho inicial do app
        self.root.resizable(False, False) #Configura sua responsividade
        self.root.minsize(width = 1100, height = 1100) #Configura tamanho minimo do app
        self.root.maxsize(width = 1100, height = 1100) #Configura tamanho máximo do app
        
    def frames(self):  #Aqui é onde eu configuro frames e abas do app
        self.notebook = ttk.Notebook(self.root) #Cria abas
        self.notebook.pack(fill=BOTH, expand=True)
        
        self.frame1wid = Frame(self.notebook, bg = "purple") #Configura aba 1
        self.notebook.add(self.frame1wid, text="Placar")
        
        self.frame2wid = Frame(self.notebook, bg = "purple") #Configura aba 2
        self.notebook.add(self.frame2wid, text="Configurações")
        
        self.frame3wid = Frame(self.notebook, bg = "purple") #Configura aba 3
        self.notebook.add(self.frame3wid, text="Escalação")
        
        self.frame4wid = Frame(self.notebook, bg = "purple") #Configura aba 4
        self.notebook.add(self.frame4wid, text="Jornal")

        self.frame5wid = Frame(self.notebook, bg = "purple") #Configura aba 4
        self.notebook.add(self.frame5wid, text="24 Segundos")
        
        #Configura os frames na aba 1
        self.frameLado = Label(self.frame1wid, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2, font = ("Courier New", 48, "bold"))
        self.frameLado.place(relx = 0.01, rely = 0.05, relwidth = 0.12, relheight = 0.8)
        
        self.frameLadoLabel = Label(self.frameLado, bg = "aqua", font = ("Courier New", 12, "bold"), fg = "black", text = "Funções")
        self.frameLadoLabel.place(relx = 0.14, rely = 0.05, relwidth = 0.7, relheight = 0.05)
        
        self.frame1 = Label(self.frame1wid, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2, textvariable = self.cronometro, font = ("Courier New", 48, "bold"))
        self.frame1.place(relx = 0.15, rely = 0.05, relwidth = 0.75, relheight = 0.2) #Cronometro
        
        self.entry_texto1 = Entry(self.frame1wid, textvariable=self.texto_entry, font=("Courier New", 12, "bold"), bg = "purple", fg = "white")
        self.entry_texto1.place(relx=0.15, rely=0.3, relwidth=0.2, relheight=0.05) #Nome do time da casa
        
        self.frameLocalLabel = Label(self.frame1wid, textvariable = self.placarLocal, bg = "aqua", font = ("Courier New", 48, "bold"), highlightbackground = "Blue", highlightthickness = 2, cursor = "hand1")
        self.frameLocalLabel.place(relx = 0.15, rely = 0.35, relwidth = 0.2, relheight = 0.2) #Placar do time da casa
        self.frameLocalLabel.bind("<Button-1>", lambda event: self.plus(1)) #Função do placar
        
        self.frameLocalSubs = Label(self.frame1wid, textvariable = self.placarLocalSubs, bg = "aqua", font = ("Courier New", 12, "bold"), highlightbackground = "Blue", highlightthickness = 2, cursor = "hand1")
        self.frameLocalSubs.place(relx = 0.363, rely = 0.35, relwidth = 0.05, relheight = 0.05) #Placar das substituições do time da casa
        self.frameLocalSubs.bind("<Button-1>", lambda event: self.plus(9)) #Função do placar das substituições
        
        self.localSubsText = Label(self.frame1wid, text="Subs", bg = "purple", font=("Courier New", 12, "bold"), fg = "white")
        self.localSubsText.place(relx=0.363, rely=0.4, relwidth=0.05, relheight=0.02) #Texto escrito "Subs"
        
        self.frameLocalFools = Label(self.frame1wid, textvariable = self.localFools, bg = "aqua", font = ("Courier New", 12, "bold"), highlightbackground = "Blue", highlightthickness = 2, cursor = "hand1")
        self.frameLocalFools.place(relx = 0.15, rely = 0.57, relwidth = 0.2, relheight = 0.05) #Placar das faltas do time da casa
        self.frameLocalFools.bind("<Button-1>", lambda event: self.plus(4)) #Função do placar das faltas
        
        self.localFoolsText = Label(self.frame1wid, text="Faltas", bg = "purple", font=("Courier New", 12, "bold"), fg = "white")
        self.localFoolsText.place(relx=0.15, rely=0.63, relwidth=0.2, relheight=0.02) #Texto escrito "Faltas"
        
        self.time = Label(self.frame1wid, text="Tempo", bg = "purple", font=("Courier New", 24, "bold"), fg = "white")
        self.time.place(relx=0.425, rely=0.3, relwidth=0.2, relheight=0.05) #Texto escrito "Tempo"
        
        self.frameTime = Label(self.frame1wid, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2, font = ("Courier New", 48, "bold"), textvariable = self.placarTempo, cursor = "hand1")
        self.frameTime.place(relx = 0.425, rely = 0.35, relwidth = 0.2, relheight = 0.2) #Tempo/Periodo
        self.frameTime.bind("<Button-1>", lambda event: self.plus(3)) #Função do placar do tempo
        
        self.frameSet1 = Label(self.frame1wid, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2, font = ("Courier New", 12, "bold"), textvariable = self.set1, cursor = "hand1") 
        self.frameSet1.place(relx = 0.425, rely = 0.57, relwidth = 0.07, relheight = 0.05) #Placar dos sets do time da casa
        self.frameSet1.bind("<Button-1>", lambda event: self.plus(6)) #Função do placar dos sets do time da casa
        
        self.set1Label = Label(self.frame1wid, text="Set", bg = "purple", font=("Courier New", 10, "bold"), fg = "white")
        self.set1Label.place(relx=0.43, rely=0.62, relwidth=0.05, relheight=0.03) #Texto escrito "Set"
        
        self.frameSet2 = Label(self.frame1wid, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2, font = ("Courier New", 12, "bold"), textvariable = self.set2, cursor = "hand1") 
        self.frameSet2.place(relx = 0.555, rely = 0.57, relwidth = 0.07, relheight = 0.05) #Placar dos sets do time visitante
        self.frameSet2.bind("<Button-1>", lambda event: self.plus(7)) #Função do placar dos sets do time visitante
        
        self.set2Label = Label(self.frame1wid, text="Set", bg = "purple", font=("Courier New", 10, "bold"), fg = "white")
        self.set2Label.place(relx=0.57, rely=0.62, relwidth=0.05, relheight=0.03) #Texto escrito "Set"
        
        self.entry_texto = Entry(self.frame1wid, textvariable=self.texto_entry2, font=("Courier New", 12, "bold"), bg = "purple", fg = "white")
        self.entry_texto.place(relx=0.70, rely=0.3, relwidth=0.2, relheight=0.05) #Nome do time visitante
        
        self.frameVisitante = Label(self.frame1wid, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2, font = ("Courier New", 48, "bold"), textvariable = self.placarVisitante, cursor = "hand1")
        self.frameVisitante.place(relx = 0.70, rely = 0.35, relwidth = 0.2, relheight = 0.2) #Placar time visitante
        self.frameVisitante.bind("<Button-1>", lambda event: self.plus(2)) #Função do placar do time visitante
        
        self.frameAwaySubs = Label(self.frame1wid, textvariable = self.placarVisitanteSubs, bg = "aqua", font = ("Courier New", 12, "bold"), highlightbackground = "Blue", highlightthickness = 2, cursor = "hand1")
        self.frameAwaySubs.place(relx = 0.637, rely = 0.35, relwidth = 0.05, relheight = 0.05) #Placar das substituições do time visitante
        self.frameAwaySubs.bind("<Button-1>", lambda event: self.plus(10)) #Função do placar das substituições
        
        self.awaySubsText = Label(self.frame1wid, text="Subs", bg = "purple", font=("Courier New", 12, "bold"), fg = "white")
        self.awaySubsText.place(relx=0.637, rely=0.4, relwidth=0.05, relheight=0.02) #Texto escrito "Subs"

        
        self.frameAwayFools = Label(self.frame1wid, textvariable = self.awayFools, bg = "aqua", font = ("Courier New", 12, "bold"), highlightbackground = "Blue", highlightthickness = 2, cursor = "hand1")
        self.frameAwayFools.place(relx = 0.70, rely = 0.57, relwidth = 0.2, relheight = 0.05) #Placar das faltas do time visitante
        self.frameAwayFools.bind("<Button-1>", lambda event: self.plus(5)) #Função do placar das faltas do time visitante
        
        self.AwayFoolsText = Label(self.frame1wid, text="Faltas", bg = "purple", font=("Courier New", 12, "bold"), fg = "white")
        self.AwayFoolsText.place(relx=0.70, rely=0.63, relwidth=0.2, relheight=0.02) #Texto escrito "Faltas"
        
        self.frame2 = Label(self.frame1wid, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2)
        self.frame2.place(relx = 0.15, rely = 0.65, relwidth = 0.75, relheight = 0.2) #Botões variados
        
        #Configura os frames na aba 2
        self.frame1wid2Label = Label(self.frame2wid, bg = "purple", font = ("Courier New", 12, "bold"), fg = "White", text = "Esporte")
        self.frame1wid2Label.place(relx = 0.15, rely = 0.2, relwidth = 0.2, relheight = 0.2) 
        
        self.frame2wid2Label = Label(self.frame2wid, bg = "purple", font = ("Courier New", 12, "bold"), fg = "White", text = "Cronômetro")
        self.frame2wid2Label.place(relx = 0.15, rely = 0.5, relwidth = 0.2, relheight = 0.2) 
        
        self.frame3wid2Label = Label(self.frame2wid, bg = "purple", font = ("Courier New", 12, "bold"), fg = "White", text = "Mudar tema")
        self.frame3wid2Label.place(relx = 0.425, rely = 0.2, relwidth = 0.2, relheight = 0.2) 
        
        self.frame4wid2Label = Label(self.frame2wid, bg = "purple", font = ("Courier New", 12, "bold"), fg = "White", text = "Comunicação Serial")
        self.frame4wid2Label.place(relx = 0.4, rely = 0.5, relwidth = 0.25, relheight = 0.2) 
        
        self.frame5wid2Label = Label(self.frame2wid, bg = "purple", font = ("Courier New", 12, "bold"), fg = "White", text = "Atalhos")
        self.frame5wid2Label.place(relx = 0.7, rely = 0.2, relwidth = 0.2, relheight = 0.2) 
        
        self.frame6wid2Label = Label(self.frame2wid, bg = "purple", font = ("Courier New", 12, "bold"), fg = "White", text = "#")
        self.frame6wid2Label.place(relx = 0.7, rely = 0.5, relwidth = 0.2, relheight = 0.2) 
        
        self.frame1wid2 = Label(self.frame2wid, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2, font = ("Courier New", 48, "bold"))
        self.frame1wid2.place(relx = 0.15, rely = 0.05, relwidth = 0.2, relheight = 0.2) 
        
        self.frame2wid2 = Label(self.frame2wid, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2)
        self.frame2wid2.place(relx = 0.15, rely = 0.65, relwidth = 0.2, relheight = 0.2) 
        
        self.frame3wid2 = Label(self.frame2wid, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2, font = ("Courier New", 48, "bold"))
        self.frame3wid2.place(relx = 0.425, rely = 0.05, relwidth = 0.2, relheight = 0.2) 
        
        self.frame4wid2 = Label(self.frame2wid, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2)
        self.frame4wid2.place(relx = 0.425, rely = 0.65, relwidth = 0.2, relheight = 0.2) 
        
        self.frame5wid2 = Label(self.frame2wid, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2, font = ("Courier New", 48, "bold"))
        self.frame5wid2.place(relx = 0.7, rely = 0.05, relwidth = 0.2, relheight = 0.2) 
        
        self.frame6wid2 = Label(self.frame2wid, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2)
        self.frame6wid2.place(relx = 0.7, rely = 0.65, relwidth = 0.2, relheight = 0.2) 
        
        #Configura os frames da aba 3
        self.frame1wid3Label = Label(self.frame3wid, bg = "purple", fg = "white", text = "Time Local Esquerda")
        self.frame1wid3Label.place(relx = 0.05, rely = 0.01, relwidth = 0.15, relheight = 0.05)
        
        self.frame1wid3 = Label(self.frame3wid, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2)
        self.frame1wid3.place(relx = 0.05, rely = 0.05, relwidth = 0.4, relheight = 0.75)
        
        self.frame2wid3Label = Label(self.frame3wid, bg = "purple", fg = "white", text = "Time Visitante Direita")
        self.frame2wid3Label.place(relx = 0.5, rely = 0.01, relwidth = 0.15, relheight = 0.05)
        
        self.frame2wid3 = Label(self.frame3wid, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2)
        self.frame2wid3.place(relx = 0.5, rely = 0.05, relwidth = 0.4, relheight = 0.75)
        
        #Configura os frames da aba 4
        self.frame1wid4Label = Label(self.frame4wid, bg = "purple", fg = "white", text = "Serial dos 24 segundos")
        self.frame1wid4Label.place(relx = 0.05, rely = 0.01, relwidth = 0.15, relheight = 0.05)
        
        self.frame1wid4 = Label(self.frame4wid, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2)
        self.frame1wid4.place(relx = 0.05, rely = 0.05, relwidth = 0.4, relheight = 0.75)
        
        self.frame2wid4Label = Label(self.frame4wid, bg = "purple", fg = "white", text = "Terminal")
        self.frame2wid4Label.place(relx = 0.5, rely = 0.01, relwidth = 0.15, relheight = 0.05)
        
        self.frame2wid4 = Label(self.frame4wid, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2)
        self.frame2wid4.place(relx = 0.5, rely = 0.05, relwidth = 0.4, relheight = 0.75)

        self.framecithec = Label(self.frame2wid4, bg = "aqua", fg = "black", text = "TERMINAL 24 SEG.", font = ("Courier New", 24, "bold"))
        self.framecithec.place(relx = 0, rely = 0.15, relwidth = 0.9, relheight = 0.05)

        self.framecithec2 = Label(self.frame2wid4, bg = "aqua", fg = "black", text = "CITHEC - V.12/16", font = ("Courier New", 24, "bold"))
        self.framecithec2.place(relx = 0, rely = 0.25, relwidth = 0.9, relheight = 0.05)

    def botao(self):
        #Botôes de controle
        self.bt_start = Button(self.frameLado, text = "Iniciar", cursor = "clock", command = self.start_timer)
        self.bt_start.place(relx = 0.15, rely = 0.15, relwidth = 0.7, relheight = 0.03) #Iniciar cronômetro
        self.root.bind("<space>", self.start_timer)
        
        self.bt_zero = Button(self.frameLado, text = "Zerar", command = self.zero, cursor = "hand1")
        self.bt_zero.place(relx = 0.15, rely = 0.2, relwidth = 0.7, relheight = 0.03) #Zerar toda a página
        self.root.bind("0", self.zero)
        
        self.bt_pause = Button(self.frameLado, text = "Pausar", command = lambda: self.pause(1), cursor = "hand1")
        self.bt_pause.place(relx = 0.15, rely = 0.25, relwidth = 0.7, relheight = 0.03) #Pausar cronômetro
        self.root.bind("<Control-u>", lambda event: self.pause(1))
        
        self.bt_reniciar = Button(self.frameLado, text = "Reiniciar", command = lambda: self.pause(2), cursor = "hand1")
        self.bt_reniciar.place(relx = 0.15, rely = 0.3, relwidth = 0.7, relheight = 0.03) #Reinciar cronômetro
        self.root.bind("<Control-i>", lambda event: self.pause(2))
        
        self.bt_continue = Button(self.frameLado, text = "Continuar", cursor = "hand1", command = lambda: self.pause(3))
        self.bt_continue.place(relx = 0.15, rely = 0.35, relwidth = 0.7, relheight = 0.03) #Continuar cronômetro após pausa
        self.root.bind("<Control-o>", lambda event: self.pause(3))
        
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
        self.bt_theme = Button(self.frame3wid2, text = "Tema verde", command = lambda: self.change_theme(1), cursor = "hand1")
        self.bt_theme.place(relx = 0.15, rely = 0.05, relwidth = 0.7, relheight = 0.15) #Mudar tema para verde
        
        self.bt_theme2 = Button(self.frame3wid2, text = "Tema roxo", command = lambda: self.change_theme(2), cursor = "hand1")
        self.bt_theme2.place(relx = 0.15, rely = 0.25, relwidth = 0.7, relheight = 0.15) #Mudar tema para roxo

        self.bt_theme3 = Button(self.frame3wid2, text = "Tema cinza", command = lambda: self.change_theme(3), cursor = "hand1")
        self.bt_theme3.place(relx = 0.15, rely = 0.45, relwidth = 0.7, relheight = 0.15) #Mudar tema para cinza

        self.bt_serial_open = Button(self.frame4wid2, text = "Abre serial", command = lambda: self.using_serial(True), cursor = "hand1")
        self.bt_serial_open.place(relx = 0.15, rely = 0.05, relwidth = 0.7, relheight = 0.15) #Abre a porta serial

        self.bt_serial_close = Button(self.frame4wid2, text = "Fecha serial", command = lambda: self.using_serial(False), cursor = "hand1")
        self.bt_serial_close.place(relx = 0.15, rely = 0.25, relwidth = 0.7, relheight = 0.15) #Fecha a porta serial 

        self.bt_choose_serial = Menubutton(self.frame4wid2, text = "Escolhe serial", cursor = "hand1", relief="raised")
        self.bt_choose_serial.place(relx = 0.15, rely = 0.45, relwidth = 0.7, relheight = 0.15) #Escolhe a porta serial
        self.menu = Menu(self.bt_choose_serial, tearoff = 0)
        self.bt_choose_serial.config(menu = self.menu)

        self.timeout = Spinbox(self.frame4wid2, from_ = 0, to = 1000, cursor = "hand1", background = "aqua")
        self.timeout.place(relx = 0.15, rely = 0.65, relwidth = 0.7, relheight = 0.15)
        
        self.new_data = Button(self.frame4wid2, text = "Enviar serial", command = self.set_serial, cursor = "hand1")
        self.new_data.place(relx = 0.15, rely = 0.85, relwidth = 0.7, relheight = 0.15)

        self.bt_add1min = Button(self.frame2wid2, text = "+1 minuto", cursor = "hand1", command = self.add_minute)
        self.bt_add1min.place(relx = 0.15, rely = 0.05, relwidth = 0.7, relheight = 0.15) #Adiciona 1 minuto ao cronômetro

        self.bt_minus1min = Button(self.frame2wid2, text = "-1 minuto", cursor = "hand1")
        self.bt_minus1min.place(relx = 0.15, rely = 0.25, relwidth = 0.7, relheight = 0.15) #Remove 1 minuto ao cronômetro
        
        self.entry_time = Entry (self.frame2wid2, cursor = "hand1")
        self.entry_time.place(relx = 0.15, rely = 0.45, relwidth = 0.7, relheight = 0.15)

        self.front = Button(self.frame2wid2, text = "Anda para frente ⏩", cursor = "hand1")
        self.front.place(relx = 0.15, rely = 0.65, relwidth = 0.7, relheight = 0.15)

        self.back = Button(self.frame2wid2, text = "⏪ Anda pra trás", cursor = "hand1")
        self.back.place(relx = 0.15, rely = 0.85, relwidth = 0.7, relheight = 0.15)

        self.choose_game = Radiobutton(self.frame1wid2, cursor = "hand1", text = "Futebol", bg = "aqua", variable = self.esporte, value = "Futebol")
        self.choose_game.place(relx = 0.15, rely = 0.05, relwidth = 0.7, relheight = 0.15)
        
        self.choose_game2 = Radiobutton(self.frame1wid2, cursor = "hand1", text = "Voleibol", bg = "aqua", variable = self.esporte, value = "Voleibol")
        self.choose_game2.place(relx = 0.15, rely = 0.25, relwidth = 0.7, relheight = 0.15)
        
        self.choose_game3 = Radiobutton(self.frame1wid2, cursor = "hand1", text = "Basquete", bg = "aqua", variable = self.esporte, value = "Basquete")
        self.choose_game3.place(relx = 0.15, rely = 0.45, relwidth = 0.7, relheight = 0.15)
        
        self.choose_game4 = Radiobutton(self.frame1wid2, cursor = "hand1", text = "Tênis de Mesa", bg = "aqua", variable = self.esporte, value = "Tênis de Mesa")
        self.choose_game4.place(relx = 0.15, rely = 0.65, relwidth = 0.7, relheight = 0.15)
        
        self.choose_game5 = Radiobutton(self.frame1wid2, cursor = "hand1", text = "Outros", bg = "aqua", variable = self.esporte, value = "Outros")
        self.choose_game5.place(relx = 0.15, rely = 0.85, relwidth = 0.7, relheight = 0.15)
        
        self.controles = Label(self.frame5wid2, bg = "aqua", text = "Espaço = Inicia")
        self.controles.place(relx = 0.15, rely = 0.05, relwidth = 0.7, relheight = 0.15)
        
        self.controles = Label(self.frame5wid2, bg = "aqua", text = "0 = Zerar")
        self.controles.place(relx = 0.15, rely = 0.25, relwidth = 0.7, relheight = 0.15)
        
        self.controles = Label(self.frame5wid2, bg = "aqua", text = "Ctrl + u = Pausar")
        self.controles.place(relx = 0.15, rely = 0.45, relwidth = 0.7, relheight = 0.15)
        
        self.controles = Label(self.frame5wid2, bg = "aqua", text = "Ctrl + i = Reiniciar")
        self.controles.place(relx = 0.15, rely = 0.65, relwidth = 0.7, relheight = 0.15)

        self.controles = Label(self.frame5wid2, bg = "aqua", text = "Ctrl + o = Continuar")
        self.controles.place(relx = 0.15, rely = 0.85, relwidth = 0.7, relheight = 0.15)
        
    #Botões da aba 4
        self.ativar = Checkbutton(self.frame2wid4, bg = "aqua", text = "Ativar simulador 24 segundos")
        self.ativar.place(relx = 0, rely = 0.05, relwidth = 0.5, relheight = 0.05)

    def plus(self, team): #Definindo a função que vai adicionar os pontos, sets etc
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
        if team == 1: 
            self.placarLocal.set(self.placarLocal.get() + 2)
        elif team == 2:
            self.placarVisitante.set(self.placarVisitante.get() + 2)            
        self.serial_Port()
        
    def plus3(self, team): #Defiinindo a função que vai adicionar 3 pontos
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
            total_milliseconds = int(tempo.total_seconds() * 10)
            horas, resto = divmod(total_milliseconds, 36000)
            minutos, resto = divmod(resto, 600)
            segundos, milissegundos = divmod(resto, 10)
            self.cronometro.set(f"{int(horas):02}:{int(minutos):02}:{int(segundos):02}.{int(milissegundos):01}")
        if milissegundos == 1:
            self.root.after(1000, self.serial_Port)

        self.root.after(90, self.update)
        
    def add_minute(self):
        if self.contador:
            self.contador -= timedelta(minutes=1)
        else:
            self.contador = datetime.now() - timedelta(minutes=1)
        self.serial_Port()

    def min_minute(self):
        if self.contador:
            self.contador += timedelta(minutes=1)
        else:
            self.contador = datetime.now() + timedelta(minutes=1)
        self.serial_Port()
        
    def zero(self, event = None): #Definindo tudo para seu número/caractere inicial
        self.placarLocal.set(0)
        self.placarTempo.set(1)
        self.placarVisitante.set(0)
        self.set1.set(0)
        self.set2.set(0)
        self.cronometro.set("0:00:00.0")
        self.texto_entry.set("")
        self.texto_entry2.set("")
        self.localFools.set(0)
        self.awayFools.set(0)
        self.placarVisitanteSubs.set(0)
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
            
    def start_timer(self, event = None): #Inicia o cronômetro
        if not self.contador:  #Apenas inicie se o contador não estiver ativado
            self.contador = datetime.now()
            self.update()
            self.serial_Port()
            print("iniciando...")
            
    def change_theme(self, opcao): #Muda os temas
        if opcao == 1: #Tema verde
            yellow = "#111111"
            orange = "#0CF22F"
            black = "#0CF22F"
            self.frame1wid.config(bg = yellow, highlightbackground = yellow)
            self.frame1.config(bg = orange, highlightbackground = yellow)
            self.frame2.config(bg = orange, highlightbackground = yellow)
            self.frameTime.config(bg = orange, highlightbackground = yellow)
            self.frameVisitante.config(bg = orange, highlightbackground = yellow)
            self.frameLocalLabel.config(bg = orange, highlightbackground = yellow)
            self.frameLocalFools.config(bg = orange, highlightbackground = yellow)
            self.frameSet1.config(bg = orange, highlightbackground = yellow)
            self.frameSet2.config(bg = orange, highlightbackground = yellow)
            self.frameAwayFools.config(bg = orange, highlightbackground = yellow)
            self.frameLocalSubs.config(bg = orange, highlightbackground = yellow)
            self.frameAwaySubs.config(bg = orange, highlightbackground = yellow)
            self.frameLado.config(bg = orange, highlightbackground = yellow)
            self.entry_time.config(bg = yellow, fg = black)
            self.entry_texto.config(bg = yellow, fg = black)
            self.entry_texto1.config(bg = yellow, fg = black)
            self.time.config(bg = yellow, fg = black)
            self.set1Label.config(bg = yellow, fg = black)
            self.set2Label.config(bg = yellow, fg = black)
            self.AwayFoolsText.config(bg = yellow, fg = black)
            self.localFoolsText.config(bg = yellow, fg = black)
            self.localSubsText.config(bg = yellow, fg = black)
            self.awaySubsText.config(bg = yellow, fg = black)
            self.frameLadoLabel.config(bg = orange, fg = black)
        elif opcao == 2: #Tema roxo
            cor1 = "purple"
            self.frame1wid.config(bg = cor1, highlightbackground = "Blue")
            self.frame1.config(bg = "aqua", highlightbackground = "Blue")
            self.frame2.config(bg = "aqua", highlightbackground = "Blue")
            self.frameTime.config(bg = "aqua", highlightbackground = "Blue")
            self.frameVisitante.config(bg = "aqua", highlightbackground = "Blue")
            self.frameLocalLabel.config(bg = "aqua", highlightbackground = "Blue")
            self.frameLocalFools.config(bg = "aqua", highlightbackground = "Blue")
            self.frameSet1.config(bg = "aqua", highlightbackground = "Blue")
            self.frameSet2.config(bg = "aqua", highlightbackground = "Blue")
            self.frameAwayFools.config(bg = "aqua", highlightbackground = "Blue")
            self.frameLocalSubs.config(bg = "aqua", highlightbackground = "Blue")
            self.frameAwaySubs.config(bg = "aqua", highlightbackground = "Blue")
            self.frameLado.config(bg = "aqua", highlightbackground = "Blue")
            self.entry_time.config(bg = cor1, fg = "white")
            self.entry_texto.config(bg = cor1, fg = "white")
            self.entry_texto1.config(bg = cor1, fg = "white")
            self.time.config(bg = cor1, fg = "white")
            self.set1Label.config(bg = cor1, fg = "white")
            self.set2Label.config(bg = cor1, fg = "white")
            self.AwayFoolsText.config(bg = cor1, fg = "white")
            self.localFoolsText.config(bg = cor1, fg = "white")
            self.localSubsText.config(bg = cor1, fg = "white")
            self.awaySubsText.config(bg = cor1, fg = "white")
            self.frameLadoLabel.config(bg = "aqua", fg = "black")
        elif opcao == 3: #Tema cinza
            self.frame1wid.config(bg = "lightgray", highlightbackground = "white")
            self.frame1.config(bg = "white", highlightbackground = "white")
            self.frame2.config(bg = "white", highlightbackground = "white")
            self.frameTime.config(bg = "white", highlightbackground = "white")
            self.frameVisitante.config(bg = "white", highlightbackground = "white")
            self.frameLocalLabel.config(bg = "white", highlightbackground = "white")
            self.frameLocalFools.config(bg = "white", highlightbackground = "white")
            self.frameSet1.config(bg = "white", highlightbackground = "white")
            self.frameSet2.config(bg = "white", highlightbackground = "white")
            self.frameAwayFools.config(bg = "white", highlightbackground = "white")
            self.frameLocalSubs.config(bg = "white", highlightbackground = "white")
            self.frameAwaySubs.config(bg = "white", highlightbackground = "white")
            self.frameLado.config(bg = "white", highlightbackground = "white")
            self.entry_time.config(bg = "lightgray", fg = "red")
            self.entry_texto.config(bg = "lightgray", fg = "red")
            self.entry_texto1.config(bg = "lightgray", fg = "red")
            self.time.config(bg = "lightgray", fg = "red")
            self.set1Label.config(bg = "lightgray", fg = "red")
            self.set2Label.config(bg = "lightgray", fg = "red")
            self.AwayFoolsText.config(bg = "lightgray", fg = "red")
            self.localFoolsText.config(bg = "lightgray", fg = "red")
            self.localSubsText.config(bg = "lightgray", fg = "red")
            self.awaySubsText.config(bg = "lightgray", fg = "red")
            self.frameLadoLabel.config(bg = "white", fg = "red")
            
    def serial_Port(self): #Faz a comunicação com a porta serial
        array_bytes = [100,
                     40,
                     133,
                     23,
                     self.placarLocal.get(),
                     self.localFools.get(),
                     self.placarLocalSubs.get(),
                     self.set1.get(),
                     self.placarVisitante.get(),
                     self.awayFools.get(),
                     self.placarVisitanteSubs.get(),
                     self.set2.get(),
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
                    port = "COM5", 
                    baudrate = 115200, 
                    bytesize = 8, 
                    parity = "N", 
                    stopbits = 1, 
                    timeout = 1.0
                )
                print("Sua porta serial está aberta✔")
                messagebox.showinfo("Você abriu!!!", "Sua porta serial está aberta✔")
                self.options = ["COM1", "COM2" , "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "COM10"]
                for self.option in self.options:
                    self.menu.add_command(label = str(self.option), command = lambda op = self.option: self.select_serial(op))
            else:
                self.ser = None
                self.menu.delete(0, "end")
                print("Sua porta serial está fechada✘")
                messagebox.showinfo("Você fechou!!!", "Sua porta serial está fechada✘")
        except serial.SerialException:
            self.ser = None
            print("Não foi possível abrir a porta serial😔")
            messagebox.showerror("Erro", serial.SerialException)

    def select_serial(self, op):
        self.op = op
        print("Serial selecionada:", self.op)
        messagebox.showinfo("Serial selecionada:", self.op)

    def set_serial(self):
        try:
            self.ser.port = self.op
            self.ser.timeout = int(self.timeout.get())/1000
            messagebox.showinfo("Novas configurações", self.ser)
        except serial.SerialException:
            messagebox.showerror("Não foi possivel", serial.SerialException)

if __name__ == "__main__": #Inicia o programa 
    root = Tk()
    app = Interface(root)
    root.mainloop()


"""
Checkbutton: várias opções selecionáveis
Radiobutton: uma opção selecionável
Menubutton: dropdown
Spínbox: Números
"""