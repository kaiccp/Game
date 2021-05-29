#Game de Kaic Salomão
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

musica_de_fundo = pygame.mixer.music.load("sound.mp3")
pygame.mixer.music.set_volume(0.2)

coin = pygame.mixer.Sound("coin.wav")
coin.set_volume(0.5)

pygame.mixer.music.play(-1)
relogio = pygame.time.Clock()

largura = 640
altura = 480
#posição da cobra
x = largura/2-30/2
y = altura/2-30/2
#posição da maça
xM = randint(10, 630)
yM = randint(10, 470)
#fontes
fonte = pygame.font.SysFont("monospace", 16, bold=True, italic=False)
postos = 0
#cores
colorWhite = (255, 255, 255)
colorRed = (255, 0, 0)
colorGreen = (0, 255, 0)

window = pygame.display.set_mode((largura, altura))
#nome da janela
pygame.display.set_caption("Cobrinha")


#Game Loop:
while True:
    window.fill((0, 0, 0))
    message = f"Pontos: {postos}"
    texto_formatado = fonte.render(message, True, colorWhite)
    #fps
    relogio.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                x-=5
            if event.key == K_w:
                y-=5
            if event.key == K_s:
                y+=5
            if event.key == K_d:
                x+=5
                '''
    if pygame.key.get_pressed()[K_a]:
        x-=5
    if pygame.key.get_pressed()[K_w]:
        y-=5
    if pygame.key.get_pressed()[K_s]:
        y+=5
    if pygame.key.get_pressed()[K_d]:
        x+=5


    #desenhando um retangulo
    cobra = pygame.draw.rect(window, colorGreen, (x, y, 30, 30))
    maca = pygame.draw.rect(window, colorRed, (xM, yM, 10, 10))

    window.blit(texto_formatado, (450, 40))
    if cobra.colliderect(maca):
        xM = randint(10, 630)
        yM = randint(10, 470)
        postos+=1
        coin.play()
        
        
    pygame.display.update()
