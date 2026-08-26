a = int(input("Qual o first? "))
b = int(input("Qual o second? "))

opcao = -1
while opcao != 0:
    print("""
    1 -- Adição
    2 -- Subtração
    3 -- Multipĺicação
    4 -- Divisão
    0 -- Sair
""")
    opcao = int(input("Digite a opcao desejada: "))
    if opcao == 1:
        res = a+b
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
    