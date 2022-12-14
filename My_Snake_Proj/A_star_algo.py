from itertools import count
import this
import pygame
from numpy import *
from Spot import _SpotC
from time import sleep
import math

clock = pygame.time.Clock()

block_size = 15
width = 1200
height = 500

cols = width // block_size
rows = height // block_size

canvas = pygame.display.set_mode((width, height))


white = (255, 255, 255)
transp_white = (255,255,255,127)
red = (255, 0, 0)
transp_red = (255, 0, 0, 125)
blue = (0, 0, 255)
green = (0, 125, 0)
black = (0,0,0)


def heuristic(a, b):
    #dist = math.hypot(a.i-b.i, a.j-b.j)
    #dist = (b.i-a.i) + (b.j-a.j)
    dist = absolute(a.i-b.i) + absolute(a.j-b.j)
    return dist

openSet = []
closedSet = []
   


def Do_not_close():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
            pygame.display.update()


def _matrixWithSpots_():    
    print(str(cols) + " X " + str(rows))
    maze = []

    counter = 0
    for i in range(cols):
        row = []
        for j in range(rows):
            if (i == 0 and j == 0):
                spot = _SpotC()
                spot._SpotInit_(i, j)
                spot.wall, spot.start, spot.finish = False, True, False    
            elif (i == cols-2 and j == rows-2):
                spot = _SpotC()
                spot._SpotInit_(i, j)
                spot.wall, spot.finish, spot.start = False, True, False
                spot.f = 0; spot.h = 0; spot.f = 0
            else:
                spot = _SpotC()
                spot._SpotInit_(i, j)   
                
            row.append(spot)        
            spot.ShowPoint(canvas, block_size)   
            counter += 1
            #print(str(counter) + ". spots's: i" + str(spot.i) +" - j"+ str(spot.j) +" "+ str(spot.start)+" "+str(spot.finish)) 
        maze.append(row)

    for i in range(cols-1):
        for j in range(rows-1):
            maze[i][j].AddNeighbours(maze, cols, rows)
    return maze

def _2dArray_to_Spot_Matrix():
    spotmatrix = []

    return spotmatrix

def A_star_algorithm(maze):
    openSet.append(maze[0][0])

    end = _SpotC()
    end = maze[cols-2][rows-2]
    path = []
    temp = _SpotC()
    run = True
    while(run == True):
        if (len(openSet) > 0):

            #best next option
            winner = 0
            for i in range(len(openSet)):
                if (openSet[i].f < openSet[winner].f):
                    winner = i     
                #elif (openSet[i].g > openSet[winner].g):
                #    winner = i
            current = openSet[winner]


            #did we reach the finish?
            if (current == end):
                print("FinishedTask")
                run = False

            #we move the best option from openSet to closedset
            openSet.remove(current)
            closedSet.append(current)
            

            #check the neighbours
            thisNeighbours = []
            thisNeighbours = current.neighbours
            for i in range(len(thisNeighbours)):
                neighbour = _SpotC()
                neighbour = thisNeighbours[i]

                #is the next spot valid or not?
                if ((neighbour not in closedSet) and (neighbour.wall == False)):
                    tempG = current.g + heuristic(neighbour, current) #end helyett current volt !!!!!!!!!!
                    
                    #is the new found solution a better path?
                    newPath = False
                    if(neighbour in openSet):
                        if(tempG <= neighbour.g):
                            neighbour.g = tempG
                            newPath = True
                    else:
                        neighbour.g = tempG
                        newPath = True
                        openSet.append(neighbour)

                    #it IS a better path
                    if(newPath == True):
                        #print("better path")
                        neighbour.h = heuristic(neighbour, end)
                        neighbour.f = neighbour.g + neighbour.h
                        neighbour.previous = current
            
            
        else:
            print("No possible solution")
            run = False
                
        #draws the current state of the stage:
        for i in range(cols):
            for j in range(rows):
                maze[i][j].ShowPoint(canvas, block_size)
            
        for i in range(len(closedSet)):
            closedSet[i].Show(canvas, block_size, red)
            #print(len(closedSet))

        for i in range(len(openSet)):
            openSet[i].Show(canvas, block_size, green)

        temp = current
        path = []
        path.append(temp)
        while(temp.previous !=  None):
            path.append(temp.previous)
            temp = temp.previous

        for i in range(len(path)):
            path[i].Show(canvas, block_size, blue)
        pygame.display.update()
        clock.tick(120)
    
    return path



path=[]
maze = _matrixWithSpots_()
path = A_star_algorithm(maze)

canvas.fill(black)
for i in range(len(path)):
    path[i].Show(canvas, block_size, blue)
    pygame.display.update()
Do_not_close()
