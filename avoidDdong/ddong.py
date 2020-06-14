import pygame
from .main import *


class Ddong():

    ddong = pygame.image.load('../src/img/enemy.png')
    ddong_size = ddong.get_rect().size
    ddong_width = ddong_size[0]
    ddong_heigh = ddong_size[1]
    ddong_x = screen_width/2
    ddong_y = screen_height/2
