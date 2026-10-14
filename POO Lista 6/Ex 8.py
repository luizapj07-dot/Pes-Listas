#Estudante
class Estudante:
    def __init__(self, matricula, nome, sobrenome, idade):
        self.matricula = matricula
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


    def cadastroest(self):
        matriculax = int(input("Digite a matricula da pessoa: "))
        nomex = input("Digite o nome da pessoa: ")
        sobrenomex = input("Digite o sobrenome da pessoa: ")
        idadex = int(input("Digite o idade da pessoa: "))

        return  Estudante(matriculax, nomex, sobrenomex, idadex)
    
Estudantes = []

#Professor
class Professor:
    def __init__(self, matriculap, nomep, sobrenomep, idadep, especializacaop):
        self.matriculap = matriculap
        self.nomep = nomep
        self.sobrenomep = sobrenomep
        self.idadep = idadep
        self.especializacaop = especializacaop


    def cadastroprof(self):
        matriculaxprof = int(input("Digite a matricula da pessoa: "))
        nomexprof = input("Digite o nome da pessoa: ")
        sobrenomexprof = input("Digite o sobrenome da pessoa: ")
        idadexprof = int(input("Digite o idade da pessoa: "))
        especializacaoxprof = input("Digite a especialização da pessoa: ")

        return  Professor(matriculaxprof, nomexprof, sobrenomexprof, idadexprof, especializacaoxprof)
    
Professores = []

r = -1
while r != 0:
    print("""Sistema de Cadastro
          --------------------
            1 – Cadastrar estudante
            2 – Cadastrar professor
            3 – Listar estudantes
            4 – Listar professores
            5 – Alterar estudante pela matrícula
            6 – Alterar estudante pelo nome
            7 – Alterar professor pela matrícula
            8 – Alterar professor pelo nome
            9 – Excluir estudante pela matrícula
            10 – Excluir professor pela matrícula
            0 – Sair
Opção: """)
    r = int(input("Digite a opcao desejada: "))

    if r == 1:
        Estudantex = Estudante(0, "", "", 0)
        Estudantex = Estudantex.cadastroest()
        Estudantes.append(Estudantex)
        print("Exito!")

    elif r == 2:
        Professorx = Professor(0, "", "", 0, "")
        Professorx = Professorx.cadastroprof()
        Professores.append(Professorx)
        print("Exito!")

    elif r == 3:
        for estudante in Estudantes:
            print(estudante.matricula, estudante.nome, estudante.sobrenome, estudante.idade)
    elif r == 4:
        for professor in Professores:
            print(professor.matriculap, professor.nomep, professor.sobrenomep, professor.idadep, professor.especializacaop)
    elif r == 5:
        chocolex = int(input("Digite a matrícula de quem você quer alterar!")) #Matrícula alterar
        
        encontrado = False

        for estudante in Estudantes:
            if estudante.matricula == chocolex:
                print("Estudante existe! Digite os novos dados: ")

                estudante.nome = input("Digite o nome: ")
                estudante.sobrenome = input("Digite o sobrenome: ")
                estudante.idade = int(input("Digite a idade: "))

                encontrado = True
                print("Alteroso")
                break
        if not encontrado:
            print("Não existex")
    elif r == 6:
        brr = input("Digite o nome de quem você quer alterar!") #Nome alterar
        
        encontrado = False

        for estudante in Estudantes:
            if estudante.nome == brr:
                print("Estudante existe! Digite os novos dados: ")

                estudante.nome = input("Digite o nome: ")
                estudante.sobrenome = input("Digite o sobrenome: ")
                estudante.idade = int(input("Digite a idade: "))

                encontrado = True
                print("Alteroso")
                break
        if not encontrado:
            print("Não existex")
    elif r == 7: 
        elclassico = int(input("Digite a matrícula do professor que deseja alterar: "))

        encontrado = False

        for professor in Professores:
            if professor.matriculap == elclassico:
                print("Professor encontrado! Digite os novos dados:")

                professor.nomep = input("Digite o nome: ")
                professor.sobrenomep = input("Digite o sobrenome: ")
                professor.idadep = int(input("Digite a idade: "))
                professor.especializacaop = input("Digite a especialização: ")

                encontrado = True
                print("Professor alterado com sucesso!")
                break

        if not encontrado:
            print("Professor não encontrado!")
    elif r == 8:
        dazu = input("Digite o nome do professor que deseja alterar: ")

        encontrado = False

        for professor in Professores:
            if professor.nomep == dazu:
                print("Professor encontrado! Digite os novos dados:")

                professor.nomep = input("Digite o nome: ")
                professor.sobrenomep = input("Digite o sobrenome: ")
                professor.idadep = int(input("Digite a idade: "))
                professor.especializacaop = input("Digite a especialização: ")

                encontrado = True
                print("Professor alterado com sucesso!")
                break

        if not encontrado:
            print("Professor não encontrado!")

    elif r == 9:
        paper = int(input("Quem vc quer excluir? (pela matricula!)"))

        encontrado = False
        for estudante in Estudantes:
            if estudante.matricula == paper:
                Estudantes.remove(estudante)
                encontrado = True 
                print("Exito!")
                break
        if not encontrado:
            print("Estudante não encontrado!")
            
    elif r == 10:
        kane = int(input("Quem vc quer excluir? (pela matricula!)"))

        encontrado = False
        for professor in Professores:
            if professor.matriculap == kane:
                Professores.remove(professor)
                encontrado = True 
                print("Exito!")
                break
        if not encontrado:
            print("Professor não encontrado!")
    elif r == 0:
        print("Saindo do Sistema!")
    else:
        print("Opção Inválida!!")