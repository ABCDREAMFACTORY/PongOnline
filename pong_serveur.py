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
font = pygame.font.Font("assets/NotoSans-Bold.ttf",  screen.get_width()//40)
pygame.display.set_caption("Pong")
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


def restart(afficher=None):
    screen.fill("black")
    j1.rect = [fenetreLargeur*0.1-fenetreLargeur/200, fenetreHauteur/2, fenetreLargeur/200, fenetreHauteur/15]
    j2.rect = [fenetreLargeur*0.9, fenetreHauteur/2, fenetreLargeur/200, fenetreHauteur/15]
    s.__init__()
    j1.draw()
    j2.draw()
    s.draw()
    if afficher != None:
        screen.blit(afficher, (20,20))
    pygame.display.flip()
    if afficher != None:
        time.sleep(1)

class Menu:
    def __init__(self):
        self.titre = font.render("PONG",True,"white")
        self.button_play = Button(fenetreLargeur/2-fenetreLargeur/20,fenetreHauteur*0.3,fenetreLargeur/10,fenetreHauteur/15,"white","Jouer seul",(0,0,0))
        self.button_play_lan = Button(fenetreLargeur/2-fenetreLargeur/20,fenetreHauteur*0.4,fenetreLargeur/10,fenetreHauteur/15,"white","Jouer en lan",(0,0,0),20)
        self.button_option = Button(fenetreLargeur/2-fenetreLargeur/20,fenetreHauteur*0.5,fenetreLargeur/10,fenetreHauteur/15,"white","Options",(0,0,0))
        self.ouvert = True
    def load(self):
        screen.fill("black")
        screen.blit(self.titre,(fenetreLargeur/2-self.titre.get_width()/2,0))
        self.button_play.draw()
        self.button_play_lan.draw()
        self.button_option.draw()

class Menu_Options:
    def __init__(self):
        self.titre = font.render("Options",True,"white")
        self.descip = font.render("ip",True,"white")
        self.input_ip = InputBox(fenetreLargeur/2-fenetreLargeur/20,fenetreHauteur*0.2,fenetreLargeur/10,fenetreHauteur/15,"Test")
        self.back = Button(fenetreLargeur/2-fenetreLargeur/20,fenetreHauteur*0.3,fenetreLargeur/10,fenetreHauteur/15,"white","Quitter","black")
        self.ouvert = False
    def load(self):
        screen.fill("black")
        screen.blit(self.titre,(fenetreLargeur/2-self.titre.get_width()/2,0))
        screen.blit(self.descip,(self.input_ip.rect.x-self.descip.get_width(),self.input_ip.rect.y))
        self.input_ip.update()
        self.input_ip.draw()
        self.input_ip.handle_event(event)
        self.back.draw()

class Button:
    def __init__(self,x,y,width,height,color,text = None,text_color = (255,255,255),taille = 25):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color
        self.taille_text = pygame.font.Font("assets/NotoSans-Bold.ttf", taille)
        self.text = self.taille_text.render(text, 1,text_color)
    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect)
        screen.blit(self.text,(self.rect.x,self.rect.y))
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = "white"
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False

    def handle_event(self,event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if self.rect.collidepoint(event.pos):
                    # Toggle the active variable.
                    self.active = True
                else:
                    self.active = False
                # Change the current color of the input box.
                self.color = "orange" if self.active else (255,255,255)
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        print(self.text)
                        self.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                    # Re-render the text.
                    self.txt_surface = font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

s = Square()
j1 = Player(0.1)
j2 = Player(0.9)
menu_list = [Menu(),Menu_Options()]
game = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_co = pygame.mouse.get_pos()
            if menu_list[0].ouvert == True:
                if menu_list[0].button_play.rect.collidepoint(pygame.mouse.get_pos()):
                    game = True
                    menu_list[0].ouvert = False
                if menu_list[0].button_option.rect.collidepoint(pygame.mouse.get_pos()):
                    menu_list[0].ouvert = False
                    menu_list[1].ouvert = True
            if menu_list[1].ouvert == True:
                if menu_list[1].back.rect.collidepoint(pygame.mouse.get_pos()):
                    menu_list[1].ouvert = False
                    menu_list[0].ouvert = True
        if menu_list[1].ouvert == True:
            menu_list[1].input_ip.handle_event(event)
            
    if menu_list[0].ouvert == True:
        menu_list[0].load()
    if menu_list[1].ouvert == True:
        menu_list[1].load()
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
        if keys[pygame.K_ESCAPE]:
            restart()
            game = False
            menu_list[0].ouvert = True
            #timer = time.time()
        s.draw()
        s.move(delta_time)
        j1.draw()
        j2.draw()
    pygame.display.flip()
    clock.tick(60)
