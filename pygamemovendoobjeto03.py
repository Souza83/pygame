import pygame  # Importa a biblioteca pygame
from pygame.locals import *  # Importa de pygame tudo do submódulo locals
from sys import exit  # Importa a função exit do módulo sys que fecha a janela

# Inicializa todas as funções e variáveis da biblioteca pygame
pygame.init()


# Cria o objeto tela
largura = 640  # Medida da tela em pixel
altura = 480  # Medida da tela em pixel
x = largura/2  # Variável que representa a posição horizontal (eixo x = largura da tela / 2 = meio da tela)
y = 0  # Variável que representa a posição vertical (eixo y)
tela = pygame.display.set_mode((largura, altura))  # Objeto que configura display
relogio = pygame.time.Clock()  # Variável que controla o tempo

# Configura nome da tela
pygame.display.set_caption('Jogo')

# loop principal do jogo
while True:
    relogio.tick(30)  # Controla a taxa de frame por segundo (numero> = rápido e n< = devagar  )
    tela.fill((0, 0, 0))  # ("Limpa tela") A cada iteração do loop infinito a tela é preenchida com a cor preta
    for event in pygame.event.get():  # Detecta se algum evento ocorreu
        if event.type == QUIT:  # Para a janela fechar ao clicar em fechar
            pygame.quit()
            exit()

    pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))  # Desenha retangulo ((local),(cor),(posição XY e PX))
    if y >= altura:  # Altera a posição ao tocar o final da tela, retorna ao inicio da tela
        y = 0  # Zera a posição do eixo vertical
    y = y + 15  # Posição do eixo y recebe acrescenta + 1 a cada iteração

    pygame.display.update()  # Atualiza tela do jogo a cada interação do loop principal
