import tkinter as tk

def selecionar_opcao(opcao):
    print(f"Opção selecionada: {opcao}")

root = tk.Tk()
root.geometry("300x200")

# Define as opções para os MenuButtons
opcoes = ["Opção 1", "Opção 2", "Opção 3"]

# Cria o primeiro MenuButton
menu_button1 = tk.Menubutton(root, text="MenuButton 1", relief="raised")
menu_button1.menu = tk.Menu(menu_button1, tearoff=0)
menu_button1["menu"] = menu_button1.menu

for opcao in opcoes:
    menu_button1.menu.add_command(label=opcao, command=lambda opcao=opcao: selecionar_opcao(opcao))

menu_button1.pack()

# Cria o segundo MenuButton com as mesmas opções
menu_button2 = tk.Menubutton(root, text="MenuButton 2", relief="raised")
menu_button2.menu = tk.Menu(menu_button2, tearoff=0)
menu_button2["menu"] = menu_button2.menu

for opcao in opcoes:
    menu_button2.menu.add_command(label=opcao, command=lambda opcao=opcao: selecionar_opcao(opcao))

menu_button2.pack()

root.mainloop()
