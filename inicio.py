from tkinter import *
from tkinter import messagebox
from datetime import datetime
import os

class Interface():
    def __init__(self, root):
        self.root = root
        self.placarLocal = IntVar()
        self.placarLocal.set(0)
        self.placarTempo = IntVar()
        self.placarTempo.set(1)
        self.localFools = IntVar()
        self.localFools.set(0)
        self.placarVisitante = IntVar()
        self.placarVisitante.set(0)
        self.tempo_correndo = False
        self.cronometro = StringVar()
        self.cronometro.set("0:00:00")
        self.contador = None
        self.config_tela()
        self.frames()
        self.botao()

    def config_tela(self):
        self.root.title("Placar Eletrônico")
        self.root.configure(background = "purple")
        self.root.geometry("900x900")
        self.root.resizable(True, True)
        self.root.minsize(width = 750, height = 750)
        
    def frames(self):
        self.frame1 = Label(self.root, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2, textvariable = self.cronometro, font = ("Courier New", 48, "bold"))
        self.frame1.place(relx = 0.15, rely = 0.05, relwidth = 0.75, relheight = 0.2) #Cronometro
        
        self.frameLocalLabel = Label(self.root, textvariable = self.placarLocal, bg = "aqua", font = ("Courier New", 48, "bold"), highlightbackground = "Blue", highlightthickness = 2, cursor = "hand1")
        self.frameLocalLabel.place(relx = 0.15, rely = 0.35, relwidth = 0.2, relheight = 0.2)
        self.frameLocalLabel.bind("<Button-1>", lambda event: self.plus(1))
        
        self.frameTime = Label(self.root, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2, font = ("Courier New", 48, "bold"), textvariable = self.placarTempo)
        self.frameTime.place(relx = 0.425, rely = 0.35, relwidth = 0.2, relheight = 0.2) #Tempo
        
        self.frameVisitante = Label(self.root, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2, font = ("Courier New", 48, "bold"), textvariable = self.placarVisitante, cursor = "hand1")
        self.frameVisitante.place(relx = 0.70, rely = 0.35, relwidth = 0.2, relheight = 0.2) #Placar time visitante
        self.frameVisitante.bind("<Button-1>", lambda event: self.plus(2))
        
        self.frame2 = Label(self.root, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2)
        self.frame2.place(relx = 0.15, rely = 0.65, relwidth = 0.75, relheight = 0.2) #Botões variados
        
    def botao(self):
        self.bt_start = Button(self.frame2, text = "Iniciar", cursor = "hand1", command = self.start_timer)
        self.bt_start.place(relx = 0.42, rely = 0.05, relwidth = 0.15, relheight = 0.15)
        
        self.bt_zero = Button(self.frame2, text = "Zerar", command = self.zero, cursor = "hand1")
        self.bt_zero.place(relx = 0.42, rely = 0.25, relwidth = 0.15, relheight = 0.15)
        
        self.bt_pause = Button(self.frame2, text = "Pausar", command = lambda: self.pause(1), cursor = "hand1")
        self.bt_pause.place(relx = 0.42, rely = 0.45, relwidth = 0.15, relheight = 0.15)
        
        self.bt_reniciar = Button(self.frame2, text = "Reiniciar", command = lambda: self.pause(2), cursor = "hand1")
        self.bt_reniciar.place(relx = 0.42, rely = 0.65, relwidth = 0.15, relheight = 0.15)
        
        self.bt_continue = Button(self.frame2, text = "Continuar", cursor = "hand1", command = self.continuar)
        self.bt_continue.place(relx = 0.61, rely = 0.05, relwidth = 0.15, relheight = 0.15)
        
        self.bt_alternar_modo = Button(self.frame2, text="Alternar Modo", cursor="hand1", command = self.alternar_modo)
        self.bt_alternar_modo.place(relx = 0.61, rely = 0.25, relwidth = 0.15, relheight = 0.15)
        
        self.bt_minus = Button(self.frame2, text = "-1", command = lambda: self.minus(1), cursor = "hand1")
        self.bt_minus.place(relx = 0.05, rely = 0.05, relwidth = 0.15, relheight = 0.15)
        
        self.plus1 = Button(self.frame2, text = "+1", command = lambda: self.plus(1), cursor = "hand1")
        self.plus1.place(relx = 0.05, rely = 0.25, relwidth = 0.15, relheight = 0.15)
        
        self.bt_plus2 = Button(self.frame2, text = "+2", command = lambda: self.plus2(1), cursor = "hand1")
        self.bt_plus2.place(relx = 0.05, rely = 0.45, relwidth = 0.15, relheight = 0.15)
        
        self.bt_plus3 = Button(self.frame2, text = "+3", command = lambda: self.plus3(1), cursor = "hand1")
        self.bt_plus3.place(relx = 0.05, rely = 0.65, relwidth = 0.15, relheight = 0.15)
        
        self.bt_minus_visitante = Button(self.frame2, text = "-1", command = lambda: self.minus(2), cursor = "hand1")
        self.bt_minus_visitante.place(relx = 0.8, rely = 0.05, relwidth = 0.15, relheight = 0.15)
        
        self.plus_visitante = Button(self.frame2, text = "+1", command = lambda: self.plus(2), cursor = "hand1")
        self.plus_visitante.place(relx = 0.8, rely = 0.25, relwidth = 0.15, relheight = 0.15)
         
        self.bt_plus2_visitante = Button(self.frame2, text = "+2", command = lambda: self.plus2(2), cursor = "hand1")
        self.bt_plus2_visitante.place(relx = 0.8, rely = 0.45, relwidth = 0.15, relheight = 0.15)
        
        self.bt_plus3_visitante = Button(self.frame2, text = "+3", command = lambda: self.plus3(2), cursor = "hand1")
        self.bt_plus3_visitante.place(relx = 0.8, rely = 0.65, relwidth = 0.15, relheight = 0.15)
        
    def plus(self, team):
        if team == 1: 
            self.placarLocal.set(self.placarLocal.get() + 1)
        elif team == 2:
            self.placarVisitante.set(self.placarVisitante.get() + 1)

    def plus2(self, team):
        if team == 1: 
            self.placarLocal.set(self.placarLocal.get() + 2)
        elif team == 2:
            self.placarVisitante.set(self.placarVisitante.get() + 2)
    
    def plus3(self, team):
        if team == 1: 
            self.placarLocal.set(self.placarLocal.get() + 3)
        elif team == 2:
            self.placarVisitante.set(self.placarVisitante.get() + 3)
    
    def minus(self, team):
        if team == 1: 
            if self.validate(1):
                self.placarLocal.set(self.placarLocal.get() - 1)
        elif team == 2:
            if self.validate(2):
                self.placarVisitante.set(self.placarVisitante.get() - 1)
    
    def update(self):
        if self.contador:
            tempo = datetime.now() - self.contador
            self.cronometro.set(str(tempo).split('.')[0])
        self.root.after(10, self.update)
        
    def zero(self):
        self.placarLocal.set(0)
        self.placarTempo.set(1)
        self.placarVisitante.set(0)
        self.contador = datetime.now()
        self.update()
        
    def pause(self, opcao):
        if opcao == 1:
            self.contador_pause = datetime.now() - self.contador
            self.contador = None
        elif opcao == 2:
            self.contador = datetime.now()
            self.update()
    
    def validate(self, opcao):
        if opcao == 1:
            if self.placarLocal.get() <= 0:
                self.placarLocal.set(0)
                return False
        elif opcao == 2:
            if self.placarVisitante.get() <= 0:
                self.placarVisitante.set(0)
                return False
        return True
            
    def continuar(self):
        if self.contador_pause:
            self.contador = datetime.now() - self.contador_pause
            self.update()
            self.contador_pause = None
                
    def alternar_modo(self):
        if self.tempo_correndo:  
            self.pause(1)

        if self.cronometro.get() == "0:00:00":  
            self.tempo_correndo = False
            self.cronometro.set(str(self.tempo_inicial))
        else:  
            self.tempo_correndo = True
            self.contador = datetime.now()
            self.update()
        
    def start_timer(self):
        if not self.contador:  # Apenas inicie se o contador não estiver ativado
            self.contador = datetime.now()
            self.update()
        
if __name__ == "__main__": 
    root = Tk()
    app = Interface(root)
    root.mainloop()