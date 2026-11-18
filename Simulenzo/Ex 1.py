class Bancada:
    def __init__(self, numero, note):
        self.numero = numero
        self.notebook_atual = None

    def colocar(self, notebook):
        if self.notebook_atual == None:
            self.notebook_atual = notebook
            return True
        else:
            return False
    
    def retirar(self):
        self.notebook_atual = None

class Notebook:
    def __init__(self, patrimonio, marca):
        self.patrimonio = patrimonio
        self.marca = marca

notebook1 = Notebook("N-001", "Dell")
notebook2 = Notebook("N-002", "Lenovo")

bancada1 = Bancada("B-03")

print(bancada1.colocar(notebook1))  # True
print(bancada1.colocar(notebook2))  # False

print(bancada1.notebook_atual.marca)  # Dell

bancada1.retirar()

print(bancada1.notebook_atual)  # None
