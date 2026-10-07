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
          3 - Excluir Pessoa
          4 - Atualizar idade, altura e peso
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

    elif r == 3:
        exit = input("Digite quem você quer tirar: ")

        for pessoa in Pessoas:
            if pessoa.nome == exit:
                Pessoas.remove(pessoa)
                break

    elif r == 4:
        atualizenzo = input("Digite o nome da pessoa que você quer atualizar: ")
        for pessoa in Pessoas:
            if pessoa.nome == atualizenzo:
                a = input("Digite a nova idade: ")
                b = input("Digite a nova altura: ")
                c = input("Digite o novo peso: ")
                pessoa.idade = a
                pessoa.altura = b
                pessoa.peso = c
    elif r == 0:
        print("Saindo...")

    else:
        print("Opção Invalida!!!")
