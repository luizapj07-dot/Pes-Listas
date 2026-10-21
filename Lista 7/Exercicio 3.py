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
            return "True"
        else:
            return "False"

vaga1 = VagadeEstacionamento(1)
carro = Carro(234789, "Gol")
print(vaga1.ocupar_vaga(carro))
