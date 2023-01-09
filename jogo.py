import pygame
from pygame.locals import *
from sys import exit 
import random

def atualizar_movimento(x,y):
        if pygame.key.get_pressed()[K_a]:
            x-=20
        if pygame.key.get_pressed()[K_d]:
            x+=20
        if pygame.key.get_pressed()[K_s]:
            y+=20
        if pygame.key.get_pressed()[K_w]:
            y-=20

        if y==altura: 
            y=0
        if y<0:
            y=altura
        if x==largura:
            x=0
        if x<0:
            x=largura
        return x,y

pygame.init()

pygame.mixer.music.set_volume(0.2)
musica_fundo=pygame.mixer.music.load("musica_fundo.wav")
pygame.mixer.music.play(-1)

barulho_colisao=pygame.mixer.Sound("smw_coin.wav")

largura=640
altura=480
x=int((largura/2) - (45/2))
y=int(altura/2)
pontos=0
x_azul=random.randrange(40,600)
y_azul=random.randrange(50,430)
fonte = pygame.font.Font("PokemonGB.ttf", 20)

tela=pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo')
relogio=pygame.time.Clock()

while True:
    relogio.tick(60)
    tela.fill((0,0,0))
    mensagem="Pontos: {}".format(pontos)
    texto_formatado=fonte.render(mensagem, True, (255,255,255))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()     
        x,y=atualizar_movimento(x,y)

    cobra=pygame.draw.rect(tela, (0,255,0), (x,y,20,20))
    maca=pygame.draw.rect(tela, (255,0,0), (x_azul,y_azul,20,20))

    if cobra.colliderect(maca):
        x_azul=random.randrange(40,600)
        y_azul=random.randrange(50,430)
        pontos+=1
        barulho_colisao.play()

    tela.blit(texto_formatado, (450,20))
    pygame.display.update()