# -*- coding: utf-8 -*-
import pygame
import random
import Buttons
import math
#import numpy as np
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
class filler(pygame.sprite.Sprite):# Pola terenu
    def __init__(self):
        super(filler, self).__init__()
        self.surf = pygame.Surface((300, H))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
class tile(pygame.sprite.Sprite):# Pola terenu
    def __init__(self):
        super(tile, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((random.randint(10, 200), random.randint(10, 200), random.randint(10, 200)))
        #self.surf = bomber.convert()
        #self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rigity=0
        self.cover=0
class Player(pygame.sprite.Sprite):     # Klasa grzacza
    def __init__(self,inmap,anyun):
        super(Player, self).__init__()
        #self.surf = pygame.Surface((75, 25))
        #self.surf.fill((255, 255, 255))
        self.surf = krol.convert()
        self.surf.set_colorkey((255, 255, 255))
        self.inmap=inmap
        self.rect = self.surf.get_rect()
        self.timer=0
        self.reload=2000
        self.speed=5
        self.q=0.5
        self.maxhp=20
        self.hp=self.maxhp
        self.range=200
        self.spread=50
        self.damage=10
        self.anyun=anyun
        #self.rect=((300,300))
    def colisdet(self):
        a=0
        self.anyun.remove(self)
        if pygame.sprite.spritecollideany(self, self.anyun):
            a=1
        self.anyun.add(self)
        return a
    def update(self, pressed_keys):#steruje przyciskami
        #print(self.rect.center[0])
        post=self.rect.center
        tert=self.inmap[int(post[0]/20)][int(post[1]/20)].rigity
        sf=self.speed*(1-self.q*tert)
        #print(tert)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -sf)
            if self.colisdet()==1:
                self.rect.move_ip(0, sf)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, sf)
            if self.colisdet()==1:
                self.rect.move_ip(0, -sf)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-sf, 0)
            if self.colisdet()==1:
                self.rect.move_ip(sf, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(sf, 0)
            if self.colisdet()==1:
                self.rect.move_ip(-sf, 0)
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
class Enemy(pygame.sprite.Sprite):  # Klasa npc
    def __init__(self,inmap,anyun):
        super(Enemy, self).__init__()
        #self.surf = pygame.Surface((75, 25))
        #self.surf.fill((255, 255, 255))
        self.state=0
        self.surf = eninf.convert()
        self.surf.set_colorkey((255, 255, 255))
        self.inmap=inmap
        self.rect = self.surf.get_rect(
            center=(
                0,
                0,
            )
        )
        self.timer=0
        self.reload=1000
        self.speed=2
        self.q=0.25                 # Jak bardzo teren wpływa na jednostkę
        self.maxhp=5
        self.hp=self.maxhp
        self.range=3
        self.damage=3
        self.anyun=anyun
        self.target=[350,350]
        #self.rect=((300,300))
    def decision(self):
        tg=self.target
        xy=[self.rect.centerx,self.rect.centery]
        if abs(tg[0]-xy[0])<10 and abs(tg[1]-xy[1])<10:
            self.state=0
        elif xy[0]<tg[0]:
            self.state=4
        elif xy[0]>tg[0]:
            self.state=3
        elif xy[1]<tg[1]:
            self.state=2
        elif xy[1]>tg[1]:
            self.state=1
        
    def colisdet(self):
        a=0
        self.anyun.remove(self)
        if pygame.sprite.spritecollideany(self, self.anyun):
            a=1
        self.anyun.add(self)
        return a
    def update(self):#steruje przyciskami
        self.decision()
        post=self.rect.center
        tert=self.inmap[int(post[0]/20)][int(post[1]/20)].rigity
        sf=self.speed*(1-self.q*tert)
        if self.state==1:
            self.rect.move_ip(0, -sf)
            if self.colisdet()==1:
                self.rect.move_ip(0, sf)
        if self.state==2:
            self.rect.move_ip(0, sf)
            if self.colisdet()==1:
                self.rect.move_ip(0, -sf)
        if self.state==3:
            self.rect.move_ip(-sf, 0)
            if self.colisdet()==1:
                self.rect.move_ip(sf, 0)
        if self.state==4:
            self.rect.move_ip(sf, 0)
            if self.colisdet()==1:
                self.rect.move_ip(-sf, 0)
            #self.rect.update((self.speed, 0))
        #self.colisdet()
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
class Marker(pygame.sprite.Sprite):     # Klasa celownika
    def __init__(self,playmod):
        super(Marker, self).__init__()
        #self.surf = pygame.Surface((75, 25))
        #self.surf.fill((255, 255, 255))
        self.surf = marker.convert()
        self.surf.set_colorkey((255, 255, 255))
        self.playmod=playmod
        self.rect = self.surf.get_rect()
        self.speed=5
        self.xy=[0,0]
        #self.rect=((300,300))
    def update(self, pressed_keys):#steruje przyciskami
        # ruch markera
        if pressed_keys[K_w]:
            #self.rect.move_ip(0, -self.speed)
            self.xy[1]= self.xy[1]-self.speed
        if pressed_keys[K_s]:
            #self.rect.move_ip(0, self.speed)
            self.xy[1]= self.xy[1]+self.speed
        if pressed_keys[K_a]:
            #self.rect.move_ip(-self.speed, 0)
            self.xy[0]= self.xy[0]-self.speed
        if pressed_keys[K_d]:
            #self.rect.move_ip(self.speed, 0)
            self.xy[0]= self.xy[0]+self.speed
        # granice
        ran=self.playmod.range
        if self.xy[0] < -ran:
            self.xy[0] = -ran
        if self.xy[0] > ran:
            self.xy[0] = ran
        if self.xy[1] < -ran:
            self.xy[1] = -ran
        if self.xy[1] > ran:
            self.xy[1] = ran
        self.rect = self.surf.get_rect(
            center=(
                self.playmod.rect.centerx+self.xy[0],
                self.playmod.rect.centery+self.xy[1],
            )
        )
def makemap(map=[]):#,tiles=[]): # Tworzy mapę
    for i in range(len(map)):
        for j in range(len(map[i])):
            map[i][j] =tile()
            map[i][j].rect=((20*i,20*j))
            r=random.randint(0, 100)
            map[i][j].surf.fill((100+r, 100+r, 100+r))
            map[i][j].rigity=r/100
            tiles.add(map[i][j])
    return map
                
def game():     # Funkcja cyklu gry
    rungame=True
    screen.fill((0,0,0))
    mousestate="brak"
    ADDENEMY = pygame.USEREVENT + 1     # ogłasza event
    pygame.time.set_timer(ADDENEMY, 1800)
    mapa = [[0 for i in range(35)] for j in range(35)]  # Tworzy mapę
    mapa=makemap(mapa)
    wave=0
    waveorder=[0,0]
    wavetroops=[0,0]
    fill=filler()                                       # Filler
    fill.rect.right=W
    fill.rect.bottom=H
    moni=1000               # Startowe pieniądze
    enemies = pygame.sprite.Group()     # Grupa przeciwników
    allunits = pygame.sprite.Group()    # Grupa wszystkich jednostek
    player = Player(mapa,allunits)   # Inicjuje gracza
    player.rect.x = 340
    player.rect.y = 340
    marker=Marker(player)   # Inicjuje celownik
    marker.rect.x = 330
    marker.rect.y = 330
    allunits.add(player)
    playteam = pygame.sprite.Group()    # Grupa sojuszniczych npc
    playergroup = pygame.sprite.Group() # Grupa sojusznicza
    playergroup.add(player)
    bw=200                      # szerokosć przycisków
    bh=80                       # wysokosć przycisków
    font = pygame.font.SysFont(None, 40)
    #moncount = font.render(str(moni), True, (255, 0, 0))
    butgm=Buttons.Button()                              # przycisk G menu 
    butin=Buttons.Button()                              # przycisk produkcji
    butwv=Buttons.Button()                              # przycisk fali
    butgm.create_button(screen, (50,50,250), (W-bw), (H-(bh*(1))), bw, bh, 0, "Menu", (0,0,0))    #rysuje przycisk gry
    butwv.create_button(screen, (50,50,250), (W-bw), (H-(bh*(2))), bw, bh, 0, "Następna fala", (0,0,0))    #rysuje przycisk gry
    butin.create_button(screen, (50,50,250), (W-bw), (H-(bh*(3))), bw, bh, 0, "Piechota 100", (0,0,0))    #rysuje przycisk gry
    
    #print("game")
    while rungame:      # Cykle gry
        troopleft=waveorder[0]-wavetroops[0]
        moncount = font.render(str(moni), True, (255, 0, 0))
        wavecount = font.render("Fala "+str(wave)+" | "+str(troopleft)+" nadchodzi", True, (255, 0, 0))
        hpcount = font.render(str(int(player.hp)), True, (255, 0, 0))
        mtext=mousestate
        if mtext!="brak" and mtext!="produkcja":
            mtext="rozkazy"
        mousecount = font.render(mtext, True, (255, 0, 0))
        rtime=player.timer-pygame.time.get_ticks()
        if rtime>0:
            rcount=str(int(rtime/100))
        else:
            rcount="OGNIA"
        rcount = font.render(rcount, True, (255, 0, 0))
        for event in pygame.event.get():                # Zarządza zdarzeniami
            if event.type == pygame.QUIT:
                rungame = False
            if event.type == KEYDOWN:#escape
                if event.key == K_ESCAPE:
                    rungame = False
                if event.key == K_SPACE and pygame.time.get_ticks()>player.timer and player.hp>0: # Artyleria
                    player.timer=pygame.time.get_ticks()+player.reload
                    inacx=random.randint(-10, 10)
                    inacy=random.randint(-10, 10)
                    postm=marker.rect.center
                    for entity in allunits:
                        poste=entity.rect.center
                        dist=math.sqrt(pow(postm[0]-poste[0]+inacx,2)+pow(postm[1]-poste[1]+inacy,2))
                        if dist < player.spread:
                            dmg=player.damage*math.sqrt(1 - dist/player.spread)
                            entity.hp=entity.hp-dmg
                            #print(dmg)
            elif event.type == ADDENEMY:                          # Create the new enemy and add it to sprite groups
                #print(wavetroops[0])
                if troopleft>0:
                    new_enemy = Enemy(mapa,allunits)
                    r=random.randint(1, 4)
                    #print(r)
                    if r==1:
                        spos=[H-10,random.randint(10, H-10)]
                    elif r==2:
                        spos=[10,random.randint(10, H-10)]
                    elif r==3:
                        spos=[random.randint(10, H-10),10]
                    elif r==4:
                        spos=[random.randint(10, H-10),H-10]
                    new_enemy.rect = new_enemy.surf.get_rect(
                        center=(
                            spos[0],
                            spos[1],
                        )
                    )
                    if not pygame.sprite.spritecollideany(new_enemy, allunits):
                        enemies.add(new_enemy)
                        allunits.add(new_enemy)
                        wavetroops[0]=wavetroops[0]+1
                
                
            if event.type == pygame.MOUSEBUTTONDOWN:          # Nacinięcie myszki
                x=pygame.mouse.get_pos()
                if butgm.pressed(pygame.mouse.get_pos()):      # Przycisk resetu               
                    rungame=False
                    #del butmg
                    mainmenu()
                if butwv.pressed(pygame.mouse.get_pos()):      # Przycisk fali 
                    field=0
                    for entity in enemies:       #jatka
                        field=field+1
                    if field==0 and troopleft==0:
                        wave=wave+1
                        waveorder[0]=waveorder[0]+wave*5
                        moni=moni+wave*200
                        for entity in playteam:       #jatka
                            entity.hp=entity.maxhp
                elif butin.pressed(pygame.mouse.get_pos()):    # Przycisk prod inf  
                    if mousestate=="produkcja":
                        mousestate="brak"
                    else:
                        mousestate="produkcja"
                elif x[0]<700 and moni>=100 and mousestate=="produkcja":            # Stawia piechote
                    moni=moni-100
                    mousestate="brak"
                    new_frien=Enemy(mapa,allunits)
                    new_frien.surf = pinf.convert()
                    new_frien.surf.set_colorkey((255, 255, 255))
                    new_frien.rect.center = (x[0],x[1])
                    new_frien.target = (x[0],x[1])
                    if not pygame.sprite.spritecollideany(new_frien, allunits):
                        playergroup.add(new_frien)
                        playteam.add(new_frien)
                        allunits.add(new_frien)
                    else:
                        moni=moni+100
                else:
                    a=0
                    for entity in playteam:
                        if entity.rect.collidepoint(event.pos):
                            mousestate=entity
                            a=1
                    if a==0 and mousestate!="brak" and mousestate!="produkcja":
                        mousestate.target=(x[0],x[1])
                        mousestate="brak"
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
        postg=player.rect.center
        for entity in enemies:       #jatka
            poste=entity.rect.center
            distg=math.sqrt(pow(postg[0]-poste[0],2)+pow(postg[1]-poste[1],2))
            if distg<=entity.range*20 and pygame.time.get_ticks()>entity.timer and player.hp>0:#celuje w gracza
                entity.timer=pygame.time.get_ticks()+entity.reload
                player.hp=player.hp-entity.damage
            for fren in playteam:   # pomiedzy npc
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
        screen.blit(marker.surf, marker.rect)   # celownik
        screen.blit(fill.surf, fill.rect)       # filler
        screen.blit(moncount, (W-300,0))        # wyswietla text
        screen.blit(hpcount, (W-300,40))        # wyswietla text
        screen.blit(rcount, (W-300,80))        # wyswietla text
        screen.blit(mousecount, (W-300,120))        # wyswietla text
        screen.blit(wavecount, (W-300,160))        # wyswietla text
        butgm.create_button(screen, (50,50,250), (W-bw), (H-(bh*(1))), bw, bh, 0, "Menu", (0,0,0))    #rysuje przycisk gry
        butwv.create_button(screen, (50,50,250), (W-bw), (H-(bh*(2))), bw, bh, 0, "Następna fala", (0,0,0))    #rysuje przycisk gry
        butin.create_button(screen, (50,50,250), (W-bw), (H-(bh*(3))), bw, bh, 0, "Piechota 100", (0,0,0))    #rysuje przycisk gry
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
        clock.tick(30)# fps
        pygame.display.flip()

W=1000                                  # Szerokoć okna
H=700                                   # Wysokoć okna
krol=pygame.image.load("krol.png")      # Ładuje spite'y
marker=pygame.image.load("marker.png")
eninf=pygame.image.load("eninf.png")
pinf=pygame.image.load("pinf.png")
entank=pygame.image.load("entank.png")
ptank=pygame.image.load("ptank.png")
tiles = pygame.sprite.Group()           # Grupa terenu
clock = pygame.time.Clock()#Dla ustawiania fps
fontm = pygame.font.SysFont(None, 40)
#tmq = 'TRUP'#text
#tmqi = fontm.render(tmq, True, (255, 0, 0))
screen = pygame.display.set_mode([W, H])
pygame.display.set_caption("Król Wzgórza")
running = True
mainmenu()
pygame.quit()