import pygame
from pygame.locals import *
import time
# Importing os module
import os
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

window = pygame.display.set_mode((650, 650))
clock = pygame.time.Clock()

background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *background.get_size(), (128, 128, 128), (64, 64, 64)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
[pygame.draw.rect(background, color, rect) for rect, color in tiles]

cube = pygame.Rect(0, 0, 20, 20)
cube.center = window.get_rect().center
speed = 5
nono = pygame.draw.rect(background, BLUE, pygame.Rect(30, 30, 60, 60))

font1 = pygame.font.SysFont([os.path.join(fontspath,"LektonCode-Regular.ttf")], 72)
img1 = font1.render('Game Over', True, BLUE)  



# Initialing Color
colore = (0,255,0)
  
# Drawing Rectangle

# main application loop
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
    window.blit(background, (0, 0))

    # draw the scene  
    # 
    pygame.draw.rect(window, (255, 0, 0), cube)
     
    pygame.draw.rect(background, colore, pygame.Rect(30, 30, 60, 60))
    collide = nono.colliderect(cube)
    if collide:
        window.blit(img1, (20, 50))
        break
    # update the display
    pygame.display.flip()
execfile("f.py")
pygame.quit()
exit()