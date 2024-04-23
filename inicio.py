from tkinter import *
from tkinter import messagebox
from datetime import datetime

class Interface():
    def __init__(self, root):
        self.root = root
        self.placarLocal = IntVar()
        self.placarLocal.set(0)
        self.placarTempo = IntVar()
        self.placarTempo.set(1)
        self.placarVisitante = IntVar()
        self.placarVisitante.set(0)
        self.cronometro = StringVar()
        self.cronometro.set("00:00:00")
        self.contador = None
        self.config_tela()
        self.frames()
        self.botao()

    def config_tela(self):
        self.root.title("Placar Eletrônico")
        self.root.configure(background = "purple")
        self.root.geometry("900x900")
        self.root.resizable(True, True)
        self.root.minsize(width = 700, height = 700)
        
    def frames(self):
        self.frame1 = Label(self.root, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2, textvariable = self.cronometro, font = ("Arial", 48, "bold"))
        self.frame1.place(relx = 0.15, rely = 0.05, relwidth = 0.75, relheight = 0.2) #Cronometro
        
        self.frameLocalLabel = Label(self.root, textvariable = self.placarLocal, bg = "aqua", font = ("Arial", 48, "bold"), highlightbackground = "Blue", highlightthickness = 2, cursor = "hand1")
        self.frameLocalLabel.place(relx = 0.15, rely = 0.35, relwidth = 0.2, relheight = 0.2)
        self.frameLocalLabel.bind("<Button-1>", lambda event: self.plus(1))
        
        self.frameTime = Label(self.root, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2, font = ("Arial", 48, "bold"), textvariable = self.placarTempo)
        self.frameTime.place(relx = 0.425, rely = 0.35, relwidth = 0.2, relheight = 0.2) #Tempo
        
        self.frameVisitante = Label(self.root, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2, font = ("Arial", 48, "bold"), textvariable = self.placarVisitante,  cursor = "hand1")
        self.frameVisitante.place(relx = 0.70, rely = 0.35, relwidth = 0.2, relheight = 0.2) #Placar time visitante
        self.frameVisitante.bind("<Button-1>", lambda event: self.plus(2))
        
        self.frame2 = Label(self.root, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2)
        self.frame2.place(relx = 0.15, rely = 0.65, relwidth = 0.75, relheight = 0.2) #Botões variados
        
    def botao(self):
        self.bt_game = Button(self.frame2, text = "Esportes")
        self.bt_game.place(relx = 0.42, rely = 0.05, relwidth = 0.15, relheight = 0.15)
        
        self.bt_zero = Button(self.frame2, text = "Zerar")
        self.bt_zero.place(relx = 0.42, rely = 0.25, relwidth = 0.15, relheight = 0.15)
        
        self.bt_plus2 = Button(self.frame2, text = "+2", command = lambda: self.plus2(1))
        self.bt_plus2.place(relx = 0.05, rely = 0.05, relwidth = 0.15, relheight = 0.15)
        self.bt_minus2 = Button(self.frame2, text = "-2", command = lambda: self.minus2(1))
        self.bt_minus2.place(relx = 0.05, rely = 0.25, relwidth = 0.15, relheight = 0.15)
        
        self.bt_plus3 = Button(self.frame2, text = "+3", command = lambda: self.plus3(1))
        self.bt_plus3.place(relx = 0.05, rely = 0.45, relwidth = 0.15, relheight = 0.15)
        self.bt_minus3 = Button(self.frame2, text = "-3", command = lambda: self.minus3(1))
        self.bt_minus3.place(relx = 0.05, rely = 0.65, relwidth = 0.15, relheight = 0.15)
        
        self.bt_plus2_visitante = Button(self.frame2, text = "+2", command = lambda: self.plus2(2))
        self.bt_plus2_visitante.place(relx = 0.8, rely = 0.05, relwidth = 0.15, relheight = 0.15)
        self.bt_minus2_visitante = Button(self.frame2, text = "-2", command = lambda: self.minus2(2))
        self.bt_minus2_visitante.place(relx = 0.8, rely = 0.25, relwidth = 0.15, relheight = 0.15)
        
        self.bt_plus3_visitante = Button(self.frame2, text = "+3", command = lambda: self.plus3(2))
        self.bt_plus3_visitante.place(relx = 0.8, rely = 0.45, relwidth = 0.15, relheight = 0.15)
        self.bt_minus3_visitante = Button(self.frame2, text = "-3", command = lambda: self.minus3(2))
        self.bt_minus3_visitante.place(relx = 0.8, rely = 0.65, relwidth = 0.15, relheight = 0.15)
        
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
            self.placarLocal.set(self.placarLocal.get() - 1)
        elif team == 2:
            self.placarVisitante.set(self.placarVisitante.get() - 1)
    
    def minus2(self, team):
        if team == 1: 
            self.placarLocal.set(self.placarLocal.get() - 2)
        elif team == 2:
            self.placarVisitante.set(self.placarVisitante.get() - 2)
            
    def minus3(self, team):
        if team == 1: 
            self.placarLocal.set(self.placarLocal.get() - 3)
        elif team == 2:
            self.placarVisitante.set(self.placarVisitante.get() - 3)
    
    def update(self):
        if self.contador:
            tempo = datetime.now() - self.contador
            self.cronometro.set(str(tempo).split('.')[0])
        self.root.after(1000, self.update)

    def start(self):
        self.contador = datetime.now()
        self.update()
        
if __name__ == "__main__": 
    root = Tk()
    app = Interface(root)
    app.start()
    root.mainloop()