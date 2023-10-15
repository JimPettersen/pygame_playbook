from game.utilities.vector import Vector as V
import pygame as pg


class Snake:
    def __init__(self):
        self.head_pos = V.ZERO
        self.head_dir = V.RIGHT
        self.body = [
            self.head_pos,
            self.head_pos - self.head_dir,
            self.head_pos - self.head_dir * 2,
        ]
        self.speed = 1
        self.color = (0, 255, 0)
        self.growing = False

    def move(self):
        self.head_pos += self.head_dir * self.speed
        self.body.insert(0, self.head_pos)
        if not self.growing:
            self.body.pop()
        else:
            self.growing = False

    def change_direction(self, new_direction: V):
        if new_direction != -self.head_dir:
            self.head_dir = new_direction

    def grow(self):
        self.growing = True

    def check_collision_with_bounds(self, screen_width, screen_height):
        return (
            self.head_pos.x < 0
            or self.head_pos.x >= screen_width
            or self.head_pos.y < 0
            or self.head_pos.y >= screen_height
        )

    def check_collision_with_self(self):
        return self.head_pos in self.body[1:]

    def draw(self, screen):
        for segment in self.body:
            pg.draw.rect(screen, self.color, (*segment, 10, 10))
