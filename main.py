import pygame
import sys
from pygame.locals import *


largura = 700
altura = 600

class naveEspacial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagemPlayer = pygame.image.load('soldado.png')

        self.rect = self.imagemPlayer.get_rect()
        self.rect.centerx = largura / 2
        self.rect.centery = altura - 500

        self.listaDisparo = []
        self.vidas = True

def disparar():
    pass


def jogo():
    pygame.init()
    screen = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Wartiming")

    run = True
    while run == True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False

    pygame.display.update()



jogo()




