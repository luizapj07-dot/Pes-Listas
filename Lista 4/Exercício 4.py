cidades = []

Quant = int(input("Digite a quantidade de cidades a serem cadastradas:"))
contador = 0
while contador < Quant:
    cidade = input("Digite o nome da cidade:")
    cidades.append(cidade)
    contador += 1

for cidade in cidades:
    print(cidade)
    
remover = input("Digite a cidade a ser removida:")

indice = cidades.index(remover)
cidades.pop(indice)

for cidade in cidades:
    print(cidade)