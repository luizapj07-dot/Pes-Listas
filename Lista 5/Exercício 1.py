professores = {
    "001": {
        "nome" : "Prof Thiago Paes",
        "laboratorios": ["Lab102", "Lab105", "Lab106", "Lab107"]
    },
    "002": {
        "nome": "Prof Schalata",
        "laboratorios": ["Lab106", "Lab107"]
    },
    "003": {
        "nome": "Prof Ignácio",
        "laboratorios": ["Lab102", "Lab105", "Lab106"]
    },
    "004": {
        "nome": "Prof Ryan",
        "laboratorios": ["Lab102", "Lab104"]
    },
    "005": {
        "nome": "Prof André",
        "laboratorios": ["Lab102", "Lab104", "Lab107"]
    },
    "006": {
        "nome": "Prof Fabiana",
        "laboratorios": ["Lab102"]
    },
    "007": {
        "nome": "Prof Alberto",
        "laboratorios": ["Lab103", "Lab105"]
    },
    "008": {
        "nome": "Prof Juliano",
        "laboratorios": ["Lab104"]
    },
    "009": {
        "nome": "Prof Thiago Waltrik",
        "laboratorios": ["Lab105", "Lab106", "Lab107"]
    },
    "010": {
        "nome": "Prof João Eduardo",
        "laboratorios": ["Lab107"]
    }
}

opcao = -1

while opcao != 0:

    print("""
        1 - Adicionar Professor
        2 - Alterar Professor
        3 - Excluir Professor
        4 - Listar Professor
        5 - Adicionar acesso
        6 - Alterar acesso
        7 - Excluir acesso
        8 - Listar acesso
        9 - Testar acesso
          """)
    opcao = int(input("Digite a opção:"))
    
    if opcao == 1:
        codigo = input("Digite o código do professor: ")
        nome = input("Digite o nome do professor: ")

        professores[codigo] = {
            "nome": nome,
            "laboratorios": []
        }
        print("Professor cadastrado com sucesso!")
    elif opcao == 2:
        codigo = input("Digite o código do professor:")

        if codigo in professores:
            nome = input("Qual será o nome do professor:")

            professores[codigo]["nome"] = nome
        
            print("Professor alterado com sucesso!")
        else:
            print("Professor não encontrado!")
    elif opcao == 3:
        codigo = input("Digite o código do professor:")

        if codigo in professores:
            del professores[codigo]
            print("Professor deletado com sucesso!")
        else:
            print("Professor não encontrado!")
    elif opcao == 4:
        for codigo, dados in professores.items():
            print ("Código:", codigo)
            print("Nome:", dados["nome"])
            print("Laboratórios:", dados["laboratorios"])
            print("--------------------")
    elif opcao == 5:
        codigo = input("Digite o código do professor: ")
        if codigo in professores:
            laboratorio = input("Digite o laboratorio que deseja adicionar:")

            professores[codigo]["laboratorio"].append(laboratorio)
            print("Acesso adicionado com sucesso!")
        else:
            print("Professor não encontrado!")
    elif opcao == 6:
        codigo = input("Digite o acesso que deseja alterar: ")
        if codigo in professores:
            laboratorio_atual = input("Laboratório que deseja alterar")

            if laboratorio_atual in professores[codigo]["laboratorios"]:
                novo_laboratorio = input("Digite o novo lab: ")

                professores[codigo]["laboratorios"].remove(laboratorio_atual)
                professores[codigo]["laboratorios"].append(novo_laboratorio)

                print("Acesso alterardo!")
            else:
                print("O professor não possui este laboratório:")
        else:
            print("Professor não encontrado!!")
    elif opcao == 7:
        codigo = input("Digite o codigo a ser excluído:")

        if codigo in professores:
            acesso = input("Digite o acesso a ser excluído:")
            
            if acesso in professores[codigo]["laboratorios"]:
                professores[codigo]["laboratorios"].remove(acesso)

                print("Acesso excluído com sucesso!")
            else:
                print("Acesso não é do professor!")
        else:
            print("Professor não encontrado!")
    elif opcao == 8: # não entendi esta parte!!
        if codigo in professores:
            print("Professor:", professores[codigo]["nome"])
            print("Laboratórios:", professores[codigo]["laboratorios"])
        else:
            print("Professor não encontrado!")
    
    elif opcao == 9:
        codigo = input("Qual professor (código) estás procurando:")
    
        if codigo in professores:
            lab = input("E em que sala: ")
    
            if lab in professores[codigo]["laboratorio"]:
                print("Professor online")
            else:
                print("Professor offline")
        else: 
            print("Professor inexistente!")

