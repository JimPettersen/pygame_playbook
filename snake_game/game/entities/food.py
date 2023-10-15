import pygame as pg
from random import randint
from game.utilities.vector import Vector as V


class Food:
    def __init__(self, screen_width, screen_height):
        self.position = V(randint(0, screen_width - 10), randint(0, screen_height - 10))
        self.color = (255, 0, 0)
        self.size = 10

    def respawn(self, screen_width, screen_height):
        self.position = V(
            randint(0, screen_width - self.size), randint(0, screen_height - self.size)
        )

    def draw(self, screen):
        pg.draw.rect(screen, self.color, (*self.position, self.size, self.size))
