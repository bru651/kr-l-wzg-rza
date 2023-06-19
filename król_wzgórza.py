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
class filler(pygame.sprite.Sprite):# Filler boczny
    def __init__(self):
        super(filler, self).__init__()
        self.surf = pygame.Surface((300, H))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
class tile(pygame.sprite.Sprite):# Pola terenu
    def __init__(self):
        super(tile, self).__init__()
        self.surf = pnplain.convert()
        self.surf.set_colorkey((0, 0, 0))
        #self.surf = bomber.convert()
        #self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rigity=0.2
        self.cover=0
class hills(tile):# Pola terenu
    def __init__(self):
        super(hills, self).__init__()
        self.surf = pnhill.convert()
        self.surf.set_colorkey((0, 0, 0))
        #self.surf = bomber.convert()
        #self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rigity=0.35
        self.cover=0
class forest(tile):# Pola terenu
    def __init__(self):
        super(forest, self).__init__()
        self.surf = pnforest.convert()
        self.surf.set_colorkey((0, 0, 0))
        #self.surf = bomber.convert()
        #self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rigity=0.45
        self.cover=0
class mount(tile):# Pola terenu
    def __init__(self):
        super(mount, self).__init__()
        self.surf = pnmount.convert()
        self.surf.set_colorkey((0, 0, 0))
        #self.surf = bomber.convert()
        #self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rigity=0.9
        self.cover=0
class m_f(tile):# Pola terenu
    def __init__(self):
        super(m_f, self).__init__()
        self.surf = pnm_f.convert()
        self.surf.set_colorkey((0, 0, 0))
        #self.surf = bomber.convert()
        #self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rigity=0.7
        self.cover=0
class road(tile):# Pola terenu
    def __init__(self):
        super(road, self).__init__()
        self.surf = pnroad.convert()
        self.surf.set_colorkey((0, 0, 0))
        #self.surf = bomber.convert()
        #self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rigity=0
        self.cover=0
class city(tile):# Pola terenu
    def __init__(self):
        super(city, self).__init__()
        self.surf = pncity.convert()
        self.surf.set_colorkey((0, 0, 0))
        #self.surf = bomber.convert()
        #self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rigity=0
        self.cover=0
class effect(pygame.sprite.Sprite):# efekt
    def __init__(self):
        super(effect, self).__init__()
        self.surf = fl.convert()
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect()
        self.duration=100
        self.timer=0
        self.birth=pygame.time.get_ticks()
    def update(self):
        self.timer=pygame.time.get_ticks()
        if self.timer-self.birth>self.duration:
            self.kill()
class symbol(pygame.sprite.Sprite):# symbol
    def __init__(self):
        super(symbol, self).__init__()
        self.surf = pnhp.convert()
        self.surf.set_colorkey((255, 255, 255))
