import tkinter as tk
from tkinter import ttk

class TabelaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Exemplo de Tabela Editável")

        # Cria um Treeview para exibir a tabela
        self.tree = ttk.Treeview(root, columns=("Nome", "Posição", "Número"), show="headings")

        # Define os cabeçalhos de coluna como imutáveis
        self.tree.heading("Nome", text="Nome", anchor=tk.CENTER)
        self.tree.heading("Posição", text="Posição", anchor=tk.CENTER)
        self.tree.heading("Número", text="Número", anchor=tk.CENTER)

        # Ajusta as colunas para que se ajustem ao conteúdo
        for col in ("Nome", "Posição", "Número"):
            self.tree.column(col, width=100, anchor=tk.CENTER)

        # Coloca o Treeview na janela
        self.tree.pack(pady=20)

        # Botões para adicionar e editar linhas
        self.btn_adicionar = tk.Button(root, text="Adicionar Nova Linha", command=self.adicionar_linha)
        self.btn_adicionar.pack(pady=10)

        self.btn_editar = tk.Button(root, text="Editar Selecionado", command=self.editar_linha)
        self.btn_editar.pack(pady=5)

    def adicionar_linha(self):
        # Função para adicionar uma nova linha com dados fictícios
        dados_nova_linha = ("Novo Nome", "Nova Posição", "456")
        self.tree.insert("", "end", values=dados_nova_linha)

    def editar_linha(self):
        # Função para editar a linha selecionada na tabela
        selected_item = self.tree.selection()
        if selected_item:
            # Obtém os valores atuais da linha selecionada
            values_atuais = self.tree.item(selected_item)["values"]

            # Cria uma janela de diálogo para edição
            self.dialogo_edicao = tk.Toplevel(self.root)
            self.dialogo_edicao.title("Editar Linha")

            # Labels e campos de entrada para editar os valores
            tk.Label(self.dialogo_edicao, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
            tk.Label(self.dialogo_edicao, text="Posição:").grid(row=1, column=0, padx=5, pady=5)
            tk.Label(self.dialogo_edicao, text="Número:").grid(row=2, column=0, padx=5, pady=5)

            self.nome_entry = tk.Entry(self.dialogo_edicao)
            self.nome_entry.grid(row=0, column=1, padx=5, pady=5)
            self.nome_entry.insert(0, values_atuais[0])

            self.posicao_entry = tk.Entry(self.dialogo_edicao)
            self.posicao_entry.grid(row=1, column=1, padx=5, pady=5)
            self.posicao_entry.insert(0, values_atuais[1])

            self.numero_entry = tk.Entry(self.dialogo_edicao)
            self.numero_entry.grid(row=2, column=1, padx=5, pady=5)
            self.numero_entry.insert(0, values_atuais[2])

            # Botão para confirmar a edição
            tk.Button(self.dialogo_edicao, text="Salvar", command=self.salvar_edicao).grid(row=3, columnspan=2, padx=5, pady=10)

    def salvar_edicao(self):
        # Função para salvar as alterações feitas na linha editada
        selected_item = self.tree.selection()
        if selected_item:
            # Atualiza os valores na tabela com os novos valores inseridos
            novos_valores = (
                self.nome_entry.get(),
                self.posicao_entry.get(),
                self.numero_entry.get()
            )
            self.tree.item(selected_item, values=novos_valores)
            self.dialogo_edicao.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TabelaApp(root)
    root.mainloop()
