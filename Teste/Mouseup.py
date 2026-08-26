import pygame


# Inicia o Pygame
pygame.init()


# Cria a janela
tela = pygame.display.set_mode((800, 600))


# Título da janela
pygame.display.set_caption("Teste do Mouse")


# Variáveis para verificar os botões do mouse
mouse = {
    "left": False,
    "middle": False,
    "right": False
}


# Fonte para mostrar informações na tela
fonte = pygame.font.Font(None, 36)


# Mantém o programa aberto
rodando = True


while rodando:

    # Analisa os eventos
    for event in pygame.event.get():

        # Fecha a janela
        if event.type == pygame.QUIT:
            rodando = False


        # Quando um botão do mouse é pressionado
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
                mouse["left"] = True

            if event.button == 2:
                mouse["middle"] = True

            if event.button == 3:
                mouse["right"] = True


        # Quando um botão do mouse é solto
        if event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1:
                mouse["left"] = False

            if event.button == 2:
                mouse["middle"] = False

            if event.button == 3:
                mouse["right"] = False


    # Cor de fundo
    tela.fill((30, 30, 30))


    # Textos que mostram o estado dos botões
    texto_esquerdo = fonte.render(
        f"Esquerdo: {mouse['left']}",
        True,
        (255, 255, 255)
    )

    texto_meio = fonte.render(
        f"Meio: {mouse['middle']}",
        True,
        (255, 255, 255)
    )

    texto_direito = fonte.render(
        f"Direito: {mouse['right']}",
        True,
        (255, 255, 255)
    )


    # Coloca os textos na tela
    tela.blit(texto_esquerdo, (50, 100))
    tela.blit(texto_meio, (50, 200))
    tela.blit(texto_direito, (50, 300))


    # Atualiza a tela
    pygame.display.flip()


# Encerra o Pygame
pygame.quit()