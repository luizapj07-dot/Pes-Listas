from Classses import Estudante
#Criando 3 objetos das classe estudante

estudante1 = Estudante("Pedro", "Da Silva", 17, "888.888.888-88")
estudante2 = Estudante("Schalata", "Junior", 16, "333.333.333-33")
estudante3 = Estudante("Felipe", "Dazi", 15, "444.444.444-44")

# #Ler atributo de objeto
# print(estudante1.nome)

# #Alterar atributo de objeto
# estudante1.sobrenome = "Zan"

alunos = [estudante1, estudante2, estudante3]

for aluno in alunos:
    print(aluno.nome, aluno.idade)

