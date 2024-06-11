import tkinter as tk

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Teste de focus_get")

        self.label = tk.Label(self.root, text="Pressione a tecla de espaço para ver o widget com o foco.")
        self.label.pack(pady=10)

        self.root.bind("<space>", self.show_focused_widget)

    def show_focused_widget(self, event=None):
        focused_widget = self.root.focus_get()
        if focused_widget:
            print("Widget com foco:", focused_widget)
        else:
            print("Nenhum widget com foco.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Application()
    app.run()
