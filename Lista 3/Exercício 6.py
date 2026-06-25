Codigos = []
Pessoas = []
Idades = []
Alturas = []
Pesos = []


opcao = 7

while opcao != 0:
    print("""
        1 – Cadastrar
        2 - Excluir pelo codigo
        3 - Excluir pelo nome
        4 - Alterar
        5 - Pesquisar
        6 - Listar
        0 - Sair""")
    
    opcao = int(input("Digite a opcao desejada!"))

    if opcao == 1:
        Codigo = input("Digite o codigo da pessoa:")
        pessoa = input("Digite o nome da pessoa:")
        idade = input("Digite a idade da pessoa:")
        altura = input("Digite a altura da pessoa:")
        peso = input("Digite o peso da pessoa:")

        Codigos.append(Codigo)
        Pessoas.append(pessoa)
        Idades.append(idade)
        Alturas.append(altura)
        Pesos.append(peso)

    if opcao == 2:
        Codigoe = input("Quem você quer excluir?")
        if Codigoe in Codigos:
            indice = Codigos.index(Codigoe)

            Codigos.pop(indice)
            Pessoas.pop(indice)
            Idades.pop(indice)
            Alturas.pop(indice)
            Pesos.pop(indice)
        else:
            print("Essa pessoa não existe na lista!!")



    if opcao == 3:
        excluir = input("Quem você quer excluir?")
        if excluir in Pessoas:
            indice = Pessoas.index(excluir)

            Pessoas.pop(indice)
            Idades.pop(indice)
            Alturas.pop(indice)
            Pesos.pop(indice)
        else:
            print("Essa pessoa não existe na lista!!")

    if opcao == 4:
        Alterar = input("Quem você quer alterar?")
        if Alterar in Pessoas:
            indice = Pessoas.index(Alterar)

            idade = input("Digite a idade da pessoa:")
            altura = input("Digite a altura da pessoa:")
            peso = input("Digite o peso da pessoa:")

            Idades[indice] = idade
            Alturas[indice] = altura
            Pesos[indice] = peso

        else:
            print("Está pessoa não está na lista")

    if opcao == 5:
        Pesquisa = input("Digite o nome da pesquisa a ser pesquisada:")
        if Pesquisa in Pessoas:
            indice = Pessoas.index(Pesquisa)

            print(
                Codigos[indice],
                Pessoas[indice],
                Idades[indice],
                Alturas[indice],
                Pesos[indice]
            )

    if opcao == 6:
        for i in range(len(Pessoas)):
            print(
                Codigos[i],
                Pessoas[i],
                Idades[i],
                Alturas[i],
                Pesos[i]
            )
    if opcao == 0:
        break



        

    