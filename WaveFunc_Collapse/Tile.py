import pygame
pygame.init()
from os import listdir


IMG_x = 0
IMG_y = 0
IMG_pos = (0,0)


def _import_img(img_path):
    img = pygame.image.load(str(img_path))
    return img
class Tile():
    image = pygame.image
    up, right, down, left = [],[],[],[] 
    edges = str
    index = int 
    w, h = int

    def _init (self, img, edges, i, DIM_of_img):
        self.image = img
        self.edges = edges
        self.up, self.right, self.down, self.left = [],[],[],[]

        self.w, self.h = DIM_of_img
        if (i != None): self.index = i

    def rotate(self, num):
        pass
