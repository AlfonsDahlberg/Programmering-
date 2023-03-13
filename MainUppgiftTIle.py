import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer")

#laddar bilder
basbild_img = pygame.image.load("gymbild.jpg")
sol_img = pygame.image.load("pixil-frame-0.png")

run = True
while run:

    screen.blit(basbild_img, (0,0))
    screen.blit(sol_img, (100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
