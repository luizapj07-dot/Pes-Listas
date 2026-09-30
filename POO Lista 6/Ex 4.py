class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def esta_disponivel(self):
        if self.quantidade > 0:
            print ("True")
        else:
            print("False")

    def vender(self):
        self.quantidade -= 1

Produto1 = Produto("bolacha", 1)

Produto1.esta_disponivel()
Produto1.vender()
Produto1.esta_disponivel()