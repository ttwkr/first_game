import pygame
from .ddong import *
import random
pygame.init()

screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load("./src/img/background.png")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))
    screen.blit(ddong, (0, random.randrange(0, screen_height)))
    pygame.display.update()
pygame.quit()
