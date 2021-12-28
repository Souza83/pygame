import pygame  # Importa a biblioteca pygame
from pygame.locals import *  # Importa de pygame tudo do submódulo locals
from sys import exit  # Importa a função exit do módulo sys que fecha a janela

# Inicializa todas as funções e variáveis da biblioteca pygame
pygame.init()

# Cria o objeto tela
largura = 640  # Medida da tela em pixel
altura = 480  # Medida da tela em pixel
tela = pygame.display.set_mode((largura, altura))  # Objeto que configura display

# Configura nome da tela
pygame.display.set_caption('Jogo')

# loop principal do jogo
while True:
    for event in pygame.event.get():  # Detecta se algum evento ocorreu
        if event.type == QUIT:  # Para a janela fechar ao clicar em fechar
            pygame.quit()
            exit()
    pygame.draw.rect(tela, (255,0,0), (200,300,40,50))  # Desenha retangulo ((local),(cor),(posição XY e PX))
    pygame.draw.circle(tela, (0, 0, 255), (300, 260), 40)  # Desenha círculo ((local),(cor),(posição XY) e Raio)
    pygame.draw.line(tela, (255, 255, 0), (390, 0), (390,600), 5)  # Desenha linha ((local),(cor),(posição XY)espessura)
    pygame.display.update()  #  Atualiza tela do jogo a cada interação do loop principal

