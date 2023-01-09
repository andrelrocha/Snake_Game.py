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

velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = random.randrange(40, 600)
y_maca = random.randrange(50, 430)


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()
pontos = 0
fonte = pygame.font.Font("PokemonGB.ttf", 20)

lista_cobra = []
comprimento_inicial = 5


def aumenta_cobra(lista_cobra):
    for xy in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (xy[0], xy[1], 20, 20))


while True:
    relogio.tick(30)
    tela.fill((255, 255, 255))
    mensagem = "Pontos: {}".format(pontos)
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else: 
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d: 
                if x_controle == -velocidade:
                    pass
                else: 
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade

    if y_cobra >= altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura
    if x_cobra >= largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura

    x_cobra += x_controle
    y_cobra += y_controle

    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))

    if cobra.colliderect(maca):
        x_maca = random.randrange(40, 600)
        y_maca = random.randrange(50, 430)
        pontos += 1
        barulho_colisao.play()
        comprimento_inicial += 1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (450, 20))
    pygame.display.update()
