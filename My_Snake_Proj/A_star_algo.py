from itertools import count
import this
import pygame
from numpy import *
from Spot import _SpotC
from time import sleep
import math

clock = pygame.time.Clock()

block_size = 20
width = 500
height = 500

cols = width // block_size
rows = height // block_size

canvas = pygame.display.set_mode((width, height))


white = (255, 255, 255)
transp_white = (255,255,255,127)
red = (255, 0, 0)
transp_red = (255, 0, 0, 125)
blue = (0, 0, 125)
green = (0, 125, 0)
black = (0,0,0)


def heuristic(a, b):
    #dist = math.hypot(a.i-b.i, a.j-b.j)
    dist = (b.i-a.i) + (b.j-a.j)
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
            elif (i == cols-1 and j == rows-1):
                spot = _SpotC()
                spot._SpotInit_(i, j)
                spot.wall, spot.finish, spot.start = False, True, False
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


maze = _matrixWithSpots_()

       
openSet.append(maze[0][0])

end = _SpotC()
end._SpotInit_(cols-1, rows-1)
end.wall, end.finish = False, True
print()
path = []
run = True
while(run):
    if (len(openSet) > 0):
        #clock.tick(30)
        #best next option
        winner = 0
        for i in range(len(openSet)):
            if (openSet[i].f < openSet[winner].f):
                winner = i     
        current = openSet[winner]
        #print(end.i, end.j, current.i, current.j)
        #did we reach the finish?

        if (current.i == end.i and current.j == end.j):
            print("FinishedTask")
            run = False
            break
        

        #we move the best option to the openSet
        openSet.remove(current)
        closedSet.append(current)

        #check the neighbours
        thisNeighbours = current.neighbours
        for i in range(len(thisNeighbours)):
            neighbour = _SpotC()
            neighbour = thisNeighbours[i]

            #is the next spot valid or not?
            if ((neighbour not in closedSet) and (neighbour.wall == False)):
                tempG = current.g + heuristic(neighbour, current)
                
                #is the new found solution a better path?
                newPath = False
                if(neighbour in openSet):
                    if(tempG < neighbour.g):
                        neighbour.g = tempG
                        newPath = True
                else:
                    neighbour.g = tempG
                    newPath = True
                    openSet.append(neighbour)

                #it is a better path
                if(newPath):
                    #print("better path")
                    neighbour.h = heuristic(neighbour, end)
                    neighbour.f = neighbour.g + neighbour.h
                    neighbour.pevious = current
    else:
        print("No possible solution")
        run = False
        break

            
        #draws the current state of the stage:
    temp = current
    path.append(temp)
    #print(len(path))
    while(temp.previous is not None):
        path.append(temp.previous)
        temp = temp.previous
    for i in range(cols):
        for j in range(rows):
            maze[i][j].ShowPoint(canvas, block_size)
        
    for i in range(len(openSet)):
        openSet[i].Show(canvas, block_size, black)

    for i in range(len(path)):
        path[i].Show(canvas, block_size, blue)

    for i in range(len(closedSet)):
        closedSet[i].Show(canvas, block_size, red)
        #print(len(closedSet))

    pygame.display.update()
    clock.tick(24)
        
Do_not_close()
