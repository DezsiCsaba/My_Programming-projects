import pygame; pygame.init()
from Tile import Tile_C
from Cell import Cell_C
from random import randint
import random
import numpy as np
from time import sleep


pygame.display.set_caption("Wave_Function_Collapse")
def DontClose():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
            pygame.display.update()

h = 400
w = h
canvas = pygame.display.set_mode((h,w))
DIM_of_canvas = 5  # 10 -> 10 x 10 tiles
DIM_of_img = int(h/DIM_of_canvas)
SIZE_of_IMG = (DIM_of_img, DIM_of_img)


def _setup():
    #tileimages = np.empty[2, pygame.image]
    
    tiles = np.empty(5, Tile_C)
    img1 = pygame.image.load("Python\WaveFunc_Collapse\Demo_Tiles/blank.png")
    img2 = pygame.image.load("Python\WaveFunc_Collapse\Demo_Tiles/up.png")
    
    tile0 = Tile_C()
    tile1 = Tile_C()
    tile2 = Tile_C()
    tile3 = Tile_C()
    tile4 = Tile_C()

    tile0._TileInit(img1, [0,0,0,0], DIM_of_img)
    tile1._TileInit(img2, [1,1,0,1], DIM_of_img)
    tile2 = tile1.rotate_tile(1)
    tile3 = tile1.rotate_tile(2)
    tile4 = tile1.rotate_tile(3)

    tiles[0] = tile0
    tiles[1] = tile1
    tiles[2] = tile2
    tiles[3] = tile3
    tiles[4] = tile4
    for i in range(len(tiles)):
        tiles[i].index = i
    

    #Generate adjacency based on the edges of Tile_C objects
    for i in range(len(tiles)):
        tile = tiles[i]
        tile._analyze(tiles)

    return tiles


def _startOver(grid):
    #Create cell for each spot on the grid
    for i in range(DIM_of_canvas * DIM_of_canvas):
        grid[i] = Cell_C()
        grid[i]._CellInit((len(tiles)))
    print("   _startover_")


def _checkValid(arr, valid):
    indexer = arr.size - 1
    while indexer >= 0:
        element = arr[indexer]
        if (element not in valid):
            arr = arr[indexer : 1]
            break
        indexer += -1
            

def WFC():
    grid = outerGrid.copy()
    imgDim = DIM_of_img
    x,y = 0,0
    #grid[3].collapsed = True
    #grid[3].options = [tiles[2]]
    #grid[1].collapsed = True
    #grid[1].options = [tiles[2], tiles[3]]

    for i in range(DIM_of_canvas):
        x=0
        for j in range(DIM_of_canvas):
            cell = grid[ j + i * DIM_of_canvas]
            if (cell.collapsed == True):
                index = cell.options[0]
                tiles[index]._ShowTile(canvas, x*imgDim, y*imgDim)
                #index._ShowTile(canvas, x*imgDim, y*imgDim)
            else:
                pygame.draw.rect(canvas, (0,50,0), (j*imgDim, i*imgDim, imgDim-1, imgDim-1))
            pygame.display.update()
            if(DIM_of_canvas < 4): sleep(0.1)
            elif(DIM_of_canvas >= 4 and DIM_of_canvas < 15): sleep(0.005)          
            x += 1
        y += 1

    #Pick the cell with the lowest entropy(the number of possible options)
    gridlist = []
    for i in range(len(grid)):
        if(grid[i].collapsed == False): gridlist.append(grid[i]) #filtering the non collapsed cells into the list
    gridlist.sort(key = lambda x: len(x.options))
    gridCopy = np.asarray(gridlist) #converting the list to a numpy array
    
    if (gridCopy.size == 0):
        return
    else: length = len(gridCopy[0].options)
    stopIndex = 0
    for i in range(len(gridCopy)):
        if (len(gridCopy[i].options) > length):
            stopIndex = i
            break

    if stopIndex > 0:
        gridCopy = gridCopy[0:stopIndex]
    cell = random.choice(gridCopy)
    cell.collapsed = True
    pick = random.choice(cell.options)
    if (pick == None):
        _startOver(grid)

    cell.options = [pick]

    nextGrid = np.empty(DIM_of_canvas*DIM_of_canvas, Cell_C)
    for j in range(DIM_of_canvas-1):
        for i in range(DIM_of_canvas-1):
            index = i + j * DIM_of_canvas
            if (grid[index].collapsed):
                nextGrid[index] = grid[index]
            else:
                options = np.full((len(tiles)), i)
                #---look up
                if(j > 0):
                    up = grid[i + (j-1) * DIM_of_canvas]
                    validOptions = np.full((len(tiles)), None)
                    for option in up.options:
                        valid = tiles[option].down
                        validOptions = np.concatenate((validOptions, valid))
                    _checkValid(options, validOptions)

                #---look right
                if(i < DIM_of_canvas -1):
                    right = grid[i + 1 + j * DIM_of_canvas]
                    validOptions = np.empty((len(tiles)))
                    for option in right.options:
                        valid = tiles[option].left
                        validOptions = np.concatenate((validOptions, valid))
                    _checkValid(options, validOptions)

                #---look down
                if(j < DIM_of_canvas-1):
                    down = grid[i + (j+1) * DIM_of_canvas]
                    validOptions = np.empty((len(tiles)))
                    for option in down.options:
                        valid = tiles[option].up
                        validOptions = np.concatenate((validOptions, valid))
                    _checkValid(options, validOptions)

                #---look left
                if(i > 0):
                    left = grid[i - 1 + j * DIM_of_canvas]
                    validOptions = np.empty((len(tiles)))
                    for option in left.options:
                        valid = tiles[option].right
                        validOptions = np.concatenate((validOptions, valid))
                    _checkValid(options, validOptions)
                
                nextGrid[index] = Cell_C()
                nextGrid[index]._CellInit(options)
    
    grid = nextGrid.copy()
    pygame.display.update()
    
    


tiles = _setup()
outerGrid = np.empty((DIM_of_canvas*DIM_of_canvas), Cell_C)
_startOver(outerGrid)

for i in range(len(outerGrid) + 1): WFC(); print(i)
pygame.display.update()












DontClose()