# --Base Game of Snake


from collections import namedtuple
from tkinter import Canvas
import pygame
from enum import Enum
import random
from random import randint


pygame.init()

width = 640
height = 480

Point = namedtuple('Point', 'x,y')

class Colors(Enum):
    white = (255, 255, 255)
    transp_white = (255,255,255,127)
    red = (255, 0, 0)
    blue = (0, 0, 125)
    green = (0, 125, 0)
    transp_green = (0, 125, 0, 150)
    black = (0, 0, 0)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('SnekkGame')


class GameContent():
    def DontClose():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    pygame.quit()
                pygame.display.update()

    def DrawGrass():
         pygame.draw.rect(window, Colors.transp_green, (0, 0, width, height))
    
    def GameOver():
        ourFont = pygame.font.Font("freesansbold.ttf", 20)
        text = ourFont.render('Game Over', True, Colors.white)
        window.blit(text, (width/2, height/2))

    def Snekk(snake_list):
        for i in snake_list:
            pygame.draw.rect(window, Colors.blue, (i[i]))

    def DrawApple(x, y):
        pygame.draw(window, Colors.red, (x, y))

GameContent.DontClose()
