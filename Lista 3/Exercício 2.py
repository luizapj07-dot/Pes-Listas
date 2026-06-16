notas = []
media = 0

for i in range(4):
    nota = int(input(f"Digite a nota {i+1}:"))
    notas.append(nota)

for nota in notas:
    media = media + nota

media = media/4

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")