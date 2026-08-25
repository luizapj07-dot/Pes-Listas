preco = int(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))

if preco >= 100:
    resultado = (preco * quantidade)*0.9
else:
    resultado = preco * quantidade

print(f"O preço final foi de {resultado} reais")