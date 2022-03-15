from pickle import NONE
import pygame, sys, time, random
from pygame.locals import *


def fadeout(surface, coordinates = (0, 0), ms_delay = 0):
    # global debug_text

    infoObject = pygame.display.Info()
    fadeout = pygame.Surface((infoObject.current_w, infoObject.current_h))
    # Find out what this does
    fadeout = fadeout.convert()
    fadeout.fill(BLACK)
    for i in range(255):
        # debug_text = debug_font.render(f'{i}', True, WHITE, BLACK)
        # windowSurface.blit(debug_text, (0, 0))

        windowSurface.blit(surface, coordinates)

        fadeout.set_alpha(i)
        windowSurface.blit(fadeout, (0, 0))
        pygame.display.update()
        time.sleep(ms_delay)
        

def fadein(surface, coordinates = (0, 0), ms_delay = 0):
    # global debug_text

    infoObject = pygame.display.Info()
    fadein = pygame.Surface((infoObject.current_w, infoObject.current_h))
    # Find out what this does
    fadein = fadein.convert()
    fadein.fill(BLACK)
    for i in range(255):
        # debug_text = debug_font.render(f'{i}', True, WHITE, BLACK)
        # windowSurface.blit(debug_text, (0, 0))

        windowSurface.blit(surface, coordinates)

        fadein.set_alpha(255-i)
        windowSurface.blit(fadein, (0, 0))
        pygame.display.update()
        time.sleep(ms_delay)

# Cool fonts:
# brushscript
# parchment
# frenchscript
# harrington
def rand_font():
    font = pygame.font.get_fonts()[random.randint(1,len(pygame.font.get_fonts()))-1]
    print(font)
    return font

def rand_rgb():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# set up pygame
pygame.init()

display = pygame.display.Info()
windowSurface = pygame.display.set_mode((display.current_w, display.current_h), FULLSCREEN, 32)
pygame.display.set_caption('Dodger')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up fonts
sys_fonts = pygame.font.get_fonts()
random_font = sys_fonts[random.randint(1,len(sys_fonts))-1]

debug_font = pygame.font.SysFont('arial', 64)
intro_font = pygame.font.SysFont(rand_font(), 128)
title_font = pygame.font.SysFont(rand_font(), 256)
menu_font = pygame.font.SysFont(rand_font(), 128)
submenu_font = pygame.font.SysFont(rand_font(), 64)


intro_color = rand_rgb()


intro_text = intro_font.render('CCCV Studios', True, intro_color, BLACK)
textRect = intro_text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# draw the text onto the surface
windowSurface.blit(intro_text, textRect)

fadein(intro_text, textRect)
time.sleep(1)
fadeout(intro_text, textRect)


#
intro_text = intro_font.render('copyrite lololol', True, intro_color, BLACK)
textRect = intro_text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

windowSurface.blit(intro_text, textRect)

fadein(intro_text, textRect)
time.sleep(1)
fadeout(intro_text, textRect)


# windowSurface.fill(BLACK)
title_text = title_font.render('Dodger', True, rand_rgb(), BLACK)
textRect = title_text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

windowSurface.blit(title_text, textRect)

fadein(title_text, textRect)
time.sleep(1)
fadeout(title_text, textRect)

menu_text = menu_font.render('Dodger', True, rand_rgb(), BLACK)
textRect = menu_text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery / 2

windowSurface.blit(menu_text, textRect)


submenu_color = rand_rgb()


submenu_text = submenu_font.render('Play', True, submenu_color, BLACK)
textRect = submenu_text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

windowSurface.blit(submenu_text, textRect)

submenu_text = submenu_font.render('Settings', True, submenu_color, BLACK)
textRect = submenu_text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery * 1.25

windowSurface.blit(submenu_text, textRect)

submenu_text = submenu_font.render('Quit', True, submenu_color, BLACK)
textRect = submenu_text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery * 1.5

windowSurface.blit(submenu_text, textRect)

pygame.display.update()


# run the game loop
while True:
    # Cycles through all the events currently occuring
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
           
        # Condition becomes true when keyboard is pressed   
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_LEFT:
                print('LEFT')

            if event.key == pygame.K_RIGHT:
                print('RIGHT')

                
