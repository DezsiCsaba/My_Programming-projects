import pygame
from random import randint
from time import sleep
from os import listdir

pygame.init()
def DontClose():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
            pygame.display.update()
pygame.display.set_caption("Wave_Function_Collapse")

h = 400
w = h
DIM_of_canvas = 10  # 10 -> 10 x 10
DIM_of_img = int(h/DIM_of_canvas)
SIZE_of_IMG = (DIM_of_img, DIM_of_img)
canvas = pygame.display.set_mode((h,w))

path = "Coding_Train_Circuit/"

IMG_x = 0
IMG_y = 0
IMG_pos = (0,0)

def _import_all_images_(dir):
    tileImages = []
    imgs = listdir(dir)
    for img_dir in imgs:
        tileImages.append(pygame.image.load(str(path) + str(img_dir)))
    return tileImages
def FillTheScreen(tileImages):
    IMG_x = 0
    IMG_y = 0
    for i in range(DIM_of_canvas):
        for j in range(DIM_of_canvas):
            IMG_pos = (IMG_x, IMG_y)
            index = randint(0,11)
            tileImages[index] = pygame.transform.scale(tileImages[index], (SIZE_of_IMG ))
            canvas.blit(tileImages[index], (IMG_pos))
            IMG_x += DIM_of_img
            pygame.display.update()
            sleep(0.1)
        IMG_y += DIM_of_img
        IMG_x = 0


tileIMGs = _import_all_images_("Coding_Train_Circuit")
FillTheScreen(tileIMGs)
pygame.display.update()
DontClose()