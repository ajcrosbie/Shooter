import random

import pygame


class target():
    def __init__(self, pos, size, colour, speed=0):
        self.pos = pos
        self.speed = speed
        self.colour = colour
        self.size = size

    def draw(self, win):
        pygame.draw.rect(win, self.colour, ((self.pos), self.size))
    

