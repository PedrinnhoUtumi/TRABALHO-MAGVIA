from tkinter import Tk, Label
from PIL import Image, ImageTk

class Interface:
    def __init__(self, root):
        self.root = root
        self.frames()

    def frames(self):
        # Carregar a imagem usando o Pillow (PIL)
        imagem = Image.open("magvia.png")
        # Converter para um formato que o tkinter pode usar
        self.imagem_tk = ImageTk.PhotoImage(imagem)

        # Criar um Label para exibir a imagem
        self.frameFoto = Label(self.root, image=self.imagem_tk)
        self.frameFoto.pack()

if __name__ == "__main__":
    root = Tk()
    app = Interface(root)
    root.mainloop()
