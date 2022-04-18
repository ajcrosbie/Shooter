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
    
    def die(self):
        return self.points


class fastTarg(target):
    def __init__(self, pos):
        speed = random.randrange(11,20)
        size = random.randrange(30, 60)
        size = (size, size)
        colour = (81, 134, 255)
        self.points = 10
        self.changeDirCount = random.randrange(20)
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

class diagonalTarg(target):
    def __init__(self, pos):
        speed = random.randrange(20, 22)
        size = random.randrange(50, 80)
        size = (size, size)
        self.points = 10
        colour = (255, 255, 255)
        self.changeDirCount = random.randrange(30)
        self.available = ["tr", "tl", "br", "bl"]
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
        if self.dir == "tr":
            self.pos = (self.pos[0]+self.speed//2, self.pos[1]-self.speed//2)
        elif self.dir == "tl":
            self.pos = (self.pos[0]-self.speed//2, self.pos[1]-self.speed//2)
        elif self.dir == "br":
            self.pos = (self.pos[0]+self.speed//2, self.pos[1]+self.speed//2)
        elif self.dir == "bl":
            self.pos = (self.pos[0]-self.speed//2, self.pos[1]+self.speed//2)

        self.dirCount = self.dirCount + 1

class bigTarg(target):
    def __init__(self, pos):
        speed = random.randrange(2, 5)
        size = random.randrange(80, 160)
        size = (size, size)
        colour = (0, 150, 255)
        self.health = 10
        self.points = 30
        self.changeDirCount = random.randrange(30)
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
    
    def die(self):
        self.colour = (self.colour[0], self.colour[1], self.colour[2]*self.health//10)
        if self.health == 0:
            return self.points
        else:
            self.health = self.health-1
            return "not today"

