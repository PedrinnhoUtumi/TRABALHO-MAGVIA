import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Exemplo de Entry com Limite de Caracteres")

        # Variável de controle para o Entry
        self.entry_text = tk.StringVar()

        # Configuração do Entry com validação
        self.entry = tk.Entry(root, textvariable=self.entry_text, validate="key")
        self.entry.pack(padx=20, pady=20)

        # Limita o tamanho máximo de caracteres permitidos
        self.entry['validatecommand'] = (self.root.register(self.validate_entry), '%P')

    def validate_entry(self, new_text):
        # Função de validação que verifica se o texto excede o limite
        return len(new_text) <= 10  # Limite de 10 caracteres

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
