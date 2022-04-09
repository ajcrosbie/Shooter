import pygame
import random
import Targets


def redrawWindow(win, targs):
    win.fill((25,100,25))
    for targ in targs:
        targ.draw(win)
    pygame.display.update()

def newTarg(WIDTH, type):
    pos = (random.randrange(WIDTH-20), random.randrange(WIDTH-20))
    colour = (255, 255, 255)
    return Targets.target(pos, (100, 100), colour) # to be changed when types are added


def shooter(targs, WIDTH):
    mouse = pygame.mouse.get_pos()
    for i in targs:
        if mouse[0] > i.pos[0] and mouse[0] < i.pos[0]+i.size[0]:
            if mouse[1] > i.pos[1] and mouse[1] < i.pos[1]+i.size[1]:
                tempTargs = targs.copy()
                tempTargs.remove(i)
                tempTargs.append(newTarg(WIDTH, 0))
                return tempTargs
    return targs
    


def runEvent(targs, WIDTH):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("fuck go back")
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            targs = shooter(targs, WIDTH)
    return targs


def main():
    targs = []
    WIDTH = 500
    win = pygame.display.set_mode((WIDTH, WIDTH))
    targs.append(newTarg(WIDTH, 0))
    for i in range(100000):
        redrawWindow(win, targs)
        targs = runEvent(targs, WIDTH)

if __name__ == "__main__":
    main()