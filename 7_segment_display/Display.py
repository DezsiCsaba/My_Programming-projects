import pygame
import numpy
from Digit import Digit_C



pygame.display.set_caption("7_Segment_Display")
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

first = Digit_C()
first._digitInit_()

first.SegmentSwitch("A", True)
first.SegmentSwitch("D", "on")
first.DisplayDigit(1)
DontClose()