Quantidade = int(input("Digite quantas notas são:"))
Notas = []
contador = 0
for i in range(Quantidade):
    nota = float(input("Digite a nota"))
    Notas.append(nota)

for nota in Notas:
    print(nota)
