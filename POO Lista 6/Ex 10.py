import pickle

# Estudante
class Estudante:
    def __init__(self, matricula, nome, sobrenome, idade):
        self.matricula = matricula
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def cadastroest(self):
        matriculax = int(input("Digite a matrícula do estudante: "))
        nomex = input("Digite o nome do estudante: ")
        sobrenomex = input("Digite o sobrenome do estudante: ")
        idadex = int(input("Digite a idade do estudante: "))

        return Estudante(matriculax, nomex, sobrenomex, idadex)


Estudantes = []


# Professor
class Professor:
    def __init__(self, matriculap, nomep, sobrenomep, idadep, especializacaop):
        self.matriculap = matriculap
        self.nomep = nomep
        self.sobrenomep = sobrenomep
        self.idadep = idadep
        self.especializacaop = especializacaop

    def cadastroprof(self):
        matriculaxprof = int(input("Digite a matrícula do professor: "))
        nomexprof = input("Digite o nome do professor: ")
        sobrenomexprof = input("Digite o sobrenome do professor: ")
        idadexprof = int(input("Digite a idade do professor: "))
        especializacaoxprof = input("Digite a especialização do professor: ")

        return Professor(
            matriculaxprof,
            nomexprof,
            sobrenomexprof,
            idadexprof,
            especializacaoxprof
        )


Professores = []

r = -1

while r != 0:
    print("""Sistema de Cadastro
    --------------------
    1 - Cadastrar estudante
    2 - Cadastrar professor
    3 - Listar estudantes
    4 - Listar professores
    5 - Alterar estudante pela matrícula
    6 - Alterar estudante pelo nome
    7 - Alterar professor pela matrícula
    8 - Alterar professor pelo nome
    9 - Excluir estudante pela matrícula
    10 - Excluir professor pela matrícula
    11 - Salvar dados
    12 - Carregar dados
    0 - Sair
    """)

    r = int(input("Digite a opção desejada: "))

    if r == 1:
        estudantex = Estudante(0, "", "", 0)
        estudantex = estudantex.cadastroest()
        Estudantes.append(estudantex)
        print("Estudante cadastrado com sucesso!")

    elif r == 2:
        professorx = Professor(0, "", "", 0, "")
        professorx = professorx.cadastroprof()
        Professores.append(professorx)
        print("Professor cadastrado com sucesso!")

    elif r == 3:
        if not Estudantes:
            print("Nenhum estudante cadastrado.")
        else:
            for estudante in Estudantes:
                print(
                    estudante.matricula,
                    estudante.nome,
                    estudante.sobrenome,
                    estudante.idade
                )

    elif r == 4:
        if not Professores:
            print("Nenhum professor cadastrado.")
        else:
            for professor in Professores:
                print(
                    professor.matriculap,
                    professor.nomep,
                    professor.sobrenomep,
                    professor.idadep,
                    professor.especializacaop
                )

    elif r == 5:
        matricula = int(input("Digite a matrícula do estudante: "))
        encontrado = False

        for estudante in Estudantes:
            if estudante.matricula == matricula:
                estudante.nome = input("Digite o novo nome: ")
                estudante.sobrenome = input("Digite o novo sobrenome: ")
                estudante.idade = int(input("Digite a nova idade: "))

                encontrado = True
                print("Estudante alterado com sucesso!")
                break

        if not encontrado:
            print("Estudante não encontrado!")

    elif r == 6:
        nome = input("Digite o nome do estudante que deseja alterar: ")
        encontrado = False

        for estudante in Estudantes:
            if estudante.nome == nome:
                estudante.nome = input("Digite o novo nome: ")
                estudante.sobrenome = input("Digite o novo sobrenome: ")
                estudante.idade = int(input("Digite a nova idade: "))

                encontrado = True
                print("Estudante alterado com sucesso!")
                break

        if not encontrado:
            print("Estudante não encontrado!")

    elif r == 7:
        matricula = int(input("Digite a matrícula do professor: "))
        encontrado = False

        for professor in Professores:
            if professor.matriculap == matricula:
                professor.nomep = input("Digite o novo nome: ")
                professor.sobrenomep = input("Digite o novo sobrenome: ")
                professor.idadep = int(input("Digite a nova idade: "))
                professor.especializacaop = input(
                    "Digite a nova especialização: "
                )

                encontrado = True
                print("Professor alterado com sucesso!")
                break

        if not encontrado:
            print("Professor não encontrado!")

    elif r == 8:
        nome = input("Digite o nome do professor que deseja alterar: ")
        encontrado = False

        for professor in Professores:
            if professor.nomep == nome:
                professor.nomep = input("Digite o novo nome: ")
                professor.sobrenomep = input("Digite o novo sobrenome: ")
                professor.idadep = int(input("Digite a nova idade: "))
                professor.especializacaop = input(
                    "Digite a nova especialização: "
                )

                encontrado = True
                print("Professor alterado com sucesso!")
                break

        if not encontrado:
            print("Professor não encontrado!")

    elif r == 9:
        matricula = int(input("Digite a matrícula do estudante que deseja excluir: "))
        encontrado = False

        for estudante in Estudantes:
            if estudante.matricula == matricula:
                Estudantes.remove(estudante)
                encontrado = True
                print("Estudante excluído com sucesso!")
                break

        if not encontrado:
            print("Estudante não encontrado!")

    elif r == 10:
        matricula = int(input("Digite a matrícula do professor que deseja excluir: "))
        encontrado = False

        for professor in Professores:
            if professor.matriculap == matricula:
                Professores.remove(professor)
                encontrado = True
                print("Professor excluído com sucesso!")
                break

        if not encontrado:
            print("Professor não encontrado!")

    elif r == 11:
        with open("cadastro.pkl", "wb") as arquivo:
            pickle.dump((Estudantes, Professores), arquivo)

        print("Dados salvos com sucesso!")

    elif r == 12:
        try:
            with open("cadastro.pkl", "rb") as arquivo:
                Estudantes, Professores = pickle.load(arquivo)

            print("Dados carregados com sucesso!")

        except FileNotFoundError:
            print("Arquivo não encontrado. Salve os dados primeiro!")

        except (pickle.UnpicklingError, EOFError, ValueError, TypeError):
            print("Não foi possível carregar os dados do arquivo!")

    elif r == 0:
        print("Saindo do sistema!")

    else:
        print("Opção inválida!")