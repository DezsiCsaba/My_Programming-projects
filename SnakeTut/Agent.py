import random
import numpy as np
from Game import SnakeGame, Direction, Point


MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001


class Agent:
    def _init_(self):
        self.n_games = 0
        self.epsilon = 0
        self.gamma = 0.9


















