Condutores = {
    "001": {
        "Nome": "Roberto Souza",
        "Caminhão": "Monobloco",
        "DH_Saida": ["01/01/2026", "01:00"],
        "DH_Chegada": ["01/01/2026", "02:00"]
    },

    "002": {
        "Nome": "João Graciano",
        "Caminhão": "Scania 112 HW",
        "DH_Saida": ["01/01/2026", "02:00"],
        "DH_Chegada": ["01/01/2026", "03:30"]
    },

    "003": {
        "Nome": "Karine Silva",
        "Caminhão": "Volkswagen Express 4150",
        "DH_Saida": ["01/01/2026", "03:00"],
        "DH_Chegada": ["01/01/2026", "04:00"]
    },

    "004": {
        "Nome": "Pedro Luiz",
        "Caminhão": "Volkswagen Express 6160",
        "DH_Saida": ["01/01/2026", "04:00"],
        "DH_Chegada": ["01/01/2026", "06:00"]
    },

    "005": {
        "Nome": "Maria Catarina",
        "Caminhão": "Volkswagen VW 17230 Worker",
        "DH_Saida": ["01/01/2026", "05:00"],
        "DH_Chegada": ["01/01/2026", "07:30"]
    },

    "006": {
        "Nome": "Júlio Cardoso",
        "Caminhão": "Volkswagen Express 9170",
        "DH_Saida": ["01/01/2026", "06:00"],
        "DH_Chegada": ["01/01/2026", "08:00"]
    },

    "007": {
        "Nome": "Altivo Antônio",
        "Caminhão": "Iveco Daily 40s14",
        "DH_Saida": ["01/01/2026", "07:00"],
        "DH_Chegada": ["01/01/2026", "09:00"]
    },

    "008": {
        "Nome": "Jorge Gonçalves",
        "Caminhão": "Iveco Tectro 310E28",
        "DH_Saida": ["01/01/2026", "08:00"],
        "DH_Chegada": ["01/01/2026", "10:30"]
    },

    "009": {
        "Nome": "Marcos Vinícius",
        "Caminhão": "Monobloco",
        "DH_Saida": ["01/01/2026", "03:00"],
        "DH_Chegada": ["01/01/2026", "05:00"]
    },

    "010": {
        "Nome": "Heleno Nunes",
        "Caminhão": "Scania 112 HW",
        "DH_Saida": ["01/01/2026", "04:00"],
        "DH_Chegada": ["01/01/2026", "06:30"]
    },

    "011": {
        "Nome": "Mara Cristina",
        "Caminhão": "Volkswagen Express 4150",
        "DH_Saida": ["01/01/2026", "05:00"],
        "DH_Chegada": ["01/01/2026", "07:00"]
    },

    "012": {
        "Nome": "Otávio Rocha",
        "Caminhão": "Volkswagen Express 6160",
        "DH_Saida": ["01/01/2026", "07:00"],
        "DH_Chegada": ["01/01/2026", "09:00"]
    }
}

opcao = -1

while opcao != 0:
    print("""
    1 - Listar Cadastro de Caminhões
    2 - Listar Cadastro de Condutores
    3 - Listar Veículos que Retornaram
    4 - Verificar se Todas as entregas foram feitas
    0 - Cancelar    
    """)
    opcao = int(input("Digite a opcao desejada: "))
    if opcao == 1:
        for chave in Condutores.keys():
            print("Caminhão: ", Condutores[chave]["Caminhão"])

    elif opcao == 2:
        for chave in Condutores.keys():
            print("Condutor: ", Condutores[chave]["Nome"])

    elif opcao == 3:
        for chave in Condutores.keys():
            print("No dia: ", Condutores[chave]["DH_Chegada"], "passou o veículo: ", Condutores[chave]["Caminhão"])

    elif opcao == 4:
        hr = int(input("Digite que horas são (sem minutos): "))
        if hr > 10:
            print("As entregas já foram feitas!!")
        elif hr < 10:
            print("As entregas não terminaram!!")
        else:
            min = int(input("Digite os minutos: "))
            if min > 29:
                print("As entregas já foram feitas!!")
            else:
                print("As entregas não terminaram!!")

