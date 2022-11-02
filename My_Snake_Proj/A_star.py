import pygame
from random import randint
from Spot import _SpotC
from numpy import *


# heuristic algorihm
def heuristic(a, b):
    dist = absolute(a.i-b.i) + absolute(a.j-b.j) #absolute distance between the 2 point
    return dist


# algo that makes a matrix consisting of SpotC objects from the Play Area
def _PlayArea_to_Spot_Matrix(foodx, foody, snake_list, w, h, block, Surface):
    spotmatrix = []
    cols = w // block
    rows = h // block

    for i in range(cols):
        row = []
        for j in range(rows):
            spot = _SpotC()
            spot._SpotInit_(i, j)   

            #create the spots with no wall, finih & start set to default
            spot.wall, spot.finish, spot.start = False, False, False
            
            row.append(spot)        
            #spot.ShowPoint(Surface, block)  
        spotmatrix.append(row)

    #print(str(cols) + "x" + str(rows))
    #set the snake's body to walls : snakelist[i] -> [0-xpos, 1-ypos, 2-RECT] 
    #print("length of snakeList: " + str(len(snake_list)))  
    for i in range(len(snake_list)):
        x = snake_list[i][0] // block
        y = snake_list[i][1] // block
        #print("x:" + str(x) + " y:" + str(y))
        spotmatrix[int(x)][int(y)].wall = True
        spotmatrix[int(x)][int(y)].ShowPoint(Surface, block)

    #set the head's wall to false & the start to True; head -> list[len-1]
    headx = int(snake_list[len(snake_list)-1][0] // block)
    heady = int(snake_list[len(snake_list)-1][1] // block)
    #headx = int(snake_list[0][0] // block)
    #heady = int(snake_list[0][1] // block)
    
    spotmatrix[headx][heady].wall = True
    spotmatrix[headx][heady].start = True

    #set the food to finish
    spotmatrix[foodx // block][foody // block].wall = False
    spotmatrix[foodx // block][foody // block].finish = True

    for i in range(cols-1):
        for j in range(rows-1):
            spotmatrix[i][j].AddNeighbours(spotmatrix, cols, rows)
    return spotmatrix

# A* algorithm that uses the upper mentioned matrix to solve the 'maze'
openSet = []
closedSet = []

def A_star_with_PlayArea(maze, cols, rows, surface, block_size):
    for i in range(cols - 1):
        for j in range(rows - 1):
            if maze[i][j].start == True:
                openSet.append(maze[i][j])
            if maze[i][j].finish == True:
                end = _SpotC()
                end = maze[i][j]

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
                

        temp = current
        path = []
        path.append(temp)
        while(temp.previous !=  None):
            path.append(temp.previous)
            temp = temp.previous
       
        

    return path

