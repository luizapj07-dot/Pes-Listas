idades = []

for i in range(6):
    idade = int(input(f"Digite a idade {i+1}:"))
    idades.append(idade)

for idade in idades:
    if idade >= 16:
        print(idade)


