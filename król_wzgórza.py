# -*- coding: utf-8 -*-
import pygame
import random
import Buttons
import numpy as np
pygame.init()
pygame.font.init()
from pygame.locals import (#przyciski

    K_UP,

    K_DOWN,

    K_LEFT,

    K_RIGHT,

    K_ESCAPE,

    KEYDOWN,
    
    K_KP_ENTER

    #QUIT,

)
class tile(pygame.sprite.Sprite):
    def __init__(self):
        super(tile, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((random.randint(10, 200), random.randint(10, 200), random.randint(10, 200)))
        #self.surf = bomber.convert()
        #self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
def makemap(map=[]):#,tiles=[]):
    for i in range(len(map)):
        for j in range(len(map[i])):
            map[i][j] =tile()
            map[i][j].rect=((20*i,20*j))
            tiles.add(map[i][j])
    return map
                
def game():
    rungame=True
    screen.fill((0,0,0))
    #tiles = pygame.sprite.Group()
    #all_sprites.add(player)
    #t1=tile()
    #t1.rect=((50,50))
    #screen.blit(t1.surf, t1.rect)
    mapa = [[0 for i in range(35)] for j in range(35)] 
    
    mapa=makemap(mapa)
    butgm=Buttons.Button()                              # przycisk G menu 
    bw=200                      # szerokosć przycisków
    bh=80                       # wysokosć przycisków
    butgm.create_button(screen, (50,50,250), (W-bw), (H-(bh*(1))), bw, bh, 0, "Menu", (0,0,0))    #rysuje przycisk gry
    #print("game")
    while rungame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rungame = False
            if event.type == KEYDOWN:#escape
                if event.key == K_ESCAPE:
                    rungame = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if butgm.pressed(pygame.mouse.get_pos()):# Przycisk resetu               
                    rungame=False
                    #del butmg
                    mainmenu()
                #print(0)
        #for x in mapa:
            #for y in x:
                #screen.blit(mapa[x][y].surf, mapa[x][y].rect)
                #print(y)
        for entity in tiles:
            screen.blit(entity.surf, entity.rect)
        pygame.display.flip()
def mainmenu():
    runningmm=True
    screen.fill((0,0,0))
    #butmq.surface.kill()
    butmq=Buttons.Button()                              # przycisk MM wyjscie 
    butmi=Buttons.Button()                              # przycisk MM info 
    butmo=Buttons.Button()                              # przycisk MM opcje 
    butmg=Buttons.Button()                              # przycisk MM graj
    bw=300                      # szerokosć przycisków
    bh=80                       # wysokosć przycisków
    butmg.create_button(screen, (50,50,250), (W-bw)/2, (H-(bh*(4)))/2, bw, bh, 0, "GRAJ", (0,0,0))    #rysuje przycisk gry
    butmo.create_button(screen, (50,50,250), (W-bw)/2, (H-(bh*(1)))/2, bw, bh, 0, "OPCJE", (0,0,0))    #rysuje przycisk opcji
    butmi.create_button(screen, (50,50,250), (W-bw)/2, (H-(bh*(-2)))/2, bw, bh, 0, "INFO", (0,0,0))    #rysuje przycisk informacji
    butmq.create_button(screen, (50,50,250), (W-bw)/2, (H-(bh*(-5)))/2, bw, bh, 0, "WYJDŹ", (0,0,0))    #rysuje przycisk wyjscia
    while runningmm:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningmm = False
            if event.type == KEYDOWN:#escape
                if event.key == K_ESCAPE:
                    runningmm = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if butmq.pressed(pygame.mouse.get_pos()):# Przycisk resetu
                    runningmm=False
                if butmg.pressed(pygame.mouse.get_pos()):# Przycisk resetu               
                    runningmm=False
                    del butmg
                    del butmo
                    del butmi
                    del butmq
                    game()
        pygame.display.flip()

W=1000
H=700
tiles = pygame.sprite.Group()
fontm = pygame.font.SysFont(None, 40)
tmq = 'TRUP'#text
tmqi = fontm.render(tmq, True, (255, 0, 0))
screen = pygame.display.set_mode([W, H])
pygame.display.set_caption("Król Wzgórza")
running = True
mainmenu()
pygame.quit()