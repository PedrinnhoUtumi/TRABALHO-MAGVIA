import tkinter as tk
from tkinter import Tk

def redesenhar(event):
    root.update()
    
if __name__ == "__main__":
    root = Tk()
    root.title("Redesenho Automático da Página")

    # Aqui você pode adicionar os widgets da sua interface gráfica
    label = tk.Label(root, text="Clique em qualquer lugar para redesenhar a página", font=("Helvetica", 18))
    label.pack(padx=20, pady=20)

    # Vincular todos os eventos de clique para chamar a função redesenhar
    root.bind_all("<Button-1>", redesenhar)

    root.mainloop()
