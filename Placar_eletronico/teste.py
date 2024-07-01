import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('600x400')

# Criando o cabeçalho da tabela
columns = ('Nome', 'Idade', 'Cidade')
treeview = ttk.Treeview(root, columns=columns, show='headings')
treeview.pack(fill='both', expand=True, padx=20, pady=20)

# Definindo os nomes das colunas
for col in columns:
    treeview.heading(col, text=col)

# Inserindo dados na tabela
data = [
    ('João', 30, 'São Paulo'),
    ('Maria', 25, 'Rio de Janeiro'),
    ('Carlos', 40, 'Belo Horizonte'),
    ('Ana', 35, 'Brasília'),
]

for item in data:
    treeview.insert('', 'end', values=item)

# Criando uma área de texto (opcional)
text_area = tk.Text(root, wrap='none', height=10)
text_area.pack(fill='both', expand=True, padx=20, pady=20)

# Adicionando texto à área de texto (opcional)
example_text = """\
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Praesent in felis lobortis, aliquet diam eget, suscipit dui.

Nulla facilisi. Donec elementum, tortor at congue posuere, ipsum justo volutpat elit, ac suscipit quam orci ac risus.
"""
text_area.insert('1.0', example_text)

root.mainloop()
