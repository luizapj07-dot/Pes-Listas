temp = float(input("Diga a temperatura!"))

if temp < 10:
    print("“Está muito frio! Use roupas quentes.")
elif temp <= 20: 
    print("Frio. Vista-se bem!")
elif temp <= 25:
    print("Temperatura agradável.")
elif temp <= 30:
    print("Está ficando quente!")
else:
    print("Está muito quente! Fique hidratado.")