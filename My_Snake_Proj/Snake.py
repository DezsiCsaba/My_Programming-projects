#   --version 4.1
#   --AI implemented
#       AI uses the A*algorithm to solve the current best path after eating each apple      

from cmath import rect
from email.policy import default
from operator import length_hint
from pickle import FALSE, TRUE
import pstats
from random import randint, random
from sre_parse import State
from tkinter.tix import Tree
import pygame
import math
from time import sleep
from A_star import _PlayArea_to_Spot_Matrix, A_star_with_PlayArea

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
width = 900
height = 600
canvas = pygame.display.set_mode((width, height))

snake_block = 20 #size of one block of snake/food (10->10x10 pixels)

    #COLORS
white = (255, 255, 255)
transp_white = (255,255,255,127)
red = (255, 0, 0)
transp_red = (255, 0, 0, 50)
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
    
    #for wall in walls:
    #    pygame.draw.rect(canvas, wallcolor, wall)

    return walls
    #returns a list containing the RECtangles, and draws the walls

#----------------PLAY_AREA----------------


def GameOver():
    ourFont = pygame.font.Font("freesansbold.ttf", 30)
    text = ourFont.render('Game Over', True, white)
    canvas.blit(text, (width/2, height/2))
    #displays the "Game Over" text onto the display

#----------------SNAKE----------------

def Snekk(snake_block, snake_list):
    index = len(snake_list)-1
    for x in snake_list:
        #pygame.draw.rect(canvas,blue,(x[0], x[1], snake_block, snake_block))
        if (index == 0):
            pygame.draw.rect(canvas, blue,(x[2]))
        else:   pygame.draw.rect(canvas, blue, (x[2]))
        index += -1



def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)
    #draws a RECtangle with a set alpha and set color

def ShowVision_Area(vision_list, color):
    for x in vision_list:
        draw_rect_alpha(canvas, color, (x[0], x[1], snake_block, snake_block))
#----------------SNAKE----------------



#----------------BRAIN_OF_AI----------------
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
            pos.append(pygame.Rect(pos_x, pos_y, snake_block, snake_block))
            Vision.append(pos)
    for i in range (0, sizeOfVision):
        for j in range(0, sizeOfVision):
            pos = []
            pos_x = headX - (i * snake_block)
            pos_y = heaady + (j * snake_block)
            pos.append(pos_x)
            pos.append(pos_y)
            pos.append(pygame.Rect(pos_x, pos_y, snake_block, snake_block))
            Vision.append(pos)
    for i in range (0, sizeOfVision):
        for j in range(0, sizeOfVision):
            pos = []
            pos_x = headX - (i * snake_block)
            pos_y = heaady - (j * snake_block)
            pos.append(pos_x)
            pos.append(pos_y)
            pos.append(pygame.Rect(pos_x, pos_y, snake_block, snake_block))
            Vision.append(pos)
    for i in range (0, sizeOfVision):
        for j in range(0, sizeOfVision):
            pos = []
            pos_x = headX + (i * snake_block)
            pos_y = heaady + (j * snake_block)
            pos.append(pos_x)
            pos.append(pos_y)
            pos.append(pygame.Rect(pos_x, pos_y, snake_block, snake_block))
            Vision.append(pos)
    return Vision
def DangerArea(snake_block, snake_list, sizeOfVision = 2):
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
            pos.append(pygame.Rect(pos_x, pos_y, snake_block, snake_block))
            Vision.append(pos)
    for i in range (0, sizeOfVision):
        for j in range(0, sizeOfVision):
            pos = []
            pos_x = headX - (i * snake_block)
            pos_y = heaady + (j * snake_block)
            pos.append(pos_x)
            pos.append(pos_y)
            pos.append(pygame.Rect(pos_x, pos_y, snake_block, snake_block))
            Vision.append(pos)
    for i in range (0, sizeOfVision):
        for j in range(0, sizeOfVision):
            pos = []
            pos_x = headX - (i * snake_block)
            pos_y = heaady - (j * snake_block)
            pos.append(pos_x)
            pos.append(pos_y)
            pos.append(pygame.Rect(pos_x, pos_y, snake_block, snake_block))
            Vision.append(pos)
    for i in range (0, sizeOfVision):
        for j in range(0, sizeOfVision):
            pos = []
            pos_x = headX + (i * snake_block)
            pos_y = heaady + (j * snake_block)
            pos.append(pos_x)
            pos.append(pos_y)
            pos.append(pygame.Rect(pos_x, pos_y, snake_block, snake_block))
            Vision.append(pos)
    return Vision
