from collections import namedtuple

import string
import pygame
from random import randint
from queue import PriorityQueue
from numpy import *

width = 300
height = 300
canvas = pygame.display.set_mode((width, height))

white = (255, 255, 255)
transp_white = (255,255,255,127)
red = (255, 0, 0)
transp_red = (255, 0, 0, 125)
blue = (0, 0, 125)
green = (0, 125, 0)

Point = namedtuple('Point', 'x,y')

def Do_not_close():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
            pygame.display.update()

block_size = 25

def Random_point():
    x = round(randint(0, width - block_size)/block_size) * block_size
    return x

def _draw_list_of_rect(block_list, color):
    for i in range (len(block_list)):
        pygame.draw.rect(canvas, color, block_list[i][2])

def _walls():
    walls = []
    for i in range((((width//block_size) * (height//block_size)) // 100) * 50):
        wall = []
        x = Random_point()
        y = Random_point()
        r = pygame.Rect(x, y, block_size-1, block_size-1)        
        wall.append(x)
        wall.append(y)
        wall.append(r)
        walls.append(wall)
        
    return walls


def _random_block(blocks, color):
    blockInfo = []
    for x in blocks:   
        block = []     
        start_x = Random_point()
        start_y = Random_point()
        r = pygame.Rect(start_x, start_y, block_size-1, block_size-1)
        if pygame.Rect.colliderect(r, x[2]) == False: break
        
    pygame.draw.rect(canvas, color, r)
    blockInfo.append(start_x)
    blockInfo.append(start_y)
    blockInfo.append(r)
    return blockInfo     # blockinfo: [0]->x, [1]->y, [2]->rect


def _make_matrix(width, height):
    columns = height // block_size
    rows = width // block_size
    print(str(columns) + " X " + str(rows))
    maze = []
    for j in range(columns):
        row = []
        for i in range(rows):
           
            if randint(1,5) == 1:
                    row.append("W")
            else:
                row.append("0")
                
        maze.append(row)
    return maze

def _draw_walls(maze):
    x = 0
    y= 0
    for i in range(height//block_size):
        for j in range(width//block_size):
            if maze[i][j] == 'W':
                pygame.draw.rect(canvas, white, (x, y, block_size-1, block_size-1))
            if maze[i][j] == '0':
                pygame.draw.rect(canvas, green, (x, y, block_size-1, block_size-1))
            x += block_size
            print("j: " + str(j))
        y += block_size
        print("j: " + str(i))


maze = _make_matrix(width, height)
_draw_walls(maze)
#print(maze)
Do_not_close()