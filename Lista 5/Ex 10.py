import random

x = -1

while x != 0:

    def embaralhar(palavra):

        lista = list(palavra) #(list) transforma a string em lista
        random.shuffle(lista) #(shuffle) embaralha os caracteres
        return "".join(lista) #(join) junta os caracteres novamente

    palavra = str(input("Digite uma palavra: "))

    print(embaralhar(palavra))