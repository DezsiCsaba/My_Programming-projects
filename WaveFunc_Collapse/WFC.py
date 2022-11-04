import pygame; pygame.init()


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

path = "Python\WaveFunc_Collapse\Coding_Train_Circuit/"

def _import_all_images_(dir): #given a directory, lists all the files within
    tileImages = []           # and appends all the files to a list
    
    for i in range(13):
        tileImages.append(pygame.image.load(str(path) + str(i) + ".png"))
    return tileImages
def displayIMG():
    for tiles in tileImages:
        tiles = pygame.transform.scale(tiles, (SIZE_of_IMG))
        canvas.blit(tiles, (0,0))


tileImages = _import_all_images_(path)
tiles = []

DontClose()
