import pygame
import time

timer = time.time()

pygame.init()
fenetreLargeur =1280# 1720 #1280 
fenetreHauteur = 720  #  1000 #720  
screen = pygame.display.set_mode((fenetreLargeur, fenetreHauteur))
clock = pygame.time.Clock()
running = True

class Square:
    def __init__(self):
        self.player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.axis_x,self.axis_y = 1,0
        self.vitesse = 1

    def draw(self):
        pygame.draw.circle(screen, "white", self.player_pos, 5)
        
    def move(self):
        self.collidej1 = self.collision(j1)
        self.collidej2 = self.collision(j2)
        if self.collidej2: 
            self.axis_x = -1

        if self.collidej1: 
            self.axis_x = 1

        if self.player_pos.x >= fenetreLargeur:
            j1.score += 1

        elif self.player_pos.x <= 0:
            j2.score += 1

        if self.player_pos.y <= 0:
            self.axis_y = 1

        elif self.player_pos.y >= fenetreHauteur:  
            self.axis_y = -1

        self.player_pos.x += self.axis_x*self.vitesse
        self.player_pos.y += self.axis_y*self.vitesse

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
        self.rect = (fenetreLargeur*x, fenetreHauteur//2-fenetreLargeur//100, fenetreLargeur//200, fenetreHauteur//25)
        self.score = 0
    def draw(self):
        pygame.draw.rect(screen,"white",self.rect)


s = Square()
j1 = Player(0.1)
j2 = Player(0.9)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    
    s.draw()
    if time.time() - timer > 0.1:
        s.move()
        #timer = time.time()
    j1.draw()
    j2.draw()
    pygame.display.flip()
