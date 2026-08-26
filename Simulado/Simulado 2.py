lista = []

while len(lista) <= 15:
    num = int(input("Digite um numero: "))
    if (num < 1 or num > 75) and num not in lista:
        print("Outro né")
    else:
        print("Número registrado com sucesso!! ")
        lista.append(num)

lista.sort() #Vai ordenar do menor pro maior
print(lista)
