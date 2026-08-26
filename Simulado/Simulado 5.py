a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

opcao = -1

while opcao != 0:
    print("""
    1 -- Adição
    2 -- Subtração
    3 -- Multiplicação
    4 -- Divisão
    0 -- Sair""")

    opcao = int(input("Qual a opção desejada? "))

    if opcao == 1:
        res = a + b
    elif opcao == 2:
        res = a-b
    elif opcao == 3:
        res = a*b
    elif opcao == 4:
        if b == 0:
            res = "Erro!"
        else:
            res = a/b

    else:
        break

    print(res)

