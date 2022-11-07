import pygame; pygame.init()
from Tile import Tile_C
from Cell import Cell_C
from random import randint
import random



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

path1 = "Python\WaveFunc_Collapse\Coding_Train_Circuit/"
path2 = "Python\WaveFunc_Collapse\Demo_Tiles\blank.png"
def _import_all_images_(dir): #given a directory, lists all the files within
    tileImages = []           # and appends all the files to a list
    
    for i in range(13):
        tileImages.append(pygame.image.load(str(dir) + str(i) + ".png"))
    return tileImages
def load_demo_tiles():
    tiles=[]
    tiles.append(pygame.image.load("Python\WaveFunc_Collapse\Demo_Tiles/blank.png"))
    tiles.append(pygame.image.load("Python\WaveFunc_Collapse\Demo_Tiles/up.png"))
    #tiles.append(pygame.transform.rotate(tiles[0], pi/2 * 1))
    return tiles
def displayIMG():
    x = 0
    for tile in tiles:
        tile = pygame.transform.scale(tile.image, (SIZE_of_IMG))
        canvas.blit(tile, (0, x))
        x +=  DIM_of_img
def DrawAllTiles(tileList):
    index = 0
    y = 0
    x = 0
    for i in range(len(tileList)):
        tileList[index]._ShowTile(canvas, x,y)
        index += 1
        if (x == w-DIM_of_img): x = 0; y += DIM_of_img
        x += DIM_of_img
#tileImages = _import_all_images_(path1)
tileImages = load_demo_tiles()

tiles = []
#Tiles_C takes no argument -> mindegyiket meg kell csinalni kulon es meghivni egyesevel a constructor functciont
def DemoTiles():
    tile1 = Tile_C()
    tile2 = Tile_C()
    tile3 = Tile_C()
    tile4 = Tile_C()
    tile5 = Tile_C()

    tile1._TileInit(tileImages[0], [0,0,0,0], DIM_of_img)
    tile2._TileInit(tileImages[1], [1,1,0,1], DIM_of_img)
    tile3 = tile2.rotate_tile(1)
    tile4 = tile2.rotate_tile(2)
    tile5 = tile2.rotate_tile(3)

    tiles.append(tile1)
    tiles.append(tile2)
    tiles.append(tile3)
    tiles.append(tile4)
    tiles.append(tile5)

#displayIMG()
DemoTiles()


def _WCF():
    grid = []
    for i in range(DIM_of_canvas*DIM_of_canvas):
        gridi = Cell_C()
        gridi._CellInit()
        gridi.collapsed = False
        gridi.options = [tiles[0], tiles[1], tiles[2],tiles[3], tiles[4]]
        grid.append(gridi)
    # -----Hardcoded values for debugging
    #grid[0].collapsed = True
    #grid[10].options = [tiles[1], tiles[4]]
    #grid[0].options = [tiles[0], tiles[2]]
    #grid[2].options = [tiles[1], tiles[4]]
    
    # -----Pick cell with the lowest entropy
    copyOfGrid = grid.copy()
    copyOfGrid.sort(key = lambda x: len(x.options))
    
    for i in range(len(copyOfGrid)):
        if (len(copyOfGrid[i].options) == len(copyOfGrid[0].options)):
            filtered.append(copyOfGrid[i])
    
    
    cell = random.choice(filtered)
    cell.collapsed = True
    pick = random.choice(cell.options)
    cell.options = [pick]
    print(pick.image)

    x,y = 0,0
    index = 0
    for i in range(DIM_of_canvas):
        x=0
        for j in range(DIM_of_canvas):
            if (grid[index].collapsed == True):
                grid[index].options[0]._ShowTile(canvas, x*DIM_of_img, y*DIM_of_img)
            else:
                pygame.draw.rect(canvas, (255,0,0), (j*DIM_of_img, i*DIM_of_img, DIM_of_img-1, DIM_of_img-1))
            index += 1
            x += 1
        y += 1
    
    
    nextTiles = []
    for i in range(DIM_of_canvas):
        for j in range(DIM_of_canvas):
            index = j + i * DIM_of_canvas
            if (grid[index].collapsed):
                nextTiles.append(grid[index])
            else:
                #above
                pass
                #right

                #down

                #left
    
    
    return (filtered)
filtered = []
filtered = _WCF()
print(len(filtered))
#DrawAllTiles(tiles)
DontClose()