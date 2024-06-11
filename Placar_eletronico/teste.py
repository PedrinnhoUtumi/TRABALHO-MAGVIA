import tkinter as tk

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Teste de Tecla de Espaço")

        self.label = tk.Label(self.root, text="Pressione a tecla de espaço para começar o cronômetro.")
        self.label.pack(pady=10)

        self.root.bind("<space>", self.start_timer)

    def start_timer(self, event):
        self.label.config(text="Cronômetro iniciado!")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Application()
    app.run()
