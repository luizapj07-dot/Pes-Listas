depositado = float(input("Quanto você investirá por mês? "))
meses = int(input("Quantos meses? "))

contador = 1
total = 0

while contador <= meses:
    total = total * 1.005
    total = total + depositado

    print(f"Mês {contador}: R$ {total:.2f}")

    contador += 1

print(f"\nValor final: R$ {total:.2f}")
