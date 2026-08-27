concen_inicial = float(input("Qual a concentração inicial? "))
concen_final = float(input("Qual a concentração final? "))
volume_final = float(input("Qual o volume final? "))

volume_inicial = (concen_final*volume_final)/concen_inicial

print(f"{volume_inicial} mls")