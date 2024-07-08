import tkinter as tk

root = tk.Tk()

# Criando um Entry
entry = tk.Entry(root)
entry.pack()

# Texto a ser inserido no Entry
texto = "Texto pré-definido"

# Inserindo o texto no Entry
entry.insert(0, texto)

root.mainloop