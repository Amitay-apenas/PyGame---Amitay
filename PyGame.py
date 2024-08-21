import pygame
import sys
import random

#função de randomização
def random_color_generator() -> tuple:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return(r, g, b)
def random_radius_generator() -> tuple:
    ratio = random.randint(20, 50)
    return(ratio)

# Inicializa o Pygame
pygame.init()

# Define as dimensões da janela
largura = 800
altura = 600

# Define a cor do círculo e do fundo
  # Vermelho
cor_fundo = (255, 255, 255)      # Preto

# Cria a janela do jogo
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Círculo segue o cursor do mouse')

# Define o raio do círculo


# Loop principal do jogo
while True:
    # Processa os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtém a posição do cursor do mouse
    x_mouse, y_mouse = pygame.mouse.get_pos()

    # Atualiza a tela
    tela.fill(cor_fundo)
    cor_circulo = random_color_generator()
    raio_circulo = random_radius_generator() 
    pygame.draw.circle(tela, cor_circulo, (x_mouse, y_mouse), raio_circulo)
    pygame.display.flip()

    # Define a taxa de atualização do jogo
    pygame.time.Clock().tick(60)