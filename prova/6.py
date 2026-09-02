def distancia_total(k, m):
    return ((k*1000) + m)

km = int(input("quantos kms: "))
m = int(input("quantos metros: "))

print(f"{distancia_total(km, m)} metros")
