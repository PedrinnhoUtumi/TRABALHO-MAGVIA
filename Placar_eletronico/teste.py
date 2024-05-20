import tkinter as tk

class Table(tk.Frame):
    def __init__(self, parent, rows=15, columns=7):
        super().__init__(parent)
        
        self.rows = rows
        self.columns = columns
        
        self.entries = [[None]*columns for _ in range(rows)]
        
        # Criando as entradas e organizando-as em uma grade
        for i in range(rows):
            for j in range(columns):
                entry = tk.Entry(self, width=10)
                entry.grid(row=i, column=j, sticky="nsew")
                self.entries[i][j] = entry
        
        # Configurando o redimensionamento da grade
        for i in range(rows):
            self.grid_rowconfigure(i, weight=1)
        for j in range(columns):
            self.grid_columnconfigure(j, weight=1)

def main():
    root = tk.Tk()
    root.title("Tabela com Entries no Tkinter")
    
    table = Table(root)
    table.pack(expand=True, fill="both")
    
    root.mainloop()

if __name__ == "__main__":
    main()
