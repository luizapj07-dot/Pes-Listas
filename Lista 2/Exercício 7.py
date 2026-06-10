quantidade = int(input("quantas notas são?"))
contador = 0
notas = 0 


while contador < quantidade: 
    nota = int(input("Me diga a nota:"))
    notas = notas + nota
    contador += 1

media = notas / quantidade
print("A média é ", media)

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado") 