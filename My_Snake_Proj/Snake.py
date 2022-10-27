#   --version 2.1

from cmath import rect
from operator import length_hint
from pickle import FALSE, TRUE
from random import randint, random
from tkinter.tix import Tree
import pygame
import math
from time import sleep

pygame.init()

pygame.display.set_caption("Snekk_Game")
def DontClose():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
            pygame.display.update()

    #CANVAS
width = 400
height = 400
canvas = pygame.display.set_mode((width, height))

    #COLORS
white = (255, 255, 255)
transp_white = (255,255,255,127)
red = (255, 0, 0)
blue = (0, 0, 125)
green = (0, 125, 0)
transp_green = (0, 125, 0, 150)
black = (0, 0, 0)

#----------------PLAY_AREA----------------
def DrawGrass():
    pygame.draw.rect(canvas,transp_green,(0, 0, width, height))
    #draws a rectangle on the full display, aka Grass/ground

def DrawWalls(wallcolor):
    walls = []
    top = pygame.Rect(0, 0, width, 10)
    left = pygame.Rect(0, 0, 10, height)
    right = pygame.Rect(width - 10, 0, 10, height)
    bottom = pygame.Rect(0, height - 10, width, 10)

    walls.append(top)
    walls.append(left)
    walls.append(right)
    walls.append(bottom)
    
    for wall in walls:
        pygame.draw.rect(canvas, wallcolor, wall)

    return walls
    #returns a list containing the RECtangles, and draws the walls

#----------------PLAY_AREA----------------


def GameOver():
    ourFont = pygame.font.Font("freesansbold.ttf", 30)
    text = ourFont.render('Game Over', True, white)
    canvas.blit(text, (width/2, height/2))
    #displays the "Game Over" text onto the display

#----------------SNAKE----------------
snake_block = 10 #size of one block of snake/food (10->10x10 pixels)

def Snekk(snake_block, snake_list):
    for x in snake_list:
        #pygame.draw.rect(canvas,blue,(x[0], x[1], snake_block, snake_block))
        pygame.draw.rect(canvas, blue, (x[2]))

def SnakeVision(snake_block, snake_list, sizeOfVision):
    HeadOfSnake = []
    sizeofSnake = len(snake_list)
    HeadOfSnake = snake_list[sizeofSnake - 1]
    headX = HeadOfSnake[0]
    heaady = HeadOfSnake[1]
    Vision = []
    for i in range (0, sizeOfVision):
        for j in range(0, sizeOfVision):
            pos = []
            pos_x = headX + (i * snake_block)
            pos_y = heaady - (j * snake_block)
            pos.append(pos_x)
            pos.append(pos_y)
            Vision.append(pos)
    for i in range (0, sizeOfVision):
        for j in range(0, sizeOfVision):
            pos = []
            pos_x = headX - (i * snake_block)
            pos_y = heaady + (j * snake_block)
            pos.append(pos_x)
            pos.append(pos_y)
            Vision.append(pos)
    for i in range (0, sizeOfVision):
        for j in range(0, sizeOfVision):
            pos = []
            pos_x = headX - (i * snake_block)
            pos_y = heaady - (j * snake_block)
            pos.append(pos_x)
            pos.append(pos_y)
            Vision.append(pos)
    for i in range (0, sizeOfVision):
        for j in range(0, sizeOfVision):
            pos = []
            pos_x = headX + (i * snake_block)
            pos_y = heaady + (j * snake_block)
            pos.append(pos_x)
            pos.append(pos_y)
            Vision.append(pos)
    return Vision

def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)
    #draws a RECtangle with a set alpha and set color

def ShowVision_Area(vision_list):
    for x in vision_list:
        draw_rect_alpha(canvas, transp_white, (x[0], x[1], snake_block, snake_block))
#----------------SNAKE----------------

#----------------AI_MOVEMENT----------------

#----------------AI_MOVEMENT----------------

#----------------APPLE----------------
def DrawApple(x_pos, y_pos):
    pygame.draw.rect(canvas,red,(x_pos, y_pos, snake_block, snake_block))
#----------------APPLE----------------

