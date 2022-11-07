import pygame; pygame.init()
from Tile import Tile_C
from math import pi

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
DIM_of_canvas = 10  # 10 -> 10 x 10 tiles
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
DrawAllTiles(tiles)
DontClose()