
codigo = 1


while codigo > 0:
    codigo = int(input("Digite o código do produto!"))
    Quantidade = int(input("Quantos você quer?"))

    if codigo == 1:
        preço = Quantidade * 6
        print(f"Você comprou {Quantidade} Sucos, custou {preço} reais ")
    
    elif codigo == 2:
        preço = Quantidade * 3
        print(f"Você comprou {Quantidade} Pão de queijos, custou {preço} reais")

    elif codigo == 3:

        preço = Quantidade * 7
        print(f"Você comprou {Quantidade} Pastel, custou {preço} reais")

    elif codigo == 4:
        preço = Quantidade * 9
        print(f"Você comprou {Quantidade} Salada de Frutas, custou {preço} reais ")

    elif codigo == 5:
        preço = Quantidade * 3.5
        print(f"Você comprou {Quantidade} Café com Leite, custou {preço} reais ")

    elif codigo == 6:
        preço = Quantidade * 4.5
        print(f"Você comprou {Quantidade} Cappuccino, custou {preço} reais")

    elif codigo == 7:
        preço = Quantidade * 6.5
        print(f"Você comprou {Quantidade} Iogurte, custou {preço} reais")

    elif codigo == 8:
        preço = Quantidade * 2.5
        print(f"Você comprou {Quantidade} Água, custou {preço} reais")

    else:
        print("codigo inválido")


    
