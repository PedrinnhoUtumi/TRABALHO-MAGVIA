import tkinter as tk

# Função para verificar o estado do Checkbutton
def verificar_estado():
    if var.get():
        print("Checkbutton ativado")
    else:
        print("Checkbutton desativado")

# Criando a janela principal
root = tk.Tk()

# Criando uma variável de controle
var = tk.BooleanVar()

# Definindo o valor da variável de controle como True para deixar o Checkbutton ativado
var.set(True)

# Criando o Checkbutton e associando-o à variável de controle
checkbutton = tk.Checkbutton(root, text="Checkbutton", variable=var)
checkbutton.pack()

# Botão para verificar o estado do Checkbutton
btn_verificar = tk.Button(root, text="Verificar Estado", command=verificar_estado)
btn_verificar.pack()

# Exibindo a janela
root.mainloop()