def is_collision(snake_list, HeadOfSnake, walls):
    HeadOfSnake = snake_list[len(snake_list) - 1]
    for i in snake_list:
            for wall in walls:
                if pygame.Rect.colliderect(i[2], wall):
                    return True

    for i in snake_list[:-1]: #Checks from the end of the list
            if i == HeadOfSnake:  # if i(part of the snake)
               return True   # collides with the head
    return False
def would_it_collide(future_rect, snake_list, walls):
    for wall in walls:
        if pygame.Rect.colliderect(future_rect, wall): return True

    for i in snake_list[:-1]: #Checks from the end of the list
            if pygame.Rect.colliderect(i[2], future_rect):  # if i(part of the snake)
               return True   # collides with the head
    return False

def get_state(snake_block, snake_list, walls, foodx, foody):
    state = []
    sizeofSnake = len(snake_list)
    HeadOfSnake = snake_list[sizeofSnake - 1]

    headx, heady = HeadOfSnake[0], HeadOfSnake[1]    
    left = pygame.Rect(headx - snake_block, heady, snake_block, snake_block)
    right = pygame.Rect(headx + snake_block, heady, snake_block, snake_block)
    up = pygame.Rect(headx, heady - snake_block, snake_block, snake_block)
    down = pygame.Rect(headx, heady + snake_block, snake_block, snake_block)
    state.append(would_it_collide(left, snake_list, walls)) # [0] -> danger left (bool)
    state.append(would_it_collide(right, snake_list, walls))# [1] -> danger right (bool)
    state.append(would_it_collide(up, snake_list, walls))# [2] -> danger up (bool)
    state.append(would_it_collide(down, snake_list, walls))# [3] -> danger down (bool)

    if foodx < headx : state.append('left') # [4] -> location of food (left, right)
    elif foodx > headx : state.append('right') # [4] -> location of food (left, right)
    else : state.append('inLine')
    
    if foody < heady : state.append('up') # [5] -> location of food (up, down)
    elif foody > heady : state.append('down') # [5] -> location of food (up, down)
    else : state.append('inLine')

    return state
#state:    
    # [0] -> danger left (bool)
    # [1] -> danger right (bool)
    # [2] -> danger up (bool)
    # [3] -> danger down (bool)
    # [4] -> location of food (left, right)
    # [5] -> location of food (up, down)

#the basic movement that was implemented before A* (not workin really well )
#uses the state function which is also full of holes tbh -> (sometimes good, sometimes shit)
def AI_movement_output(state, step_list):   
    action = ''
    if len(step_list) != 0:
        if state[4] == 'left' and state[0] == False:# and step_list[len(step_list)-1] != 'right':
            action = state[4]
            return action 
        if state[4] == 'right' and state[1] == False:# and step_list[len(step_list)-1] != 'left':
            action = 'right'
            return action 
        if state[5] == 'up' and state[2] == False:# and step_list[len(step_list)-1] != 'down':
            action = 'up'
            return action
        if state[5] == 'down' and state[3] == False:# and step_list[len(step_list)-1] != 'up':
            action  = 'down'
            return action 
        else: return step_list[len(step_list)-1]
    else: 
        action = 'up'
        return action
 
 # --A* algorithm's workings
 # basically we want the snake to follow the path, that was calculated by A*
 # the path is made of _SpotC objects, and theese objects have .i and .j traits
    # we will use theese traits to tell where the snake will have to move
def NextStep(path, xpos, ypos, stepCount):
    # closest path element's index : len(path)-2
    x, y = xpos // snake_block, ypos // snake_block
    pygame.draw.rect(canvas, blue, (path[len(path)-stepCount].i*snake_block-2, path[len(path)-stepCount].j*snake_block-2, snake_block+4, snake_block+4))
    if (x < path[len(path)-stepCount].i):
        return "right"
    elif (x > path[len(path)-stepCount].i):
        return "left"
    elif (y < path[len(path)-stepCount].j):
        return "down"
    elif (y > path[len(path)-stepCount].j):
        return "up"
#----------------BRAIN_OF_AI----------------




#----------------APPLE----------------
def DrawApple(x_pos, y_pos):
    pygame.draw.rect(canvas,red,(x_pos, y_pos, snake_block, snake_block))
#----------------APPLE----------------

