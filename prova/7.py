lista = []

i = -1
while i != 0:
    print("""
    1 - Cadastrar
    2 - Excluir
    3 - Listar
    0 - Sair
          """)
    
    i = int(input("Digite um numero acima: "))

    if i == 1:
        placa = str(input("Digite o nome da placa a cadastrar: "))
        lista.append(placa)
    elif i == 2:
        lixo = str(input("Digite o nome da placa a excluir: "))
        if lixo in lista:
            for j in range(len(lista)):
                if lista[j] == lixo:
                    indice = j
            lista.pop(j)
            print("Sucesso!")
        else:
            print("Falha!")
    elif i == 3:
        print(lista)
    else:
        break
    