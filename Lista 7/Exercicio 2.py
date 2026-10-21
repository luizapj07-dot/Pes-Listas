class CPU: #Essa é quase inteira dentro da Computador!!
    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo
    
class Computador:
    def __init__(self, tipo, cpu):
        self.tipo = tipo
        self.cpu = cpu
    
computador = Computador("Gamer", CPU("Intel", "i7-12700K"))

print(computador.cpu.fabricante)