contador = 0
number = 1
soma = 0
while number > 0:
    number = int(input("Digite seu número:"))
    soma = soma + number
    contador += 1

media = soma/contador
print(media)

