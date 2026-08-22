
def tempo_total(a, b):
    return a*60 + b

horas = int(input("Quantas horas tu jogou?"))
minutos = int(input("Quantos minutos tu jogou?"))

resultado = tempo_total(horas, minutos)
print(resultado, "minutos jogados")