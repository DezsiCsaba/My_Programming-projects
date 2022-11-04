import pygame
pygame.init()
from os import listdir



path = "Coding_Train_Circuit/"

IMG_x = 0
IMG_y = 0
IMG_pos = (0,0)

def _import_all_images_(dir): #given a directory, lists all the files within
    tileImages = []           # and appends all the files to a list
    imgs = listdir(dir)
    for img_dir in imgs:
        tileImages.append(pygame.image.load(str(path) + str(img_dir)))
    return tileImages

def _import_img(img_path):
    img = pygame.image.load(str(img_path))
    return img


class Tile():
    def _init(self):
        pass


    