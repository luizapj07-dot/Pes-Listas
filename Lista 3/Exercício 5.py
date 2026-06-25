Pessoas = []
Idades = []
Alturas = []
Pesos = []

opcao = 5

while opcao != 0:
    print("""
        1 – Cadastrar
        2 - Excluir
        3 - Alterar
        4 - Listar
        0 - Sair""")
    
    opcao = int(input("Digite a opcao desejada!"))

    if opcao == 1:
        pessoa = input("Digite o nome da pessoa:")
        idade = input("Digite a idade da pessoa:")
        altura = input("Digite a altura da pessoa:")
        peso = input("Digite o peso da pessoa:")

        Pessoas.append(pessoa)
        Idades.append(idade)
        Alturas.append(altura)
        Pesos.append(peso)

    if opcao == 2:
        excluir = input("Quem você quer excluir?")
        if excluir in Pessoas:
            indice = Pessoas.index(excluir)

            Pessoas.pop(indice)
            Idades.pop(indice)
            Alturas.pop(indice)
            Pesos.pop(indice)
        else:
            print("Essa pessoa não existe na lista!!")

    if opcao == 3:
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

    if opcao == 4:
        for i in range(len(Pessoas)):
            print(
                Pessoas[i],
                Idades[i],
                Alturas[i],
                Pesos[i]
            )
    if opcao == 0:
        break



        

    