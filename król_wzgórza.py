# -*- coding: utf-8 -*-
import pygame
import random
import Buttons
import math
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
    
    K_SPACE,
    
    K_w,  
    
    
    K_s,  
    
    
    K_a,  
    
    
    K_d,  
    
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
        self.rigity=0
        self.cover=0
class Player(pygame.sprite.Sprite):
    def __init__(self,inmap):
        super(Player, self).__init__()
        #self.surf = pygame.Surface((75, 25))
        #self.surf.fill((255, 255, 255))
        self.surf = krol.convert()
        self.surf.set_colorkey((255, 255, 255))
        self.inmap=inmap
        self.rect = self.surf.get_rect()
        self.speed=5
        self.q=0.5
        self.maxhp=20
        self.hp=self.maxhp
        self.range=15
        self.spread=20
        self.damage=10
        #self.rect=((300,300))
    def update(self, pressed_keys):#steruje przyciskami
        #print(self.rect.center[0])
        post=self.rect.center
        tert=self.inmap[int(post[0]/20)][int(post[1]/20)].rigity
        sf=self.speed*(1-self.q*tert)
        #print(tert)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -sf)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, sf)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-sf, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(sf, 0)
            #self.rect.update((self.speed, 0))
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > W-300:
            self.rect.right = W-300
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= H:
            self.rect.bottom = H
        if self.hp<=0:
            self.kill()
class Enemy(pygame.sprite.Sprite):
    def __init__(self,inmap):
        super(Enemy, self).__init__()
        #self.surf = pygame.Surface((75, 25))
        #self.surf.fill((255, 255, 255))
        self.state=0
        self.surf = eninf.convert()
        self.surf.set_colorkey((255, 255, 255))
        self.inmap=inmap
        self.rect = self.surf.get_rect(
            center=(
                W-310,
                random.randint(10, H-10),
            )
        )
        self.timer=0
        self.reload=1000
        self.speed=3
        self.q=0.25
        self.maxhp=5
        self.hp=self.maxhp
        self.range=3
        self.damage=3
        #self.rect=((300,300))
    def update(self):#steruje przyciskami
        post=self.rect.center
        tert=self.inmap[int(post[0]/20)][int(post[1]/20)].rigity
        sf=self.speed*(1-self.q*tert)
        if self.state==1:
            self.rect.move_ip(0, -sf)
        if self.state==2:
            self.rect.move_ip(0, sf)
        if self.state==3:
            self.rect.move_ip(-sf, 0)
        if self.state==4:
            self.rect.move_ip(sf, 0)
            #self.rect.update((self.speed, 0))
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > W-300:
            self.rect.right = W-300
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= H:
            self.rect.bottom = H
        if self.hp<=0:
            self.kill()
class Marker(pygame.sprite.Sprite):
    def __init__(self,playmod):
        super(Marker, self).__init__()
        #self.surf = pygame.Surface((75, 25))
        #self.surf.fill((255, 255, 255))
        self.surf = marker.convert()
        self.surf.set_colorkey((255, 255, 255))
        self.playmod=playmod
        self.rect = self.surf.get_rect()
        self.speed=5
        self.range=15
        self.range=15
        #self.rect=((300,300))
    def update(self, pressed_keys):#steruje przyciskami
        #print(self.rect.center[0])
        #print(tert)
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -self.speed)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, self.speed)
        if pressed_keys[K_a]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(self.speed, 0)
            #self.rect.update((self.speed, 0))
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > W-300:
            self.rect.right = W-300
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= H:
            self.rect.bottom = H
def makemap(map=[]):#,tiles=[]):
    for i in range(len(map)):
        for j in range(len(map[i])):
            map[i][j] =tile()
            map[i][j].rect=((20*i,20*j))
            r=random.randint(0, 100)
            map[i][j].surf.fill((100+r, 100+r, 100+r))
            map[i][j].rigity=r/100
            tiles.add(map[i][j])
    return map
                
