import tkinter as tk

def obter_texto():
    texto = texto_box.get("1.0", tk.END)  # Obtém todo o texto do widget Text
    print(texto)

root = tk.Tk()
root.title("Exemplo de Texto")

# Cria um widget Text com barras de rolagem vertical e horizontal
texto_box = tk.Text(root, wrap="word")
texto_box.pack(expand=True, fill="both")

# Adiciona um botão para obter o texto do widget Text
botao_obter = tk.Button(root, text="Obter Texto", command=obter_texto)
botao_obter.pack(pady=5)

root.mainloop()
