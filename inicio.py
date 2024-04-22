from tkinter import *
from PIL import Image, ImageDraw

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.config_tela()
        root.mainloop()

    def config_tela(self):
        self.root.title("Placar Eletrônico")
        self.root.configure(background = "#3c1a7d")
        self.root.geometry("900x900")
        self.root.resizable(True, True)
        self.root.minsize(width = 700, height = 700)
# Informações básicas para abrir a janela 👆
Application()