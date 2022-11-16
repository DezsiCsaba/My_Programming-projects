from time import sleep

import numpy
import pygame
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
DIM = h/100
canvas = pygame.display.set_mode((h,w))
x,y = 0,0
for i in range(int(DIM)):
    x=0
    for j in range(int(DIM)):
        pygame.draw.rect(canvas, (255,255,255), (j*h/DIM, i*h/DIM, h/DIM-1, h/DIM-1))
        pygame.display.update()                
        x += 1
    y += 1

displacement = 70+15
red = (255,0,0)
green =(0,255,0)



first = Digit_C()
second = Digit_C()

first._digitInit_(0, 0)
first.DisplayDigit(canvas, red)
pygame.display.update() #megleneiti a piros elsőt
sleep(4)

second.DisplayDigit(canvas,green)
pygame.display.update()#megjeleniti a zöld masodikat 0,0-n
sleep(4)

second._digitInit_(120, 0)
first.DisplayDigit(canvas, red)
pygame.display.update() #piros, zöld
sleep(2)
second.DisplayDigit(canvas, green)




def Test():
    #Rect(left, top, width, height)
    long = 50
    short = 10
    displace = 15
    base = 0
    pygame.draw.rect(canvas, (255,0,0), (base+displace, base, long, short)) #A
    pygame.draw.rect(canvas, (255,0,0), (displace+long, short, short, long)) #B
    pygame.draw.rect(canvas, (255,0,0), (displace+long, long+2*short, short, long)) #C
    pygame.draw.rect(canvas, (255,0,0), (base+displace, 2*long+2*short, long, short)) #D
    pygame.draw.rect(canvas, (255,0,0), (displace-short, long+2*short, short, long)) #E
    pygame.draw.rect(canvas, (255,0,0), (displace-short, short, short, long)) #F
    pygame.draw.rect(canvas, (255,0,0), (base+displace, long+short, long, short)) #G


DontClose()