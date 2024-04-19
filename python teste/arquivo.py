import os

lista = [{'nome': 'Cumbuca', 'categoria': 'Italiana', 'ativo': True}, 
         {'nome': 'Velhos Tempos', 'categoria': 'Pizza', 'ativo': False},
         {'nome': 'Cantina Di Colli', 'categoria': 'Italiana', 'ativo': True}]

def nome():
    print("""

█▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀
█▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄
""")

def opcoes():
    print ("""
       1. Cadastrar Restaurante 
       2. Listar Restaurante
       3. Ativar/desativar Restaurante
       4. Sair
""")
    
def voltar():
    input("\nDigite uma tecla para voltar: ")
    main()
    
def exibir_subtitulo(txt = ''):
    os.system("cls")
    linha = '*' * (len(txt))
    print(linha)
    print(txt)
    print(linha)
    print()
    
def cadastro():
    exibir_subtitulo("Cadastro")
    nome_restaurante = input("digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_restaurante}: ")
    dados = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    lista.append(dados)
    print(f"Restaurante {nome_restaurante} foi cadastrado com sucesso!")
    voltar()

def listar():
    exibir_subtitulo(f'{"Nome do Restaurante".ljust(20)}  | {"Categoria".ljust(20)} | Atividade')
    for lis in lista:
        nome = lis['nome']
        categoria = lis['categoria']
        ativo = "Ativado" if lis['ativo'] else "Desativado"
        print(f'{nome.ljust(20)}  | {categoria.ljust(20)} | {ativo}')
    voltar()
    
def ativar_desativar():
    exibir_subtitulo("Alterando estado")
    nome = input("Nome do restaurante que será alterado: ")
    encontrado = False
    for lis in lista:
        if nome == lis["nome"]:
            encontrado = True
            lis["ativo"] = not lis["ativo"]
            print(f"Restaurante {nome} foi ativado" if lis['ativo'] else f"Restaurante {nome} desativado com sucesso")
    if not encontrado:
        print("Restaurante não foi encontrado")
    voltar()
    2
def finalizar():
    exibir_subtitulo("4. sair\n")
        
def opcao_invalida():
    print("Opção inválida")
    voltar()

def opcao_escolha():
    try:
        a = int(input("Escolha uma opção: "))
        if a == 1:
            cadastro()
        elif a == 2:
            listar()
        elif a == 3:
            ativar_desativar()
        elif a == 4:
            finalizar()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    exibir_subtitulo()
    nome()
    opcoes()
    opcao_escolha()
    
if __name__ == "__main__":
    main()