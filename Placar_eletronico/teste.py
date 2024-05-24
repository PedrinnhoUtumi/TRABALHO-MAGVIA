import tkinter as tk

def show_selected():
    selected_option = var.get()
    label.config(text="Opção selecionada: " + selected_option)

# Criando a janela principal
root = tk.Tk()
root.title("Exemplo de RadioButtons")

# Variável para armazenar a opção selecionada
var = tk.StringVar()

# Criando os RadioButtons
option1 = tk.Radiobutton(root, text="Opção 1", variable=var, value="Opção 1", command=show_selected)
option2 = tk.Radiobutton(root, text="Opção 2", variable=var, value="Opção 2", command=show_selected)
option3 = tk.Radiobutton(root, text="Opção 3", variable=var, value="Opção 3", command=show_selected)

# Posicionando os RadioButtons na janela
option1.pack(anchor="w")
option2.pack(anchor="w")
option3.pack(anchor="w")

# Label para exibir a opção selecionada
label = tk.Label(root)
label.pack()

# Loop principal
root.mainloop()
