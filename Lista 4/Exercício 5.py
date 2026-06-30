lista = []

opcao = 4

while opcao != 0:
    print("""Amigos Próximos
            ---------------
            1 - Cadastrar
            2 - Excluir
            3 - Listar
            0 - Sair""")
    opcao = int(input("Digite a opcao desejada: "))

    if opcao == 1:
        Nome = input("Digite o nome do amigo novo: ")
        lista.append(Nome)
    if opcao == 2:
        Excluir = input("Digite o nome do amigo a ser removido: ")
        indice = lista.index(Excluir)
        lista.pop(indice)
    if opcao == 3:
        if len(lista) == 0:
            print("A lista está vazia!")
        else:
            for nome in lista:
                print(nome)
    if opcao == 0:
        break
