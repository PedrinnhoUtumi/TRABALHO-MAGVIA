import tkinter as tk

def clicar():
    print("Botão clicado!")

root = tk.Tk()

canvas = tk.Canvas(root, width=120, height=40, highlightthickness=0)
canvas.pack()

# Coordenadas para desenhar um botão com cantos arredondados
coordenadas = [10, 0, 110, 0, 120, 10, 120, 30, 110, 40, 10, 40, 0, 30, 0, 10]

# Criar o polígono no canvas
button = canvas.create_polygon(coordenadas, fill="lightblue", outline="black", width=2)

# Associar um evento de clique ao polígono
canvas.tag_bind(button, "<Button-1>", lambda event: clicar())

root.mainloop()
