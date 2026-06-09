idade = int(input("Ponha a idade: "))

if idade >= 18:
    print("Você pode assistir a filmes com classificação até 18 anos.")
elif idade >= 16:
    print("Você pode assistir a filmes com classificação até 16 anos.")
elif idade >= 14:
    print("Você pode assistir a filmes com classificação até 14 anos.")
elif idade >= 12:
    print("Você pode assistir a filmes com classificação até 12 anos.")
elif idade >= 10:
    print("Você pode assistir a filmes com classificação até 10 anos.")
else:
    print("Você pode assistir apenas a filmes com classificação Livre.")