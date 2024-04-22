from tkinter import *
import time

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.config_tela()
        self.frames()
        self.botao()
        root.mainloop()

    def config_tela(self):
        self.root.title("Placar Eletrônico")
        self.root.configure(background = "purple")
        self.root.geometry("900x900")
        self.root.resizable(True, True)
        self.root.minsize(width = 700, height = 700)
        
    def frames(self):
        self.frame1 = Frame(self.root, bd = 4, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2)
        self.frame1.place(relx = 0.15, rely = 0.05, relwidth = 0.75, relheight = 0.3)
        
        self.frame2 = Frame(self.root, bd = 4, bg = "aqua", highlightbackground = "Blue", highlightthickness = 2)
        self.frame2.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.3)
        
    def botao(self):
        self.bt_game = Button(text = "Esportes")
        self.bt_game.place(relx = 0.05, rely = 0.05, relwidth = 0.1, relheight = 0.03)
        
        self.bt_plus1 = Button(self.frame2, text = "+1")
        self.bt_plus1.place(relx = 0.05, rely = 0.05, relwidth = 0.05, relheight = 0.1)
        self.bt_minus1 = Button(self.frame2, text = "-1")
        self.bt_minus1.place(relx = 0.9, rely = 0.05, relwidth = 0.05, relheight = 0.1)
        
        self.bt_plus2 = Button(self.frame2, text = "+2")
        self.bt_plus2.place(relx = 0.05, rely = 0.25, relwidth = 0.05, relheight = 0.1)
        self.bt_minus2 = Button(self.frame2, text = "-2")
        self.bt_minus2.place(relx = 0.9, rely = 0.25, relwidth = 0.05, relheight = 0.1)
        
        self.bt_plus3 = Button(self.frame2, text = "+3")
        self.bt_plus3.place(relx = 0.05, rely = 0.45, relwidth = 0.05, relheight = 0.1)
        self.bt_minus3 = Button(self.frame2, text = "-3")
        self.bt_minus3.place(relx = 0.9, rely = 0.45, relwidth = 0.05, relheight = 0.1)
    
Application()