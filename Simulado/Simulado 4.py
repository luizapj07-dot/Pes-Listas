dicionario = {
    "palavra": "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma situação difícil, ou usar de meios extremos e exagerados"
}

for i in range(4):
    nova = str(input("Digite uma palavra: "))
    significado = str(input("Digite o significado dela: "))
    dicionario[nova] = significado

consulta = input("Digite uma palavra a consultar: " )

if consulta in dicionario:
    print("Significado", dicionario[consulta])
else:
    print("Palavra não encontrada!! ")
    

