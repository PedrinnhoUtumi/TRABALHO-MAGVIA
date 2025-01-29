from Interface import Interface
from tkinter import *
from PIL import Image, ImageTk

def abrirTela():
    
    if __name__ == "__main__":
        introducao.destroy()        
        root = Tk()
        interface = Interface(root)
        root.mainloop()
        
        
introducao = Tk()
introducao.geometry("500x300")
introducao.config(bg="white")

imagem = Image.open("./gravadorSerial/site/magvia.png") 
imagem = imagem.resize((500, 300))
imagemTk = ImageTk.PhotoImage(imagem)

label_imagem = Label(introducao, image=imagemTk)
label_imagem.pack()

introducao.after(2000, abrirTela)
introducao.mainloop()
