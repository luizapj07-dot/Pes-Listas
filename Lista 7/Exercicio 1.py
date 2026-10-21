class MarcadorDePagina:
    def __init__(self, pagina_atual):
        self.pagina_atual = pagina_atual

class Livro:
    marcador_de_pagina = False
    
    def __init__(self, titulo, total_de_paginas):
        self.titulo = titulo
        self.total_de_paginas = total_de_paginas

    def adicionar_marcador(self, pagina_atual):
        self.marcador_de_pagina = MarcadorDePagina(pagina_atual)

senhor_dos_aneis = Livro("Senhor dos aneis", 20000)
senhor_dos_aneis.adicionar_marcador(500)
senhor_dos_aneis.marcador_de_pagina.pagina_atual(78)
