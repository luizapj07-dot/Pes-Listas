class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descricao(self):
        print(self.titulo, "foi escrito por", self.autor)

Livro1 = Livro("20 Mil léguas submarinas", "Júlio Verne")

Livro1.descricao()