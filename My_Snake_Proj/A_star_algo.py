from itertools import count
import this
import pygame
from numpy import *
from Spot import _SpotC
from time import sleep
import math

clock = pygame.time.Clock()

block_size = 25
width = 600
height = 600

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
    dist = (a.i-b.i) + (a.j-b.j)
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
#    for i in range(cols):
#        for j in range(rows):
#            spot.AddNeighbours(spot, maze, cols, rows)
    return maze


maze = _matrixWithSpots_()
#print(maze[0][0].i, maze[0][0].j)
#print(maze[cols-1][rows-1].i, maze[cols-1][rows-1].j)
#for i in range(cols):
#    for j in range(rows):
#        print( "-> spots's: i" + str(maze[i][j].i) +" - j"+ str(maze[i][j].j) +" "+ str(maze[i][j].start)+" "+str(maze[i][j].finish)) 
       

       
openSet.append(maze[0][0])
end = _SpotC()
end._SpotInit_(cols-1, rows-1)
end.wall, end.finish = False, True


for i in range(cols-1):
    for j in range(rows-1):
        #print(i,j)
        maze[i][j].AddNeighbours(maze, cols, rows)


while(len(openSet) > 0):
    #clock.tick(30)
    #best next option
    winner = 0
    for i in range(len(openSet)):
        if (openSet[i].f < openSet.__getitem__(winner).f):
            winner = i     
    current = openSet.__getitem__(winner)

    #did we reach the finish?
    if (current == end):
        print("FinishedTask")
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
        if (neighbour not in closedSet and neighbour.wall == False):
            tempG = current.g + heuristic(neighbour, current)

            #is the new found solution a better path?
            newPath = False
            if(openSet.__contains__(neighbour)):
                if(tempG < neighbour.g):
                    neighbour.g = tempG
                    newPath = True
            else:
                neighbour.g = tempG
                newPath = True
                openSet.append(neighbour)

            if(newPath):
                neighbour.heuristic = heuristic(neighbour, end)
                neighbour.f = neighbour.g + neighbour.heuristic
                neighbour.previous = current
    
    if len(openSet)<1:
        print("No solution Possible")

    
    for i in range(cols):
        for j in range(rows):
            maze[i][j].ShowPoint(canvas, block_size)


    for j in range(len(openSet)):
        openSet[i].Show(canvas, block_size, green)
        
    for i in range(len(closedSet)):
        closedSet[i].Show(canvas, block_size, red)
        #print(len(closedSet))
    pygame.display.update()
    clock.tick(120)
        
Do_not_close()
