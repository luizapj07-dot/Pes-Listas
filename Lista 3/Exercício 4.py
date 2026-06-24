lista = []

for i in range(15):
    lista.append("0")

opcao = 4
contadorc = 0
contadore = 0


while opcao != "0":
    print("""
    1 – Cadastrar
    2 - Excluir
    3 - Listar
    0 - Sair""")

    opcao = input("Digite a opcao que quer?")

    if opcao == "1":
        while contadorc < 15:
            if lista[contadorc] == "0":
                novo = input("Digite a placa:")
                lista[contadorc] = novo
                contadorc += 1
                print("sucesso")
                break
            else:
                contadorc += 1
                print("erro")

    if opcao == "2":
        contadore = 0
        excluir = input("Qual placa você quer excluir?")

        while contadore < 15:
            if lista[contadore] == excluir:
                lista[contadore] = "0"
                print("placa excluída!!")
                break
            else:
                contadore += 1
                print("Não encontrada")

    if opcao == "3":
        for placa in lista:
            print(placa)

    if opcao == "0":
        break
