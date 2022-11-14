import pygame
import pygame_menu
pygame.init()
surface = pygame.display.set_mode((600, 400))


'''def set_difficulty(value, difficulty):
    if difficulty == 1:
        speed = 5
    else:
        speed = 6'''

def start_the_game():
    import game

menu = pygame_menu.Menu('You Died', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

'''menu.add.text_input('Name :', default=' ')
'''#menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)
