from turtle import width
import pygame
import random
import Targets


def redrawWindow(win, targs, width):
    win.fill((25,100,25))
    for targ in targs:
        targ.draw(win, width)
    pygame.display.update()

def newTarg(WIDTH, type):
    pos = (random.randrange(WIDTH-20), random.randrange(WIDTH-20))
    i = random.randrange(3)
    if i == 0:
        return Targets.bigTarg(pos) # to be changed when types are added
    elif i == 1:
        return Targets.diagonalTarg(pos) # to be changed when types are added
    elif i == 2:
        return Targets.fastTarg(pos) # to be changed when types are added

def shooter(targs, WIDTH):
    mouse = pygame.mouse.get_pos()
    for i in targs:
        if mouse[0] > i.pos[0] and mouse[0] < i.pos[0]+i.size[0]:
            if mouse[1] > i.pos[1] and mouse[1] < i.pos[1]+i.size[1]:
                tempTargs = targs.copy()
                if i.die() == "not today":
                    pass
                else:
                    points = i.die()
                    tempTargs.remove(i)
                    tempTargs.append(newTarg(WIDTH, 0))
                    return tempTargs

        if i.pos[0]+i.size[0] > WIDTH:
            if mouse[0] > 0 and mouse[0] < i.pos[0]+i.size[0]-WIDTH:
                if mouse[1] > i.pos[1] and mouse[1] < i.pos[1]+i.size[1]:
                    tempTargs = targs.copy()
                    if i.die() == "not today":
                        pass
                    else:
                        points = i.die()
                        tempTargs.remove(i)
                        tempTargs.append(newTarg(WIDTH, 0))
                        return tempTargs

        if i.pos[1]+i.size[1] > WIDTH:
            if mouse[1] > 0 and mouse[1] < i.pos[1]+i.size[1]-WIDTH:
                if mouse[0] > i.pos[0] and mouse[0] < i.pos[0]+i.size[0]:
                    tempTargs = targs.copy()
                    if i.die()=="not today":
                        pass
                    else:
                        points = i.die()   
                        tempTargs.remove(i)
                        tempTargs.append(newTarg(WIDTH, 0))
                        return tempTargs
    return targs
    


def runEvent(targs, WIDTH):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            targs = shooter(targs, WIDTH)
    for targ in targs:
        targ.move()
    return targs


def main():
    targs = []
    WIDTH = 500
    win = pygame.display.set_mode((WIDTH, WIDTH))
    targs.append(newTarg(WIDTH, 0))
    clock = pygame.time.Clock()
    for i in range(100000):
        pygame.time.delay(60)
        clock.tick(60)
        targs = runEvent(targs, WIDTH)
        redrawWindow(win, targs, WIDTH)

if __name__ == "__main__":
    main()