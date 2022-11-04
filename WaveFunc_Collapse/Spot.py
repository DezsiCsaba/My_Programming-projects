from pickle import TRUE
from random import randint
import pygame 


class _SpotC:
    i = 0
    j = 0

    f = 0.0   #values needed for the A* 
    g = 0.0   #to calculate the 
    h = 0.0   #best possible next step

    neighbours = []   #a list containing all the neighboring spots
    

    previous = None #the prev spot

    wall = False
    start = False
    finish = False


    def _SpotInit_(self, _i, _j):
        self.i = _i
        self.j = _j
        self.start, self.finish = False, False
        self.wall = False
        if (randint(0,10) < 3):
            self.wall = True
        self.neighbours = []
        self.f = 0.0
        self.g = 0.0
        self.h = 0.0
        self.previous = None
        
    def ShowPoint(self, Surface, blockSize):
        if (self.start):
            pygame.draw.rect(Surface, (0,255,0), (self.i*blockSize, self.j*blockSize, blockSize-1, blockSize-1))
        elif (self.finish):
            pygame.draw.rect(Surface, (0,0,255), (self.i*blockSize, self.j*blockSize, blockSize-1, blockSize-1))
        elif (self.wall):
            pygame.draw.rect(Surface, (255,255,255), (self.i*blockSize, self.j*blockSize, blockSize-1, blockSize-1))
        else: pygame.draw.rect(Surface, (0,0,0), (self.i*blockSize, self.j*blockSize, blockSize-1, blockSize-1))

    def Show(self, Surface, blockSize, color):
            pygame.draw.rect(Surface, color, (self.i*blockSize, self.j*blockSize, blockSize, blockSize))
       

    def AddNeighbours(self, matrix, cols, rows):
        if (self.i < cols - 1):
            self.neighbours.append(matrix[self.i + 1][self.j])
        if (self.i > 0):
            self.neighbours.append(matrix[self.i - 1][self.j])
        if (self.j < rows - 1):
            self.neighbours.append(matrix[self.i][self.j + 1])
        if (self.j > 0):
            self.neighbours.append(matrix[self.i][self.j - 1])
