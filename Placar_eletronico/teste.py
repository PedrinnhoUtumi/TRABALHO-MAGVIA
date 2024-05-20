import tkinter as tk

def imprimir_valor():
    valor = spinbox.get()
    print("O valor selecionado é:", valor)

root = tk.Tk()
root.title("Teste Spinbox")

# Função para imprimir o valor atual do Spinbox quando o botão é clicado
botao = tk.Button(root, text="Imprimir Valor", command=imprimir_valor)
botao.pack(pady=10)

# Spinbox para selecionar um valor de 0 a 10
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack()

root.mainloop()
