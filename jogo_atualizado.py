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
morreu = False


def aumenta_cobra(lista_cobra):
    for xy in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (xy[0], xy[1], 20, 20))


def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int((largura/2) - (45/2))
    y_cobra = int(altura/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = random.randrange(40, 600)
    y_maca = random.randrange(50, 430)
    morreu = False


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

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.Font("PokemonGB.ttf", 12)
        mensagem = "Game Over!"
        mensagem2 = "Pressione a tecla R para jogar novamente"
        texto_gameover = fonte.render(mensagem, True, (0, 0, 0))
        texto_gameover2 = fonte2.render(mensagem2, True, (0, 0, 0))
        ret_texto = texto_gameover.get_rect()
        ret_texto2 = texto_gameover2.get_rect()

        morreu = True
        while morreu:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2 - ret_texto.height//2)
            ret_texto2.center = (
                largura//2, (altura//2 + ret_texto2.height//2) + 10)
            tela.blit(texto_gameover, ret_texto)
            tela.blit(texto_gameover2, ret_texto2)
            pygame.display.update()

    if y_cobra >= altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura
    if x_cobra >= largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (450, 20))
    pygame.display.update()