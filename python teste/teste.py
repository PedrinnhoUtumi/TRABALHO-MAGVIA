from tkinter import *

class Interface:
    def __init__(self, root):
        self.root = root
        self.criar_menu_button()

    def criar_menu_button(self):
        # Criando um frame e um Menubutton
        self.frame = Frame(self.root)
        self.frame.pack(pady=10)

        self.menu_button = Menubutton(self.frame, text="Escolher Bobina", relief="raised")
        self.menu_button.grid(padx=10, pady=10)

        menu = Menu(self.menu_button, tearoff=0)
        self.menu_button.config(menu=menu)

        menu.add_command(label="Placa Potência", command=self.selecionar_bobina)
        menu.add_command(label="Placa Temperatura", command=self.selecionar_bobina)

        # Botão para excluir o Menubutton
        self.excluir_button = Button(self.frame, text="Excluir Menu", command=self.excluir_menu_button)
        self.excluir_button.grid(pady=10)

    def selecionar_bobina(self):
        print("Você selecionou uma bobina.")

    def excluir_menu_button(self):
        # Excluindo o Menubutton
        self.menu_button.destroy()  # Isso remove o Menubutton da interface
        self.excluir_button.destroy()  # Opcionalmente, removemos o botão de excluir também

# Criando a janela Tkinter
root = Tk()
interface = Interface(root)
root.mainloop()
