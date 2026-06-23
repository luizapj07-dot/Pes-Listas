listas = []
for i in range(10): #definindo como -1
    listas.append(-1)

contador = 0
    
opcao = 3
while opcao != "0": # inicio
    print("""
    Menu
    ----
    1 – Cadastrar
    2 – Listar todos
    0 – Sair
    """)
    
    opcao = input("Digite sua opcao:")

    if opcao == "1":
        print("contador => ", contador)

        while contador < 10:
            if listas[contador] == -1:
                sabor = int(input("Digite o novo valor:"))

                if sabor == "-1":
                    break

                else:
                    listas[contador] = sabor
                    contador += 1
                    break
            else:
                contador += 1

    if opcao == "2":
        for valor in listas:
            print(valor)
    
    if opcao == "0":
        break