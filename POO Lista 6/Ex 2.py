class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor
    
    def pintar(self):
        cornew = input("Adicione uma cor: ")
        self.cor = cornew
        
    def mostrar_cor(self):
        print("A cor do carro atual é", self.cor)

Carro1 = Carro("Volkswagen", "Amarelo")

Carro1.pintar()
Carro1.mostrar_cor()