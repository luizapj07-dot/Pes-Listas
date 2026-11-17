
class Cliente:
    def __init__(self, Nome_Cliente, Endereco_Cliente, Id_Cliente, Senha_Cliente):
        self.Nome_Cliente = Nome_Cliente
        self.Endereco_Cliente = Endereco_Cliente
        self.Id_Cliente = Id_Cliente
        self.senha = Senha_Cliente

    # Relacionamento: Cliente procura produtos
    def procurar_produto(self, Id_Produto, produtos):
        resultados = []

        for produto in produtos:
            if produto.Id_Produto == Id_Produto:
                resultados.append(produto)

        # Organiza as ofertas pelo menor preço
        resultados.sort(key=lambda produto: produto.Preco_Produto)

        return resultados


class Vendedor:
    def __init__(self, Nome_Vendedor, Telefone_Vendedor, Endereco_Vendedor, Id_Vendedor):
        self.Nome_Vendedor = Nome_Vendedor
        self.Telefone_Vendedor = Telefone_Vendedor
        self.Endereco_Vendedor = Endereco_Vendedor
        self.Id_Vendedor = Id_Vendedor

        # Cada vendedor possui seus produtos cadastrados
        self.produtos = []

    # Relacionamento: Vendedor cadastra produtos
    def cadastrar_produto(self, produto, produtos):
        self.produtos.append(produto)
        produtos.append(produto)


class Produto:
    def __init__(self, Nome_Produto, Id_Produto, Preco_Produto, Status_Produto, Link_Produto, vendedor):

        self.Nome_Produto = Nome_Produto
        self.Id_Produto = Id_Produto
        self.Preco_Produto = Preco_Produto
        self.Status_Produto = Status_Produto
        self.Link_Produto = Link_Produto

        # Relacionamento: Produto pertence a um vendedor
        self.vendedor = vendedor


# Listas do sistema
produtos = []
vendedores = []

usuario_log = None
cliente_log = None
vendedor_log = None

escolha = -1


while escolha != 0:

    print("""
    ======== BUSCANET ========

    1 -- Entrar como Cliente
    2 -- Cadastrar Produto
    3 -- Login Vendedor
    4 -- LogOut Cliente
    5 -- LogOut Vendedor
    6 -- Ver os produtos cadastrados
    7 -- Procurar Produto
    0 -- Sair
    """)

    escolha = int(input("Escolha uma opção: "))


    # LOGIN CLIENTE
    if escolha == 1:

        if usuario_log is None:

            nome_usuario = input("Digite seu e-mail: ")

            if "@" in nome_usuario:

                senha_usuario = input("Digite sua senha: ")
                endereco_usuario = input("Digite seu CEP: ")

                if len(endereco_usuario) == 8:

                    Id_usuario = input("Digite seu ID: ")

                    cliente_log = Cliente(
                        nome_usuario,
                        endereco_usuario,
                        Id_usuario,
                        senha_usuario
                    )

                    usuario_log = "cliente"

                    print("Bem-vindo ao BuscaNet!")

                else:
                    print("CEP inválido! Digite um CEP com 8 dígitos.")

            else:
                print("Esse e-mail é inválido!")

        else:
            print("Já existe um usuário logado!")


    # CADASTRAR PRODUTO
    elif escolha == 2:

        if usuario_log == "vendedor":

            nome = input("Digite o nome do produto: ")
            id_produto = input("Digite o ID do produto: ")

            preco = float(input("Digite o preço do produto: "))
            status = input("Digite o status do produto: ")
            link = input("Digite o link de compra: ")

            novo_produto = Produto(
                nome,
                id_produto,
                preco,
                status,
                link,
                vendedor_log
            )

            vendedor_log.cadastrar_produto(novo_produto, produtos)

            print("Produto cadastrado com sucesso!")

        else:
            print("Você precisa estar logado como vendedor!")


    # LOGIN VENDEDOR
    elif escolha == 3:

        if usuario_log is None:

            nome = input("Nome do Vendedor: ")
            telefone = input("Telefone do Vendedor: ")
            endereco = input("Digite seu CEP: ")
            id_vendedor = input("ID Vendedor: ")

            vendedor_log = Vendedor(
                nome,
                telefone,
                endereco,
                id_vendedor
            )

            vendedores.append(vendedor_log)

            usuario_log = "vendedor"

            print("Entrando como vendedor...")

        else:
            print("Já existe um usuário logado!")


    # LOGOUT CLIENTE
    elif escolha == 4:

        if usuario_log == "cliente":

            usuario_log = None
            cliente_log = None

            print("Você saiu da conta de cliente!")

        else:
            print("Nenhum cliente está logado!")


    # LOGOUT VENDEDOR
    elif escolha == 5:

        if usuario_log == "vendedor":

            usuario_log = None
            vendedor_log = None

            print("Você saiu da conta de vendedor!")

        else:
            print("Nenhum vendedor está logado!")


    # VER PRODUTOS CADASTRADOS
    elif escolha == 6:

        if len(produtos) > 0:

            for produto in produtos:

                print("----------------------------")
                print("Nome:", produto.Nome_Produto)
                print("ID:", produto.Id_Produto)
                print("Preço: R$", produto.Preco_Produto)
                print("Status:", produto.Status_Produto)
                print("Link:", produto.Link_Produto)
                print("Vendedor:", produto.vendedor.Nome_Vendedor)
                print("----------------------------")

        else:
            print("Nenhum produto cadastrado!")


    # PROCURAR PRODUTO
    elif escolha == 7:

        if usuario_log == "cliente":

            id_busca = input("Digite o ID do produto que deseja procurar: ")

            resultados = cliente_log.procurar_produto(
                id_busca,
                produtos
            )

            if len(resultados) > 0:

                print("\n===== OFERTAS ENCONTRADAS =====")

                for produto in resultados:

                    print("----------------------------")
                    print("Produto:", produto.Nome_Produto)
                    print("ID:", produto.Id_Produto)
                    print("Preço: R$", produto.Preco_Produto)
                    print("Status:", produto.Status_Produto)
                    print("Vendedor:", produto.vendedor.Nome_Vendedor)
                    print("Link de compra:", produto.Link_Produto)
                    print("----------------------------")

            else:
                print("Nenhuma oferta encontrada para esse produto!")

        else:
            print("Entre como cliente para procurar produtos!")


    elif escolha == 0:
        print("Saindo do BuscaNet... Até mais!")


    else:
        print("Opção inválida!")
