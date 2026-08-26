lista = []

while len(lista) <= 15:
    num = int(input("Digite um numero: "))
    if num > 75 or num < 1:
        print("Não, outro né")
    else:
        lista.append(num)
        print("Cadastrado com sucesso!")

lista.sort()

print(lista)