class Player(pygame.sprite.Sprite):     # Klasa grzacza
    def __init__(self,inmap,anyun):
        super(Player, self).__init__()
        self.surf = krol.convert()
        self.surf.set_colorkey((255, 255, 255))
        self.inmap=inmap
        self.rect = self.surf.get_rect()
        self.timer=0
        self.reload=2000
        self.speed=4
        self.q=0.5
        self.maxhp=10
        self.hp=self.maxhp
        self.inacuracy=40
        self.range=160
        self.spread=40
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
        self.sprite=eninf
        self.hid=False
        self.state=0
        self.surf = self.sprite.convert()
        self.surf.set_colorkey((255, 255, 255))
        self.inmap=inmap
        self.rect = self.surf.get_rect(
            center=(
                0,
                0,
            )
        )
        self.timer=0
        self.reload=2000
        self.stancetimer=0
        self.stance_t=2000
        self.speed=2
        self.q=0.25                 # Jak bardzo teren wpływa na jednostkę
        self.maxhp=5
        self.hp=self.maxhp
        self.range=3
        self.damage=2
        self.anyun=anyun            # grupa jednostek
        self.target=[350,350]
        #self.rect=((300,300))
    def decision(self):             # pathfinding
        tg=self.target
        xy=[self.rect.centerx,self.rect.centery]
        if abs(tg[0]-xy[0])<10 and abs(tg[1]-xy[1])<10:
            self.state=0
        elif xy[0]<tg[0]-9:#prawo
            self.state=4
            self.hid=False
            temp=pygame.transform.rotate(self.sprite,270)
            self.surf = temp.convert()
            self.surf.set_colorkey((255, 255, 255))
        elif xy[0]>tg[0]+9:#lewo
            self.state=3
            self.hid=False
            temp=pygame.transform.rotate(self.sprite,90)
            self.surf = temp.convert()
            self.surf.set_colorkey((255, 255, 255))
        elif xy[1]<tg[1]+9:#down
            self.state=2
            self.hid=False
            temp=pygame.transform.rotate(self.sprite,180)
            self.surf = temp.convert()
            self.surf.set_colorkey((255, 255, 255))
        elif xy[1]>tg[1]-9:#up
            self.state=1
            self.hid=False
            temp=pygame.transform.rotate(self.sprite,0)
            self.surf = temp.convert()
            self.surf.set_colorkey((255, 255, 255))
        if self.stancetimer>pygame.time.get_ticks():
            self.state=0
        
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
class apc(Enemy):# Pola terenu
    def __init__(self,inmap,anyun):
        super(apc, self).__init__(inmap,anyun)
        self.sprite=eapc
        self.hid=False
        self.state=0
        self.surf = self.sprite.convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                0,
                0,
            )
        )
        self.timer=0
        self.reload=3000
        self.stancetimer=0
        self.stance_t=1500
        self.speed=6
        self.q=0.9                 # Jak bardzo teren wpływa na jednostkę
        self.maxhp=8
        self.hp=self.maxhp
        self.range=4
        self.damage=4
class tank(Enemy):# Pola terenu
    def __init__(self,inmap,anyun):
        super(tank, self).__init__(inmap,anyun)
        self.sprite=etank
        self.hid=False
        self.state=0
        self.surf = self.sprite.convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                0,
                0,
            )
        )
        self.timer=0
        self.reload=6000
        self.stancetimer=0
        self.stance_t=1000
        self.speed=5
        self.q=0.65                 # Jak bardzo teren wpływa na jednostkę
        self.maxhp=15
        self.hp=self.maxhp
        self.range=5
        self.damage=10
def makemap(map=[]):#,tiles=[]): # Tworzy mapę
    for i in range(len(map)):
        for j in range(len(map[i])):
            rh=random.randint(0, 100)+j*3-20
            rw=random.randint(0, 100)+i*3-20
            if i==17 and j==17:
                map[i][j] =city()
            elif abs(i-17)==3 or abs(j-17)==3:
                map[i][j] =road()
            elif rh>150:
                map[i][j] =mount()
            elif rh>120 and rw>110:
                map[i][j] =m_f()
            elif rh>120:
                map[i][j] =hills()
            elif rw>110:
                map[i][j] =forest()
            else:
                map[i][j] =tile()
            map[i][j].rect=((20*i,20*j))
            tiles.add(map[i][j])
    return map
def firework(x,y,group,spread=50,b=False):                # efekt
          fire=effect()
          if b==False:
              fire.rect.centerx=x+random.randint(-9, 9)
              fire.rect.centery=y+random.randint(-9, 9)
          else:
              fire.surf=pygame.transform.scale(fire.surf, (spread, spread))
              fire.rect.centerx=x+(spread/20)-20
              fire.rect.centery=y+(spread/20)-20
          group.add(fire)
