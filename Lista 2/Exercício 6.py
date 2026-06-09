numero = int(input("Digite seu numero"))
contador = 1
maximo = int(input("Digite o número máximo da tabuada"))

while contador <= maximo:
    produto = numero*contador
    print(f"{numero} x {contador} = {produto}")
    contador = contador + 1
