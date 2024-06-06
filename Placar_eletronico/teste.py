import tkinter as tk

def atalho_pressionado(event):
    print("Atalho pressionado")

root = tk.Tk()

# Função que será executada quando o atalho for pressionado
root.bind("<Control-a>", atalho_pressionado)

root.mainloop()
