nump = int(input("quantas palavras serão cadastradas?"))

dicionario = {

}

for i in range(nump):
    palavra = str(input("Digite uma palavra: "))
    significado = str(input("Digite o significado dela: "))
    dicionario[palavra] = significado

print(dicionario)