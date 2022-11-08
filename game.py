import pygame
from pygame.locals import *
import time
# Importing os module
import os
import random
# absolute path
path = os.getcwd()
# python os path join method
fontspath = os.path.join(path, "fonts")
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
pygame.init()
def gameover():
    execfile("ondeath.py")
    exit()
class nmy(object):

    def __init__(self):
        self.nmy_spawn()

    def nmy_spawn(self):
        self.food_x = random.randrange(0, 615, 1)
        self.food_y = random.randrange(0, 615, 1)

    def nmy_drawing(self):
        f = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(self.food_x, self.food_y, 30, 30))
        collide2 = f.colliderect(cube)
        if collide2:
            gameover()
        
    

x = 1



window = pygame.display.set_mode((650, 650))
clock = pygame.time.Clock()
bar = 0
background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *background.get_size(), (128, 128, 128), (64, 64, 64)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
[pygame.draw.rect(background, color, rect) for rect, color in tiles]

cube = pygame.Rect(0, 0, 20, 20)
cube.center = window.get_rect().center
speed = 5
nono = pygame.draw.rect(background, BLUE, pygame.Rect(30, 30, 60, 60))
nonoo = 10
font1 = pygame.font.SysFont([os.path.join(fontspath,"LektonCode-Regular.ttf")], 72)

    

# Initialing Color
colore = (0,255,0)
  
# Drawing Rectangle

# main application loop
while x<= 10:
        bozo = nmy()
        bozo.nmy_spawn()
        
        
        x+=1
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
    
    pygame.draw.rect(window, (255, 0, 0), cube)
    bozo.nmy_drawing()
    
    collide = nono.colliderect(cube)
    if collide:
        gameover()
    pygame.display.flip()
pygame.quit()
exit()