def game():
    rungame=True
    screen.fill((0,0,0))
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 1800)
    #tiles = pygame.sprite.Group()
    #all_sprites.add(player)
    #t1=tile()
    #t1.rect=((50,50))
    #screen.blit(t1.surf, t1.rect)
    mapa = [[0 for i in range(35)] for j in range(35)] 
    mapa=makemap(mapa)
    player = Player(mapa)#inicjuje gracza
    player.rect.x = 340
    player.rect.y = 340
    #player.hp=0
    marker=Marker(player)
    marker.rect.x = 330
    marker.rect.y = 330
    #test=player.rect()
    #player.rect=(350,350)
    enemies = pygame.sprite.Group()
    allunits = pygame.sprite.Group()
    allunits.add(player)
    playteam = pygame.sprite.Group()
    playergroup = pygame.sprite.Group()
    playergroup.add(player)
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
                if event.key == K_SPACE:
                    inacx=random.randint(-10, 10)
                    inacy=random.randint(-10, 10)
                    for entity in allunits:
                        postm=marker.rect.center
                        poste=entity.rect.center
                        dist=math.sqrt(pow(postm[0]-poste[0]+inacx,2)+pow(postm[1]-poste[1]+inacy,2))
                        if dist<=player.spread:
                            dmg=player.damage*math.sqrt(player.spread-dist)
                            entity.hp=-dmg
                            print(player.hp)
            elif event.type == ADDENEMY:
                # Create the new enemy and add it to sprite groups
                new_enemy = Enemy(mapa)
                new_enemy.state=3
                enemies.add(new_enemy)
                allunits.add(new_enemy)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if butgm.pressed(pygame.mouse.get_pos()):# Przycisk resetu               
                    rungame=False
                    #del butmg
                    mainmenu()
                x=pygame.mouse.get_pos()
                if x[0]>200 and x[0]<500 and x[0]>200 and x[0]<500:
                    new_frien=Enemy(mapa)
                    new_frien.surf = pinf.convert()
                    new_frien.surf.set_colorkey((255, 255, 255))
                    new_frien.rect.center = (x[0],x[1])
                    playergroup.add(new_frien)
                    playteam.add(new_frien)
                    allunits.add(new_frien)
                #print(0)
        #for x in mapa:
            #for y in x:
                #screen.blit(mapa[x][y].surf, mapa[x][y].rect)
                #print(y)
        
        #screen.blit(player.surf, player.rect)
        screen.fill((0, 0, 0))#czarne tło
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        marker.update(pressed_keys)
        for entity in enemies:
            for fren in playteam:
                poste=entity.rect.center
                postp=fren.rect.center
                dist=math.sqrt(pow(postp[0]-poste[0],2)+pow(postp[1]-poste[1],2))
                if dist<=entity.range*20 and pygame.time.get_ticks()>entity.timer:
                    entity.timer=pygame.time.get_ticks()+entity.reload
                    fren.hp=fren.hp-entity.damage
                if dist<=fren.range*20 and pygame.time.get_ticks()>fren.timer:
                    fren.timer=pygame.time.get_ticks()+fren.reload
                    entity.hp=entity.hp-fren.damage
                    #print(fren.hp)
        
        for entity in tiles:
            screen.blit(entity.surf, entity.rect)
        for entity in enemies:
            entity.update()
            screen.blit(entity.surf, entity.rect)
        for entity in playteam:
            entity.update()
        for entity in playergroup:
            screen.blit(entity.surf, entity.rect)
        #screen.blit(player.surf, player.rect)
        screen.blit(marker.surf, marker.rect)
        butgm.create_button(screen, (50,50,250), (W-bw), (H-(bh*(1))), bw, bh, 0, "Menu", (0,0,0))    #rysuje przycisk gry
        clock.tick(30)# fps
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
test=0
krol=pygame.image.load("krol.png")
marker=pygame.image.load("marker.png")
eninf=pygame.image.load("eninf.png")
pinf=pygame.image.load("pinf.png")
entank=pygame.image.load("entank.png")
ptank=pygame.image.load("ptank.png")
tiles = pygame.sprite.Group()
clock = pygame.time.Clock()#Dla ustawiania fps
fontm = pygame.font.SysFont(None, 40)
tmq = 'TRUP'#text
tmqi = fontm.render(tmq, True, (255, 0, 0))
screen = pygame.display.set_mode([W, H])
pygame.display.set_caption("Król Wzgórza")
running = True
mainmenu()
pygame.quit()