def RunGame_withInputs():
    game_over = False

    xpos = width / 2
    ypos = height / 2
    x_change = 0
    y_change = 0
    #DrawSnakeHead(xpos, ypos)

    snake_list = []
    Length_of_Snake = 1
    clock = pygame.time.Clock()
    
    foodx = round(randint(0, width - snake_block)/snake_block) * snake_block
    foody = round(randint(0, height - snake_block)/snake_block) * snake_block


    while not game_over:
        DrawGrass()
        DrawWalls(red)
        walls = []
        walls = DrawWalls(red)
            #inputs
        for event in pygame.event.get():
            if event.type == pygame.quit:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = +snake_block
                    y_change = 0
                if event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = +snake_block
                if event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_block
        xpos += x_change
        ypos += y_change
            #inputs
        
            #Checks for collision between the snake and the wall barrier
        for i in snake_list:
            for wall in walls:
                if pygame.Rect.colliderect(i[2], wall):
                    game_over = TRUE
                    GameOver()

        snake_Head = [] #[0-xpos, 1-ypos, 2-RECT]
        snake_Head.append(xpos)
        snake_Head.append(ypos)        
        snake_Head.append(pygame.Rect(xpos, ypos, snake_block, snake_block))
        snake_list.append(snake_Head)

        if len(snake_list) > Length_of_Snake: #Deletes the tail of the snake
            del snake_list[0]                 # so we can make it 'move' 
        
        for i in snake_list[:-1]: #Checks from the end of the list
            if i == snake_Head:   # if i(part of the snake)
               game_over = True   # collides with the head
               GameOver()         # THEN it is GameOver

        
        vision = []
        vision = SnakeVision(snake_block, snake_list, 5)
        for pos in vision:
            print(pos[0], pos[1])
        ShowVision_Area(vision)
        DrawApple(foodx, foody)
        Snekk(snake_block, snake_list)
        pygame.display.update()
        if game_over == FALSE:
            canvas.fill(black)

        if xpos == foodx and ypos == foody: #Checks the head of the snake collides with the food
            foodx = round(randint(0, width - snake_block - 10)/snake_block) * snake_block
            foody = round(randint(0, height - snake_block - 10)/snake_block) * snake_block
            Length_of_Snake += 1            # if yes we add one more snake_block
            print("+1 point")

        #DrawSnakeHead(xpos, ypos)
        clock.tick(24)
        sleep(0.1)


def RunGame():
    game_over = False

    xpos = width / 2
    ypos = height / 2
    x_change = 0
    y_change = 0
    #DrawSnakeHead(xpos, ypos)

    snake_list = []
    Length_of_Snake = 1
    clock = pygame.time.Clock()
    
    foodx = round(randint(0, width - snake_block)/snake_block) * snake_block
    foody = round(randint(0, height - snake_block)/snake_block) * snake_block


    while not game_over:
        DrawGrass()
        DrawWalls(red)
        walls = []
        walls = DrawWalls(red)
        
        
        snake_Head = []
        snake_Head.append(xpos)
        snake_Head.append(ypos)
        snake_list.append(snake_Head)
        
        vision = []
        vision = SnakeVision(snake_block, snake_list, 10)
        foodIn_distance = False
        #----------------INPUTS----------------
        for visionBlock in vision:
            if visionBlock[0] == foodx and visionBlock[1] == foody: ##If the snake sees the food
                foodIn_distance = True
                print("food in vision")
                if foodx == snake_Head[0]:
                    if abs(foodx - snake_Head[0]) < 1:
                       if foody > snake_Head[1]:
                           y_change = snake_block
                           x_change = 0
                       elif foody < snake_Head[1]:
                           y_change = -snake_block
                           x_change = 0
                elif foodx > snake_Head[0]:                    
                    if abs(foodx - snake_Head[0]) < 1:
                        if foody > snake_Head[1]:
                            y_change = snake_block
                            x_change = 0
                        elif foody < snake_Head[1]:
                            y_change = -snake_block
                            x_change = 0
                    else : x_change = snake_block
                elif foodx < snake_Head[0]:                    
                    if abs(foodx - snake_Head[0]) < 1:
                        if foody > snake_Head[1]:
                            y_change = snake_block
                            x_change = 0
                        elif foody < snake_Head[1]:
                            x_change = 0
                            y_change = -snake_block
                    else: x_change = - snake_block
                break
            
        if foodIn_distance == False:
            print("Food is not in distance")
            number = randint(1, 4)
            if number == 1:
                x_change = -snake_block
                y_change = 0
            if number == 2:
                x_change = snake_block
                y_change = 0
            if number == 3:
                x_change = 0
                y_change = snake_block
            if number == 4:
                x_change = 0
                y_change = -snake_block    
#if event.type == pygame.KEYDOWN:
#    if event.key == pygame.K_LEFT:
#        x_change = -snake_block
#        y_change = 0
#    if event.key == pygame.K_RIGHT:
#        x_change = +snake_block
#        y_change = 0
#    if event.key == pygame.K_DOWN:
#        x_change = 0
#        y_change = +snake_block
#    if event.key == pygame.K_UP:
#        x_change = 0
#        y_change = -snake_block
        
        xpos += x_change
        ypos += y_change
        #----------------INPUTS----------------
        
        if xpos<=0 or xpos>=width or ypos<=0 or ypos>=height:
            game_over = True
            GameOver()
            

        if len(snake_list) > Length_of_Snake:
            del snake_list[0]

        for i in snake_list[:-1]:
            if i == snake_Head:
               game_over = True
               GameOver()

        
        #for pos in vision:
            #print(pos[0], pos[1])
        ShowVision_Area(vision)
        DrawApple(foodx, foody)
        Snekk(snake_block, snake_list)
        pygame.display.update()
        if game_over == FALSE:
            canvas.fill(black)

        if xpos == foodx and ypos == foody:
            foodx = round(randint(0, width - snake_block - 10)/snake_block) * snake_block
            foody = round(randint(0, height - snake_block - 10)/snake_block) * snake_block
            Length_of_Snake += 1
            print("+1 point")

        #DrawSnakeHead(xpos, ypos)
        clock.tick(24)
        sleep(0.1)


RunGame_withInputs()
#RunGame()
DontClose()
