from tkinter import *
from tkcalendar import DateEntry

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Seleção de Data")
        self.root.geometry("300x200")

        self.criaFrame()

    def criaFrame(self):
        frame = Frame(self.root)
        frame.pack(pady=20)

        label = Label(frame, text="Escolha uma data:")
        label.pack(pady=5)

        # Adiciona o DateEntry
        self.date_entry = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.pack(pady=5)

        button = Button(frame, text="Confirmar", command=self.mostrar_data)
        button.pack(pady=10)

    def mostrar_data(self):
        data_selecionada = self.date_entry.get()
        print(f"Data selecionada: {data_selecionada}")

if __name__ == "__main__":
    root = Tk()
    app = Interface(root)
    root.mainloop()
