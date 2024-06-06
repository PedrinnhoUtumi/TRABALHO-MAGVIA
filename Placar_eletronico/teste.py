import tkinter as tk

def imprimir_esporte():
    print(esporte.get())

root = tk.Tk()
root.geometry("300x200")

esporte = tk.StringVar()

radio_futebol = tk.Radiobutton(root, text="Futebol", variable=esporte, value="Futebol", command=imprimir_esporte)
radio_futebol.pack(anchor=tk.W)

radio_voleibol = tk.Radiobutton(root, text="Voleibol", variable=esporte, value="Voleibol", command=imprimir_esporte)
radio_voleibol.pack(anchor=tk.W)

radio_basquete = tk.Radiobutton(root, text="Basquete", variable=esporte, value="Basquete", command=imprimir_esporte)
radio_basquete.pack(anchor=tk.W)

root.mainloop()