def Run_With_Inputs():
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
        
        

        snake_Head = [] #[0-xpos, 1-ypos, 2-RECT]
        snake_Head.append(xpos)
        snake_Head.append(ypos)        
        snake_Head.append(pygame.Rect(xpos, ypos, snake_block, snake_block))
        snake_list.append(snake_Head)

        if len(snake_list) > Length_of_Snake: #Deletes the tail of the snake
            del snake_list[0]                 # so we can make it 'move' 
        
        head_of_snake = snake_list[len(snake_list) - 1]
        if is_collision(snake_list, head_of_snake, walls) == True:
            game_over = True
            GameOver()
        
        vision = []
        dangerZone = []
        vision = SnakeVision(snake_block, snake_list, 5)
        dangerZone = DangerArea(snake_block, snake_list)
        #for pos in vision:
            #print(pos[0], pos[1])
        ShowVision_Area(vision, transp_white)
        ShowVision_Area(dangerZone, transp_red)
        DrawApple(foodx, foody)
        Snekk(snake_block, snake_list)

        
        CurrentState = get_state(snake_block, snake_list, walls, foodx, foody)
        print(CurrentState)


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

def Run_AI():
    game_over = False

    width / snake_block

    xpos = int((width)/2 //snake_block) * snake_block
    ypos = int((height)/2 //snake_block) * snake_block
    x_change = 0
    y_change = 0
    #DrawSnakeHead(xpos, ypos)
    snake_list = []

    snake_Head = [] #[0-xpos, 1-ypos, 2-RECT]
    snake_Head.append(xpos)
    snake_Head.append(ypos)        
    snake_Head.append(pygame.Rect(xpos, ypos, snake_block, snake_block))
    snake_list.append(snake_Head)

    Length_of_Snake = 1
    clock = pygame.time.Clock()

    foodx = int(randint(snake_block, width - (2*snake_block))/snake_block) * snake_block
    foody = int(randint(snake_block, height - (2*snake_block))/snake_block) * snake_block
    ourFont = pygame.font.Font("freesansbold.ttf", 15)

     #--------this is where the A* works it's magic        
    snakeMaze = _PlayArea_to_Spot_Matrix(foodx, foody, snake_list, width, height, snake_block, canvas)
    path = []
    path = A_star_with_PlayArea(snakeMaze, width//snake_block, height//snake_block, canvas, snake_block)
    #--------this is where the A* works it's magic 
    step_counter = 2
    

    points = 0
    while not game_over:
        print(step_counter)
        DrawGrass()
        #DrawWalls(red)
        walls = []
        
        DrawApple(foodx, foody)
        text = ourFont.render('Points: ' + str(points), True, transp_white)
        canvas.blit(text, (0, 0))
        
        action = NextStep(path, xpos, ypos, step_counter)        
        if action == 'left':
            x_change = -snake_block
            y_change = 0
        elif action == 'right':
            x_change = +snake_block
            y_change = 0
        elif action == 'down':
            x_change = 0
            y_change = +snake_block
        elif action == 'up':
            x_change = 0
            y_change = -snake_block
        
        xpos += x_change
        ypos += y_change
        step_counter += 1

        if xpos == foodx and ypos == foody: #Checks if the head of the snake collides with the food
            snake_body = [] #[0-xpos, 1-ypos, 2-RECT]
            snake_body.append(xpos)
            snake_body.append(ypos)        
            snake_body.append(pygame.Rect(xpos, ypos, snake_block, snake_block))
            snake_list.append(snake_body)

            foodx = int(randint(snake_block, width - (2*snake_block))/snake_block) * snake_block
            foody = int(randint(snake_block, height - (2*snake_block))/snake_block) * snake_block
            Length_of_Snake += 1            # if yes we add one more snake_block
            print("+1 point")
            points += 1
            DrawApple(foodx, foody)
            step_counter = 2
             #--------this is where the A* works it's magic        
            snakeMaze = _PlayArea_to_Spot_Matrix(foodx, foody, snake_list, width, height, snake_block, canvas)
            path = []
            path = A_star_with_PlayArea(snakeMaze, width//snake_block, height//snake_block, canvas, snake_block)
          
            #--------this is where the A* works it's magic 
        else:
            snake_body = [] #[0-xpos, 1-ypos, 2-RECT]
            snake_body.append(xpos)
            snake_body.append(ypos)        
            snake_body.append(pygame.Rect(xpos, ypos, snake_block, snake_block))
            snake_list.append(snake_body)
        
        
        #for i in range(len(path)):
        #    draw_rect_alpha(canvas, transp_white, (path[i].i*snake_block, path[i].j*snake_block, snake_block-1, snake_block-1))

        if len(snake_list) > Length_of_Snake: #Deletes the tail of the snake
            del snake_list[0]                 # so we can make it 'move' 
        
        head_of_snake = snake_list[len(snake_list) - 1]
        if is_collision(snake_list, head_of_snake, walls) == True:
            game_over = True
            GameOver()
        
        
        Snekk(snake_block, snake_list)


        pygame.display.update()
        if game_over == FALSE:
            canvas.fill(black)

        #DrawSnakeHead(xpos, ypos)
        clock.tick(60)
        #sleep(0.2)

#Run_With_Inputs()
Run_AI()
DontClose()
