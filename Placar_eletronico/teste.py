import tkinter as tk
import pickle

# Função para salvar o estado do Checkbutton em um arquivo
def salvar_estado():
    with open("estado_checkbutton.pkl", "wb") as f:
        pickle.dump(var.get(), f)

# Função para carregar o estado do Checkbutton de um arquivo
def carregar_estado():
    try:
        with open("estado_checkbutton.pkl", "rb") as f:
            estado = pickle.load(f)
            var.set(estado)
    except FileNotFoundError:
        var.set(False)  # Define o estado padrão como desativado caso o arquivo não exista

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

# Carregando o estado do Checkbutton
carregar_estado()

# Criando o Checkbutton e associando-o à variável de controle
checkbutton = tk.Checkbutton(root, text="Checkbutton", variable=var)
checkbutton.pack()

# Botão para verificar o estado do Checkbutton
btn_verificar = tk.Button(root, text="Verificar Estado", command=verificar_estado)
btn_verificar.pack()

# Botão para salvar o estado do Checkbutton
btn_salvar = tk.Button(root, text="Salvar Estado", command=salvar_estado)
btn_salvar.pack()

# Exibindo a janela
root.mainloop()
