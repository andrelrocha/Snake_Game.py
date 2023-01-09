import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

pygame.mixer.music.set_volume(0.2)
musica_fundo = pygame.mixer.music.load("musica_fundo.wav")
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound("smw_coin.wav")

largura = 640
altura = 480
x_cobra = int((largura/2) - (45/2))
y_cobra = int(altura/2)
pontos = 0
x_maca = random.randrange(40, 600)
y_maca = random.randrange(50, 430)
fonte = pygame.font.Font("PokemonGB.ttf", 20)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

lista_cobra = []

def aumenta_cobra(lista_cobra):
    for xy in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (xy[0],xy[1],20,20))

while True:
    relogio.tick(30)
    tela.fill((255, 255, 255))
    mensagem = "Pontos: {}".format(pontos)
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if pygame.key.get_pressed()[K_a]:
        x_cobra -= 15
    if pygame.key.get_pressed()[K_d]:
        x_cobra += 15
    if pygame.key.get_pressed()[K_s]:
        y_cobra += 15
    if pygame.key.get_pressed()[K_w]:
        y_cobra -= 15

    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))

    if cobra.colliderect(maca):
        x_maca = random.randrange(40, 600)
        y_maca = random.randrange(50, 430)
        pontos += 1
        barulho_colisao.play()

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (450, 20))
    pygame.display.update()
