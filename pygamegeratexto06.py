import pygame  # Importa a biblioteca pygame
from pygame.locals import *  # Importa de pygame tudo do submódulo locals
from sys import exit  # Importa a função exit do módulo sys que fecha a janela
from random import randint  # Sorteia valores de um determinado intervalo
# Inicializa todas as funções e variáveis da biblioteca pygame
pygame.init()


# Cria o objeto tela
largura = 640  # Medida da tela em pixel
altura = 480  # Medida da tela em pixel

x = largura/2  # Variável que representa a posição horizontal (eixo x = largura da tela / 2 = inicia no meio da tela)
y = altura/2  # Variável que representa a posição vertical (eixo y = altura da tela / 2 = inicia no meio da tela)
x_azul = randint(40, 600)  # Variável que recebe valor aleatório entre 40 a 600 para o eixo x
y_azul = randint(50, 430)  # Variável que recebe valor aleatório entre 50 a 430 para o eixo y
pontos = 0

fonte = pygame.font.SysFont('arial', 40, True, True)  # Define fonte, tamanho, negrito e itálico ()

tela = pygame.display.set_mode((largura, altura))  # Objeto que configura display

relogio = pygame.time.Clock()  # Variável que controla o tempo

# Configura nome da tela
pygame.display.set_caption('Jogo')

# loop principal do jogo
while True:
    relogio.tick(30)  # Controla a taxa de frame por segundo (numero> = rápido e n< = devagar  )
    tela.fill((0, 0, 0))  # ("Limpa tela") A cada iteração do loop infinito a tela é preenchida com a cor preta
    mensagem = f'Pontos: {pontos}'  # Formata a mensagem que exibirá na tela com a variável pontos
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))  # Variável que formata (mensagem, pixelização e cor)
    for event in pygame.event.get():  # Detecta se algum evento ocorreu
        if event.type == QUIT:  # Para a janela fechar ao clicar em fechar
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:  # Se pressionar a tecla "a"
        x = x - 20  # mova para esquerda
    if pygame.key.get_pressed()[K_d]:  # Se pressionar a tecla "d"
        x = x + 20  # mova para direita
    if pygame.key.get_pressed()[K_w]:  # Se pressionar a tecla "w"
        y = y - 20  # mova para cima
    if pygame.key.get_pressed()[K_s]:  # Se pressionar a tecla "s"
        y = y + 20  # mova para baixo

    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))  # Desenha retangulo vermelho ((local),(cor),(posição XY e PX))
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 50))  # Desenha retangulo azul ((local),(cor),(posição XY e PX))

    if ret_vermelho.colliderect(ret_azul):  # Verifica se colidiu ou sobrepôs
        x_azul = randint(40, 600)  # Variável que recebe valor aleatório entre 40 a 600 para o eixo x
        y_azul = randint(50, 430)  # Variável que recebe valor aleatório entre 50 a 430 para o eixo y
        pontos += 1  # Recebe valor de pontos + 1 ao colidirem
    tela.blit(texto_formatado, (400,40))# Exibe o texto na tela na posição XY.

    pygame.display.update()  # Atualiza tela do jogo a cada interação do loop principal
