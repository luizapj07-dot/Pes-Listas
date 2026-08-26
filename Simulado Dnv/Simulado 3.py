preco = int(input("Qual é o preço"))
quantidade = int(input("Quantos são? "))

if preco >= 100:
    res = (quantidade*preco)*0.9
else:
    res = quantidade*preco

print(f"Custou {res} reais")