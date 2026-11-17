class Carro:
    def __init__(self, placa, modelo):
        self.placa = placa
        self.modelo = modelo

class VagadeEstacionamento:
    def __init__(self, id_vaga):
        self.id_vaga = id_vaga
        self.carro_estacionado = None
    
    def ocupar_vaga(self, carro):
        if self.carro_estacionado == None:
            self.carro_estacionado = carro
            return True
        else:
            return False

    def liberar_vaga(self):
        if self.carro_estacionado != None:
            self.carro_estacionado = None
            return True
        else:
            return False
            

opcao = -1

while opcao != 0:
    print("""
          1 -- Add Carro
          2 -- Add Vaga
          3 -- ocupar_vaga
          4 -- Libertar vaga""")
    
    opcao = int(input("A opção selecionada será? "))

    if opcao == 1: 
        placex = input("A placa é: ")
        chocolex = input("O modelo é: ")

        Carro1 = Carro(placex, chocolex)
        print("Sucesso!!")

    elif opcao == 2: 
        idvagax = input("Qual o id da vaga? ")
        Carro_estacionadox = None

        Vaga1 = VagadeEstacionamento(idvagax)
        print("Sucesso!")

    elif opcao == 3: 
        resultado = Vaga1.ocupar_vaga(Carro1)
        print(resultado)
        print("Sucesso!")
    
    elif opcao == 4:
        res = Vaga1.liberar_vaga()
        print(res)