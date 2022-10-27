from collections import namedtuple
from enum import Enum
import pygame
import numpy as np
import random
from random import randint

pygame.init()
font = pygame.font.Font('freesansbold.ttf', 15)
Point = namedtuple('Point', 'x,y')

#----------------COLORS----------------
white = (255, 255, 255)
transp_white = (255,255,255,127)
red = (255, 0, 0)
blue = (0, 0, 125)
green = (0, 125, 0)
transp_green = (0, 125, 0, 150)
black = (0, 0, 0)
#----------------COLORS----------------

class Direction(Enum):
    Right = 1; Left = 2; Up = 3; Down = 4
snake_block = 10 #size of blocks(snake & food) -> 10 = 10x10px



class SnakeGame:
    def __init__(self, width = 640, height = 480):
        self.width = width
        self.height = height
        self.canvas = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("AI_Learns_to_play_Snake")
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.direction = Direction.Up
        self.head = Point(self.width/2, self.height/2)
        self.snake =[self.head,
                        Point(self.head.x - snake_block, self.head.y),
                        Point(self.head.x - (2*snake_block), self.head.y)
                    ]
        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0

    def _place_food(self):
        x = random.randint(0, (self.width-snake_block) // snake_block) * snake_block
        y = random.randint(0, (self.width-snake_block) // snake_block) * snake_block
        self.food = Point(x,y)
        if self.food in self.snake:
            self._place_food()

    def play_step(self, action):
        self.frame_iteration += 1
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
                quit()

        self.move(action)
        self.snake.insert(0, self.head)


        reward = 0
        game_over = False
        if self._is_colliding() or self.frame_iteration > 100*(len(self.snake)):
            game_over = True
            reward = -10
            return reward, game_over, self.score

        if self.head == self.food:
            self.score  += 1
            reward = 10
            self._place_food()
        else: self.snake.pop()


        self.update_ui()
        self.clock.tick(24)

        return reward, game_over, self.score

    def _is_colliding(self, pt = None):
        if pt is None:
            pt = self.head
        if pt.x > self.width - snake_block or pt.x < 0 or pt.y > self.height - snake_block or pt.y < 0:
            return True
        return False

    def update_ui(self):
        self.display.fill(black)

        for pt in self.snake:
            pygame.draw.rect(self.display, blue, pygame.Rect(pt.x, pt.y, snake_block, snake_block))
        
        pygame.draw.rect(self.display, red, pygame.Rect(self.food.x, self.food.y, snake_block, snake_block))
        
        text = font.render("Score: " + str(self.score), True, white)
        self.display.blit(text, [0,0])
        pygame.display.flip()

    def _move(self, action):
        clock_wise = (Direction.Right, Direction.Down, Direction.Left, Direction.Up)
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx] # no change
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx] # right turn r -> d -> l -> u
        else: # [0, 0, 1]
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx] # left turn r -> u -> l -> d

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += snake_block
        elif self.direction == Direction.LEFT:
            x -= snake_block
        elif self.direction == Direction.DOWN:
            y += snake_block
        elif self.direction == Direction.UP:
            y -= snake_block

        self.head = Point(x, y)

    def DontClose():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    pygame.quit()



