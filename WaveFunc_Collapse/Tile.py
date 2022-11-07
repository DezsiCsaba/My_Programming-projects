import pygame
pygame.init()
from os import listdir
from math import pi


IMG_x = 0
IMG_y = 0
IMG_pos = (0,0)


def _import_img(img_path):
    img = pygame.image.load(str(img_path))
    return img


class Tile_C():
    image = pygame.surface
    up, right, down, left = [],[],[],[] 
    edges = str
    index = int 
    w, h = int, int

    def _TileInit (self, img, edges, DIM_of_img):
        self.image = img
        self.edges = edges
        self.up, self.right, self.down, self.left = [],[],[],[]

        self.w, self.h = DIM_of_img, DIM_of_img
        #if (i != None): self.index = i

    def rotate_tile(self, num):
        newimg = (self.image).copy()
        newimg = pygame.transform.rotate(newimg, 90 * num)

        newEdges = []
        for i in range(len(self.edges)):
            newEdges.append(self.edges[i-1 + len(self.edges) % len(self.edges)])

        tile = Tile_C()
        tile._TileInit(newimg, newEdges, self.h)
        return tile

    def _ShowTile(self, display, x, y):
        disptile = pygame.transform.scale(self.image, (self.h, self.w))
        display.blit(disptile, (x, y))