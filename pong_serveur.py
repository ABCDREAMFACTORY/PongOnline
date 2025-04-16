import pygame
import time
import random
import math
timer = time.time()
pygame.init()
Plein_écran = True
if Plein_écran:
    fenetreLargeur =1280# 1720 #1280 
    fenetreHauteur = 720  #  1000 #720
else:
    fenetreLargeur =1720# 1720 #1280 
    fenetreHauteur = 1000  #  1000 #720
screen = pygame.display.set_mode((fenetreLargeur, fenetreHauteur))
clock = pygame.time.Clock()
running = True
font = pygame.font.Font("assets/NotoSans-Bold.ttf", 30)

class Square:
    def __init__(self):
        self.player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.axis_x,self.axis_y = 1,random.randint(-1,1)
        self.vitesse = math.hypot(fenetreLargeur,fenetreHauteur)*0.5#(fenetreHauteur+fenetreLargeur)*0.3#fenetreLargeur/5 + fenetreHauteur/5
    def draw(self):
        pygame.draw.circle(screen, "white", self.player_pos, 5)

    def move(self,time):
        self.collidej1 = self.collision(j1)
        self.collidej2 = self.collision(j2)
        if self.collidej2: 
            self.axis_x = -1
            self.axis_y = random.randint(-1,1)
        if self.collidej1: 
            self.axis_x = 1
            self.axis_y = random.randint(-1,1)
        if self.player_pos.x >= fenetreLargeur:
            j1.score += 1
            afficher = font.render(f"score: {j1.score}/{j2.score}", 1,(255,255,255))
            restart(afficher)
        elif self.player_pos.x <= 0:
            j2.score += 1
            afficher = font.render(f"score: {j1.score}/{j2.score}", 1,(255,255,255))
            restart(afficher)
        if self.player_pos.y <= 0:
            self.axis_y = 1

        elif self.player_pos.y >= fenetreHauteur-10:  
            self.axis_y = -1

        self.player_pos.x += self.axis_x*self.vitesse*time
        self.player_pos.y += self.axis_y*self.vitesse*time

    def collision(self,player):
         # Trouve le point le plus proche du centre du cercle sur le rectangle
        closest_x = max(player.rect[0], min(self.player_pos.x,player.rect[0] + player.rect[2]))
        closest_y = max(player.rect[1], min(self.player_pos.y,player.rect[1] + player.rect[3]))
         # Calcul de la distance entre ce point et le centre du cercle
        distance_x = self.player_pos.x - closest_x
        distance_y = self.player_pos.y - closest_y

        distance_squared = distance_x**2 + distance_y**2
        return distance_squared <= 25


class Player:
    def __init__(self,x):
        self.rect = [fenetreLargeur*x, fenetreHauteur/2-fenetreLargeur/100, fenetreLargeur/200, fenetreHauteur/15]
        self.score = 0
        self.vitesse = fenetreHauteur*1#(fenetreHauteur+fenetreLargeur)*0.5
    def draw(self):
        pygame.draw.rect(screen,"white",self.rect)
    def move_up(self,time):
        if self.rect[1] > 0:
            self.rect[1] -= self.vitesse*time
    def move_down(self,time):
        if self.rect[1] < fenetreHauteur-self.rect[3]:
            self.rect[1] += self.vitesse*time


def restart(afficher):
    screen.fill("black")
    j1.rect = [fenetreLargeur*0.1-fenetreLargeur/200, fenetreHauteur/2, fenetreLargeur/200, fenetreHauteur/15]
    j2.rect = [fenetreLargeur*0.9, fenetreHauteur/2, fenetreLargeur/200, fenetreHauteur/15]
    s.__init__()
    j1.draw()
    j2.draw()
    s.draw()
    screen.blit(afficher, (20,20))
    pygame.display.flip()
    time.sleep(1)

class Menu:
    def __init__(self):
        self.titre = font.render("PONG",True,"white")
        self.button_play = [fenetreLargeur/2-fenetreLargeur/20,fenetreHauteur*0.3,fenetreLargeur/10,fenetreHauteur/15]
        self.ouvert = True
    def load(self):
        screen.fill("black")
        screen.blit(self.titre,(fenetreLargeur/2-self.titre.get_width()/2,0))
        pygame.draw.rect(screen,"white",self.button_play)

s = Square()
j1 = Player(0.1)
j2 = Player(0.9)
menu_list = [Menu()]
game = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and menu_list[0].ouvert == True:
            mouse_co = pygame.mouse.get_pos()
            if mouse_co[0] >= menu_list[0].button_play[0] and mouse_co[0] <= menu_list[0].button_play[0] + menu_list[0].button_play[2] and mouse_co[1] >= menu_list[0].button_play[1] and mouse_co[1] <= menu_list[0].button_play[1] + menu_list[0].button_play[3]:
                game = True
                menu_list[0].ouvert = False
    if menu_list[0].ouvert == True:
        menu_list[0].load()
    if game == True:
        screen.fill("black")
        delta_time = clock.tick(60) / 1000.0
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            j1.move_up(delta_time)
        if keys[pygame.K_s]:
            j1.move_down(delta_time)
        if keys[pygame.K_UP]:
            j2.move_up(delta_time)
        if keys[pygame.K_DOWN]:
            j2.move_down(delta_time)

            #timer = time.time()
        s.draw()
        s.move(delta_time)
        j1.draw()
        j2.draw()
    pygame.display.flip()
    clock.tick(60)
