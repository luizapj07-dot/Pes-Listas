quantidade = int(input("quantas notas são?"))
contador = 0
notas = 0 


while contador <= quantidade: 
    nota = float(input("qual foi as notas?"))
    notas = notas + nota

media = notas / quantidade
print(media)