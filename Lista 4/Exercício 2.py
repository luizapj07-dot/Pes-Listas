Quantidade = int(input("Digite quantas notas são:"))
Notas = []
contador = 0
for i in range(Quantidade):
    nota = float(input("Digite a nota"))
    Notas.append(nota)


while contador < Quantidade:
    print(f"A nota é: {Notas[contador]}")
    contador += 1

for nota in Notas:
    print(f"A nota é: {nota}")
