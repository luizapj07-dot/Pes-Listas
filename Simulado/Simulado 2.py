lista = []

while len(lista) < 15:
    num = int(input("Digite um número: "))
    if 1 <= num <= 75 and not num in lista:
        lista.append(num)
        print("Número adicionado com sucesso!")
    else:
        print("No!")        

lista.sort()
print(lista)