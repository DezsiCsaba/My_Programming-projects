import pygame
from Tile import _import_all_images_, _import_img

pygame.init()
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


DontClose()