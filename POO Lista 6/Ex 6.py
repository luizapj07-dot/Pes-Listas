class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def cadastro(self):
        nomex = input("Digite o nome da pessoa: ")
        idadex = int(input("Digite o idadex da pessoa: "))
        alturax = float(input("Digite o alturax da pessoa: "))
        pesox = float(input("Digite o peso da pessoa: "))

        return  Pessoa(nomex, idadex, alturax, pesox)
Pessoas = []
r = -1
while r != 0:
    print("""Cadastro de Pessoas
        ----------------------  
          1 - Cadastrar
          2 - Listar
          0 Sair
          Opcão:""")
        
    r = int(input("Digite a opção desejada: "))
    if r == 1:
        Pessoanew = Pessoa("", 0, 0, 0)
        Pessoanew = Pessoanew.cadastro()
        Pessoas.append(Pessoanew)

    elif r == 2:
        for people in Pessoas:
            print(people.nome, people.idade, people.altura, people.peso)

    elif r == 0:
        print("Saindo...")

    else:
        print("Opção Invalida!!!")

#FULL CHAT