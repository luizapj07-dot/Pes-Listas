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
        Estudantex = Estudantex(0, "", "", 0)
        Estudantex = Estudantex.cadastroest()
        Estudantes.append(Estudante)

    elif r == 2:
        Professorx = Professorx(0, "", "", 0, "")
        Professorx = Professorx.cadastroprof()
        Professorx.append(Professor)

    elif r == 3:
        for estudante in Estudantes:
            print(estudante.matricula, estudante.nome, estudante.sobrenome, estudante.idade)
    elif r == 4:
        for professor in Professores:
            print(professor.matriculap, professor.nomep, professor.sobrenomep, professor.idadep, professor.especializacaop)
    elif r == 5:
        