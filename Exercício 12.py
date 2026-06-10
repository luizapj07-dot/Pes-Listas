opcao = -1

while opcao != 0:
    print("Menu")
    print("-------")
    print("1 – Adição")
    print("2 – Subtração")
    print("3 – Divisão")
    print("4 – Multiplicação")
    print("0 - Sair")
    opcao = int(input("Digite a opção"))

    if opcao == 0:
        print("Programa Encerrado")
    elif opcao >= 1 and opcao <= 4:
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número:"))
        if opcao == 1:
            res = num1 + num2
            print(res)
        elif opcao == 2:
            res = num1 - num2
            print(res)
        elif opcao == 3:
            if num2 == 0:
                print("Erro: divisão por zero!!!")
            else:
                res = num1 / num2
                print(f"Resultado: {res}")
        elif opcao == 4:
            res = num1 * num2
            print(res)
    else:
        print("Opção Inválida!!!.tente denovo!")