def wymianaognia(entity,victim,distg,egroup,p):             #jatka
    if distg<=entity.range*20:   #celuje
        if entity.state==0:
            if pygame.time.get_ticks()>entity.timer:
                entity.timer=pygame.time.get_ticks()+entity.reload
                entity.stancetimer=entity.stancetimer+entity.reload
                victim.hp=victim.hp-entity.damage
                #firework(victim.rect.centerx, victim.rect.centery, egroup)
                #fire=effect()
                #fire.rect.centerx=victim.rect.centerx+random.randint(-9, 9)
                #fire.rect.centery=victim.rect.centery+random.randint(-9, 9)
                #effects.add(fire)
                if entity.hid==True:
                    victim.timer=pygame.time.get_ticks()+entity.stance_t
                    entity.hid=False
                    print("szok")
        else:
            entity.stancetimer=pygame.time.get_ticks()+entity.stance_t
            entity.timer=pygame.time.get_ticks()+entity.stance_t
            entity.state=0
def upgrademenu(player,moni):                  # menu ulepszeń
    runningum=True
    screen.fill((0,0,0))
    #butmq.surface.kill()
    butuq=Buttons.Button()                              # przycisk UM wyjscie 
    hpscb=Buttons.Button()                              # przycisk UM wyjscie 
    speedscb=Buttons.Button()                              # przycisk UM wyjscie 
    damagescb=Buttons.Button()                              # przycisk UM wyjscie 
    rangescb=Buttons.Button()                              # przycisk UM wyjscie 
    inacscb=Buttons.Button()                              # przycisk UM wyjscie 
    spreadscb=Buttons.Button()                              # przycisk UM wyjscie 
    firespeedscb=Buttons.Button()                              # przycisk UM wyjscie 
    fontu = pygame.font.SysFont(None, 40)
    hps = fontu.render("Maksymalne życie", True, (255, 0, 0))
    speeds = fontu.render("Szybkość", True, (255, 0, 0))
    damages = fontu.render("Obrażenia", True, (255, 0, 0))
    ranges = fontu.render("Zasięg", True, (255, 0, 0))
    inacs = fontu.render("Niecelnoć", True, (255, 0, 0))
    spreads = fontu.render("Obszar rażenia", True, (255, 0, 0))
    firespeeds = fontu.render("Czas przeładowania", True, (255, 0, 0))
    bw=300                      # szerokosć przycisków
    bh=80                       # wysokosć przycisków
    butuq.create_button(screen, (50,50,250), W-bh, H-bh, bh, bh, 0, "X", (0,0,0))    #rysuje przycisk wyjscia
    hpscb.create_button(screen, (50,50,250), W-bw, bh*0, bw, bh, 0, "+1 (100)", (0,0,0))
    speedscb.create_button(screen, (50,50,250), W-bw, bh*1, bw, bh, 0, "+1 (200)", (0,0,0))
    damagescb.create_button(screen, (50,50,250), W-bw, bh*2, bw, bh, 0, "+1 (200)", (0,0,0))
    rangescb.create_button(screen, (50,50,250), W-bw, bh*3, bw, bh, 0, "+10 (300)", (0,0,0))
    inacscb.create_button(screen, (50,50,250), W-bw, bh*4, bw, bh, 0, "-4 (300)", (0,0,0))
    spreadscb.create_button(screen, (50,50,250), W-bw, bh*5, bw, bh, 0, "+5 (200)", (0,0,0))
    firespeedscb.create_button(screen, (50,50,250), W-bw, bh*6, bw, bh, 0, "-100 (250)", (0,0,0))
    ms=symbol()
    ms.surf = pnmoni.convert()
    ms.surf.set_colorkey((255, 255, 255))
    while runningum:
        hpsc = fontu.render(str(player.maxhp), True, (255, 0, 0))
        speedsc = fontu.render(str(player.speed), True, (255, 0, 0))
        damagesc = fontu.render(str(player.damage), True, (255, 0, 0))
        rangesc = fontu.render(str(player.range), True, (255, 0, 0))
        inacsc = fontu.render(str(player.inacuracy), True, (255, 0, 0))
        spreadsc = fontu.render(str(player.spread), True, (255, 0, 0))
        monic = fontu.render(str(moni), True, (255, 0, 0))
        firespeedsc = fontu.render(str(player.reload), True, (255, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningum = False
            if event.type == KEYDOWN:#escape
                if event.key == K_ESCAPE:
                    runningum = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if butuq.pressed(pygame.mouse.get_pos()):# Przycisk wyjcia
                    runningum=False
                if hpscb.pressed(pygame.mouse.get_pos()):# Przycisk kupna
                    if moni>=100:
                        moni=moni-100
                        player.maxhp=player.maxhp+1
                if speedscb.pressed(pygame.mouse.get_pos()):# Przycisk kupna
                    if moni>=200:
                        moni=moni-200
                        player.speed=player.speed+1
                if damagescb.pressed(pygame.mouse.get_pos()):# Przycisk kupna
                    if moni>=200:
                        moni=moni-200
                        player.damage=player.damage+1
                if rangescb.pressed(pygame.mouse.get_pos()):# Przycisk kupna
                    if moni>=300:
                        moni=moni-300
                        player.range=player.range+10
                if inacscb.pressed(pygame.mouse.get_pos()):# Przycisk kupna
                    if moni>=300 and player.inacuracy>0:
                        moni=moni-300
                        player.inacuracy=player.inacuracy-4
                if spreadscb.pressed(pygame.mouse.get_pos()):# Przycisk kupna
                    if moni>=200:
                        moni=moni-200
                        player.spread=player.spread+5
                if firespeedscb.pressed(pygame.mouse.get_pos()):# Przycisk kupna
                    if moni>=250 and player.reload>0:
                        moni=moni-250
                        player.reload=player.reload-100
        screen.fill((50,50,50))
        screen.blit(hps, (0,bh*0))        # wyswietla text
        screen.blit(speeds, (0,bh*1))        # wyswietla text
        screen.blit(damages, (0,bh*2))        # wyswietla text
        screen.blit(ranges, (0,bh*3))        # wyswietla text
        screen.blit(inacs, (0,bh*4))        # wyswietla text
        screen.blit(spreads, (0,bh*5))        # wyswietla text
        screen.blit(firespeeds, (0,bh*6))        # wyswietla text
        #
        screen.blit(hpsc, (W/2,bh*0))        # wyswietla text
        screen.blit(speedsc, (W/2,bh*1))        # wyswietla text
        screen.blit(damagesc, (W/2,bh*2))        # wyswietla text
        screen.blit(rangesc, (W/2,bh*3))        # wyswietla text
        screen.blit(inacsc, (W/2,bh*4))        # wyswietla text
        screen.blit(spreadsc, (W/2,bh*5))        # wyswietla text
        screen.blit(firespeedsc, (W/2,bh*6))        # wyswietla text
        
        screen.blit(ms.surf, (30,H-30))
        screen.blit(monic, (50,H-30))
        butuq.create_button(screen, (50,50,250), W-bh, H-bh, bh, bh, 0, "X", (0,0,0))    #rysuje przycisk wyjscia
        #
        hpscb.create_button(screen, (50,50,250), W-bw, bh*0, bw, bh, 0, "+1 (100)", (0,0,0))
        speedscb.create_button(screen, (50,50,250), W-bw, bh*1, bw, bh, 0, "+1 (200)", (0,0,0))
        damagescb.create_button(screen, (50,50,250), W-bw, bh*2, bw, bh, 0, "+1 (200)", (0,0,0))
        rangescb.create_button(screen, (50,50,250), W-bw, bh*3, bw, bh, 0, "+10 (300)", (0,0,0))
        inacscb.create_button(screen, (50,50,250), W-bw, bh*4, bw, bh, 0, "-4 (300)", (0,0,0))
        spreadscb.create_button(screen, (50,50,250), W-bw, bh*5, bw, bh, 0, "+5 (200)", (0,0,0))
        firespeedscb.create_button(screen, (50,50,250), W-bw, bh*6, bw, bh, 0, "-100 (250)", (0,0,0))
        clock.tick(30)# fps
        pygame.display.flip()  
    return moni
def game():     # Funkcja cyklu gry
    rungame=True
    screen.fill((0,0,0))
    lost=False
    mousestate="brak"
    produkcja=0
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
    effects = pygame.sprite.Group()    # Grupa effektów
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
    fontL = pygame.font.SysFont(None, 80)
    #moncount = font.render(str(moni), True, (255, 0, 0))
    butgm=Buttons.Button()                              # przycisk G menu 
    butin=Buttons.Button()                              # przycisk produkcji
    butapc=Buttons.Button()                              # przycisk produkcji
    buttank=Buttons.Button()                              # przycisk produkcji
    butwv=Buttons.Button()                              # przycisk fali
    butwu=Buttons.Button()                              # przycisk ulepszeń
    butgm.create_button(screen, (50,50,250), (W-bw*6/5), (H-(bh*(1))), bw, bh, 0, "Menu", (0,0,0))    #rysuje przycisk gry
    butwv.create_button(screen, (50,50,250), (W-bw*6/5), (H-(bh*(2))), bw, bh, 0, "Następna fala", (0,0,0))    #rysuje przycisk gry
    butwu.create_button(screen, (50,50,250), (W-bw*6/5), (H-(bh*(3))), bw, bh, 0, "Ulepszenia", (0,0,0))    #rysuje przycisk ulepszeń
    butin.create_button(screen, (50,50,250), (W-bw*6/5), (H-(bh*(4))), bw, bh, 0, "Piechota 100", (0,0,0))    #rysuje przycisk pp
    butapc.create_button(screen, (50,50,250), (W-bw*6/5), (H-(bh*(5))), bw, bh, 0, "APC 400", (0,0,0))    #rysuje przycisk pa
    buttank.create_button(screen, (50,50,250), (W-bw*6/5), (H-(bh*(6))), bw, bh, 0, "Czołg 1000", (0,0,0))    #rysuje przycisk pt
    hps=symbol()                    # Symbole
    ts=symbol()
    ts.surf = pntimer.convert()
    ts.surf.set_colorkey((255, 255, 255))
    ms=symbol()
    ms.surf = pnmoni.convert()
    ms.surf.set_colorkey((255, 255, 255))
    lostmessage = fontL.render("PREGRAŁEŚ", True, (255, 0, 0))
    #print("game")
    while rungame:      # Cykle gry
        troopleft=waveorder[0]-wavetroops[0]
        field=0
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
                    inacx=random.randint(-player.inacuracy, player.inacuracy)
                    inacy=random.randint(-player.inacuracy, player.inacuracy)
                    postm=marker.rect.center
                    firework(postm[0]+inacx, postm[1]+inacy, effects, player.spread,True)
                    for entity in allunits:
                        poste=entity.rect.center
                        dist=math.sqrt(pow(postm[0]-poste[0]+inacx,2)+pow(postm[1]-poste[1]+inacy,2))
                        if dist < player.spread:
                            dmg=player.damage*math.sqrt(1 - dist/player.spread)
                            entity.hp=entity.hp-dmg
                            #print(dmg)
            elif event.type == ADDENEMY:                          # Dodanie przeciwników
                #print(wavetroops[0])
                if troopleft>0:
                    rt=random.randint(0, 20)
                    if rt>18:
                        new_enemy = tank(mapa,allunits)
                    elif rt>14:
                        new_enemy = apc(mapa,allunits)
                    else:
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
                    for entity in enemies:       #liczy przeciwników
                        field=field+1
                    if field==0 and troopleft==0:
                        wave=wave+1
                        waveorder[0]=waveorder[0]+wave*5
                        moni=moni+wave*100
                        player.hp=player.maxhp
                        for entity in playteam:       #regeneracja
                            entity.hp=entity.maxhp
                elif butin.pressed(pygame.mouse.get_pos()):    # Przycisk prod inf  
                    produkcja=0
                    if mousestate=="produkcja":
                        mousestate="brak"
                    else:
                        mousestate="produkcja"
                elif butapc.pressed(pygame.mouse.get_pos()):    # Przycisk prod apc  
                    produkcja=1
                    if mousestate=="produkcja":
                        mousestate="brak"
                    else:
                        mousestate="produkcja"
                elif buttank.pressed(pygame.mouse.get_pos()):    # Przycisk prod tank  
                    produkcja=2
                    if mousestate=="produkcja":
                        mousestate="brak"
                    else:
                        mousestate="produkcja"
                elif butwu.pressed(pygame.mouse.get_pos()):    # Przycisk ulepszeń
                    moni=upgrademenu(player,moni)
                elif x[0]<700 and moni>=100 and mousestate=="produkcja" and produkcja==0:            # Stawia piechote
                    moni=moni-100
                    mousestate="brak"
                    new_frien=Enemy(mapa,allunits)
                    new_frien.sprite = pinf
                    new_frien.surf = new_frien.sprite.convert()
                    new_frien.surf.set_colorkey((255, 255, 255))
                    new_frien.rect.center = (x[0],x[1])
                    new_frien.target = (x[0],x[1])
                    if not pygame.sprite.spritecollideany(new_frien, allunits):
                        playergroup.add(new_frien)
                        playteam.add(new_frien)
                        allunits.add(new_frien)
                        if field==0 and troopleft==0:
                            new_frien.hid=True
                    else:
                        moni=moni+100
                elif x[0]<700 and moni>=400 and mousestate=="produkcja" and produkcja==1:            # Stawia apc
                    moni=moni-400
                    mousestate="brak"
                    new_frien=apc(mapa,allunits)
                    new_frien.sprite = papc
                    new_frien.surf = new_frien.sprite.convert()
                    new_frien.surf.set_colorkey((255, 255, 255))
                    new_frien.rect.center = (x[0],x[1])
                    new_frien.target = (x[0],x[1])
                    if not pygame.sprite.spritecollideany(new_frien, allunits):
                        playergroup.add(new_frien)
                        playteam.add(new_frien)
                        allunits.add(new_frien)
                        if field==0 and troopleft==0:
                            new_frien.hid=True
                    else:
                        moni=moni+400
                elif x[0]<700 and moni>=1000 and mousestate=="produkcja" and produkcja==2:            # Stawia czołg
                    moni=moni-1000
                    mousestate="brak"
                    new_frien=tank(mapa,allunits)
                    new_frien.sprite = ptank
                    new_frien.surf = new_frien.sprite.convert()
                    new_frien.surf.set_colorkey((255, 255, 255))
                    new_frien.rect.center = (x[0],x[1])
                    new_frien.target = (x[0],x[1])
                    if not pygame.sprite.spritecollideany(new_frien, allunits):
                        playergroup.add(new_frien)
                        playteam.add(new_frien)
                        allunits.add(new_frien)
                        if field==0 and troopleft==0:
                            new_frien.hid=True
                    else:
                        moni=moni+1000
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
            post=entity.rect.center
            tert=(int(post[0]/20),int(post[1]/20))
            if tert[0]==17 and tert[1]==17:
                lost=True
                player.hp=0
                moni=0
                for fren in playteam:
                    fren.hp=0
            if player.hp>0:                
                distg=math.sqrt(pow(postg[0]-poste[0],2)+pow(postg[1]-poste[1],2))
                wymianaognia(entity, player, distg, player, effects)
            for fren in playteam:   # pomiedzy npc
                postp=fren.rect.center
                dist=math.sqrt(pow(postp[0]-poste[0],2)+pow(postp[1]-poste[1],2))
                wymianaognia(entity, fren, dist, player, effects)
                wymianaognia(fren, entity, dist, player, effects)
        
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
        for entity in effects:
            entity.update()
            screen.blit(entity.surf, entity.rect)
        if player.hp>0:
            screen.blit(marker.surf, marker.rect)   # celownik
        screen.blit(fill.surf, fill.rect)       # filler
        screen.blit(moncount, (W-280,0))        # wyswietla text
        screen.blit(hpcount, (W-280,40))        # wyswietla text
        screen.blit(rcount, (W-280,80))         # wyswietla text
        screen.blit(mousecount, (W-300,120))        # wyswietla text
        screen.blit(wavecount, (W-300,160))        # wyswietla text
        screen.blit(ts.surf, (W-300,80))        # wyswietla symbole
        screen.blit(ms.surf, (W-300,0))
        screen.blit(hps.surf, (W-300,40))
        butgm.create_button(screen, (50,50,250), (W-bw*6/5), (H-(bh*(1))), bw, bh, 0, "Menu", (0,0,0))    #rysuje przycisk gry
        butwv.create_button(screen, (50,50,250), (W-bw*6/5), (H-(bh*(2))), bw, bh, 0, "Następna fala", (0,0,0))    #rysuje przycisk gry
        butwu.create_button(screen, (50,50,250), (W-bw*6/5), (H-(bh*(3))), bw, bh, 0, "Ulepszenia", (0,0,0))    #rysuje przycisk ulepszeń
        butin.create_button(screen, (50,50,250), (W-bw*6/5), (H-(bh*(4))), bw, bh, 0, "Piechota 100", (0,0,0))    #rysuje przycisk pp
        butapc.create_button(screen, (50,50,250), (W-bw*6/5), (H-(bh*(5))), bw, bh, 0, "APC 400", (0,0,0))    #rysuje przycisk pa
        buttank.create_button(screen, (50,50,250), (W-bw*6/5), (H-(bh*(6))), bw, bh, 0, "Czołg 1000", (0,0,0))    #rysuje przycisk pt
        if lost==True:
            screen.blit(lostmessage, (W/4,H/2))         # wyswietla text
        clock.tick(30)# fps
        pygame.display.flip()
def mainmenu():
    runningmm=True
    screen.fill((0,0,0))
    #butmq.surface.kill()
    butmq=Buttons.Button()                              # przycisk MM wyjscie 
    #butmi=Buttons.Button()                              # przycisk MM info 
    butmg=Buttons.Button()                              # przycisk MM graj
    #butmt=Buttons.Button()                              # przycisk MM graj
    bw=300                      # szerokosć przycisków
    bh=80                       # wysokosć przycisków
    fontT = pygame.font.SysFont(None, 150)
    title = fontT.render("KRÓL WZGORZA", True, (50,50,250))
    screen.blit(title, (W/14,bh))        # wyswietla text
    #butmt.create_button(screen, (50,50,250), (W-bw*2)/2, 20, bw*2, bh*2, 0, "KRÓŁ WZGÓRZA", (0,0,0))    #rysuje przycisk gry
    butmg.create_button(screen, (50,50,250), (W-bw)/2, (H-(bh*(0)))/2, bw, bh, 0, "GRAJ", (0,0,0))    #rysuje przycisk gry
    #butmi.create_button(screen, (50,50,250), (W-bw)/2, (H-(bh*(-2)))/2, bw, bh, 0, "INFO", (0,0,0))    #rysuje przycisk informacji
    butmq.create_button(screen, (50,50,250), (W-bw)/2, (H-(bh*(-4)))/2, bw, bh, 0, "WYJDŹ", (0,0,0))    #rysuje przycisk wyjscia
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
                    #del butmi
                    del butmq
                    game()
        clock.tick(30)# fps
        pygame.display.flip()


W=1000                                  # Szerokoć okna
H=700                                   # Wysokoć okna
krol=pygame.image.load("pnking.png")      # Ładuje spite'y
marker=pygame.image.load("marker.png")
eninf=pygame.image.load("pneinf.png")
pinf=pygame.image.load("pnpinf.png")
papc=pygame.image.load("pnfapc.png")
eapc=pygame.image.load("pneapc.png")
ptank=pygame.image.load("pnftank.png")
etank=pygame.image.load("pnetank.png")

fl=pygame.image.load("fl.png")
pnhp=pygame.image.load("pnhp.png")
pnmoni=pygame.image.load("pnmoni.png")
pntimer=pygame.image.load("pntimer.png")
#
pnplain=pygame.image.load("pnplain.png")
pnhill=pygame.image.load("pnhill.png")
pnmount=pygame.image.load("pnmount.png")
pnforest=pygame.image.load("pnforest.png")
pnm_f=pygame.image.load("pnh+f.png")
pnroad=pygame.image.load("pnroadroad.png")
pncity=pygame.image.load("pntown.png")
#
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