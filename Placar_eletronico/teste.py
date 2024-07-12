from tkinter import Tk, ttk, Frame, Entry

class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title("Exemplo Tkinter com Notebook")

        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(padx=10, pady=10, fill='both', expand=True)

        self.tab1 = Frame(self.notebook)
        self.tab2 = Frame(self.notebook)

        self.notebook.add(self.tab1, text='Aba 1')
        self.notebook.add(self.tab2, text='Aba 2')

        self.frames()

    def frames(self):
        self.entry_tab1 = Entry(self.tab1)
        self.entry_tab1.pack(padx=20, pady=20)

        self.entry_tab2 = Entry(self.tab2)
        self.entry_tab2.pack(padx=20, pady=20)

if __name__ == "__main__":
    root = Tk()
    app = Interface(root)
    root.mainloop()
