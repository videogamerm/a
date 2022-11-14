import pygame
from pygame.locals import *
import time
# Importing os module
import os
import random
# absolute path
path = os.getcwd()
import glo
# python os path join method
from pygame import mixer
fontspath = os.path.join(path, "fonts")
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
YELLOW = (255,255,0)
pygame.init()

x = 1
def scoreup():
    glo.score +=1
def gameover():
    runfile("ondeath.py")
    exit()
class Coin(pygame.sprite.Sprite):
    def __init__(self, pos,f):
        super().__init__()
        
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        if f == True:
            self.food_x = random.randrange(0, 615, 1)
            self.food_y = random.randrange(0, 615, 1)
            self.rect.topleft = (self.food_x,self.food_y)
        else:
            self.rect.topleft = pos
        
    def update(self):
        if self.rect.colliderect(cube):
            glo.score += 1
            self.food_x = random.randrange(0, 615, 1)
            self.food_y = random.randrange(0, 615, 1)
            self.rect.topleft = (self.food_x,self.food_y)
            self.kill()
class Cube(pygame.sprite.Sprite):
    def __init__():
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("cube.png")
        self.rect = self.image.get_rect()
        self.x = 350
        self.y = 350
        self.rect.topleft = (self.x,self.y)
     
              
class nmy(pygame.sprite.Sprite):

    def __init__(self, pos,f):
        super().__init__()
        
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        if f == True:
            self.food_x = random.randrange(0, 615, 1)
            self.food_y = random.randrange(0, 615, 1)
            self.rect.topleft = (self.food_x,self.food_y)
        else:
            self.rect.topleft = pos
    def update(self):
        opposite = 1
        if self.food_x <=0 :
            opposite = -1
        if self.food_x >=650:
            opposite = 1
        self.food_x = (self.food_x +5 )* opposite 
        if self.rect.colliderect(cube):
            glo.score += 1
            self.food_x = random.randrange(0, 615, 1)
            self.food_y = random.randrange(0, 615, 1)
            self.rect.topleft = (self.food_x,self.food_y)
            gameover()     
            
        
    




window = pygame.display.set_mode((650, 650))
clock = pygame.time.Clock()
bar = 0
background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *background.get_size(), (128, 128, 128), (64, 64, 64)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
[pygame.draw.rect(background, color, rect) for rect, color in tiles]

cube = pygame.Rect(0, 0, 20, 20)
cube.center = window.get_rect().center
cube2 = pygame.Rect(cube.x, cube.y, , height)
speed = 5

font1 = pygame.font.SysFont([os.path.join(fontspath,"LektonCode-Regular.ttf")], 72)

'''mixer.init()
''''''mixer.music.load("Umm.wav")
''''''mixer.music.set_volume(3)
mixer.music.play(loops=99999)'''

# Initialing Color
colore = (0,255,0)
  
# Drawing Rectangle

# main application loop
bozo = nmy(1,True)
l= Coin(1,True)
b = Coin(1,True)
window.blit(l.image, l.rect)
window.blit(b.image, b.rect)
run = True
while run:
    # limit frames per second
    clock.tick(100)

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # update the game states and positions of objects dependent on the input 
    keys = pygame.key.get_pressed()
    cube.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed 
    cube.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed
    border_rect = window.get_rect()
    cube.clamp_ip(border_rect)

    # clear the display and draw background
    window.blit(background, (0, 0))    # draw the scene  
    window.blit(l.image, l.rect)
    window.blit(b.image, b.rect)
    window.blit(bozo.image, bozo.rect)
    bozo.update()
    b.update()    
    l.update()
    window.blit(cube2)
    pygame.draw.rect(window, (255, 0, 0), cube)
    text = font1.render(str(glo.score), True, GREEN)
    window.blit(text,(15,20))
    

    pygame.display.flip()
    
pygame.quit()
exit()