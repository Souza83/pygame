import pygame  # Importa a biblioteca pygame
from pygame.locals import *  # Importa de pygame tudo do submódulo locals
from sys import exit  # Importa a função exit do módulo sys que fecha a janela

# Inicializa todas as funções e variáveis da biblioteca pygame
pygame.init()


# Cria o objeto tela
largura = 640  # Medida da tela em pixel
altura = 480  # Medida da tela em pixel
x = largura/2  # Variável que representa a posição horizontal (eixo x = largura da tela / 2 = inicia no meio da tela)
y = altura/2  # Variável que representa a posição vertical (eixo y = altura da tela / 2 = inicia no meio da tela)
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
        '''
        if event.type == KEYDOWN:  # Se o evento for do tipo pressionar tecla do teclado
            if event.key == K_a:  # Se pressionar a tecla "a"
                x = x - 20  # mova para esquerda
            if event.key == K_d:  # Se pressionar a tecla "d"
                x = x + 20  # mova para direita
            if event.key == K_w:  # Se pressionar a tecla "w"
                y = y - 20  # mova para cima
            if event.key == K_s:  # Se pressionar a tecla "s"
                y = y + 20  # mova para baixo
        '''
    if pygame.key.get_pressed()[K_a]:  # Se pressionar a tecla "a"
        x = x - 20  # mova para esquerda
    if pygame.key.get_pressed()[K_d]:  # Se pressionar a tecla "d"
        x = x + 20  # mova para direita
    if pygame.key.get_pressed()[K_w]:  # Se pressionar a tecla "w"
        y = y - 20  # mova para cima
    if pygame.key.get_pressed()[K_s]:  # Se pressionar a tecla "s"
        y = y + 20  # mova para baixo

    pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))  # Desenha retangulo ((local),(cor),(posição XY e PX))

    pygame.display.update()  # Atualiza tela do jogo a cada interação do loop principal
