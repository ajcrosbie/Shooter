import random
import pygame


class target():
    def __init__(self, pos, size, colour, speed=0):
        self.pos = pos
        self.speed = speed
        self.colour = colour
        self.size = size
        self.dirCount = 0

    def draw(self, win, width):
        if self.pos[0] >width:
            self.pos = (0, self.pos[1])
        if self.pos[0] < 0:
            self.pos = (width, self.pos[1])

        if self.pos[1] > width:
            self.pos = (self.pos[0], 0)
        if self.pos[1] < 0:
            self.pos = (self.pos[0], width)
        
        
        if self.pos[0] + self.size[0] > width:
            pygame.draw.rect(win, self.colour, ((0, self.pos[1]), (self.pos[0]+self.size[0]-width, self.size[1])))
        if self.pos[1] + self.size[1] > width:
            pygame.draw.rect(win, self.colour, ((self.pos[0], 0), (self.size[0] ,self.pos[1]+self.size[1]-width)))

        pygame.draw.rect(win, self.colour, ((self.pos), self.size))
    
    def move(self):
        raise NotImplementedError("must override move")
    
    def changeDir(self):
        raise NotImplementedError("must override move")

class fastTarg(target):
    def __init__(self, pos, size, colour):
        speed = random.randrange(8,15)
        self.changeDirCount = random.randrange(50)
        self.available = ["l", "r", "u", "d"]
        self.dir = random.choice(self.available)
        super().__init__(pos, size, colour, speed)

    def changeDir(self):
        tempavailable = self.available.copy()
        tempavailable.remove(self.dir)
        self.dir = random.choice(tempavailable)


    def move(self):
        if self.dirCount == self.changeDirCount:
            self.changeDir()
            self.dirCount=0
        if self.dir == "l":
            self.pos = (self.pos[0]-self.speed, self.pos[1])
        elif self.dir == "r":
            self.pos = (self.pos[0]+self.speed, self.pos[1])
        elif self.dir == "u":
            self.pos = (self.pos[0], self.pos[1]-self.speed)
        elif self.dir == "d":
            self.pos = (self.pos[0], self.pos[1]+self.speed)

        self.dirCount = self.dirCount + 1

