dinheiro = 1000
meses = int(input("Quantos mêses devendo?"))
contagem = 0

while contagem < meses:
    dinheiro = dinheiro + dinheiro/100*(15.3)
    contagem += 1

print(dinheiro)