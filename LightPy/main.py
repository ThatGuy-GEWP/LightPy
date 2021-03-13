import pygame, math, threading, numba
from numba import jit
from LightPy import *

pygame.init()

size = [600,600]

 
Lights = []
Walls = []

screen = pygame.display.set_mode(size)
pygame.display.set_caption("LightPy V1")

render = pygame.surface.Surface(size)

Quality = 5

def RenderBrights():
    Brights = CalcBrightSheet(Lights, Walls, size)
    for y in range(0,size[1]):
        for x in range(0,size[0]):
            brtFn = (Brights[y][x], Brights[y][x], Brights[y][x])
            pygame.draw.rect(render, brtFn, ((x,y),(1,1)))





done = False
clock = pygame.time.Clock()
WallCords = []

while not done:
    xy = pygame.mouse.get_pos()
    screen.blit(render,(0,0))

    # This limits the while loop to a max of x times per second.
    clock.tick()
    # Leave this out and we will use all CPU we can.


    if len(WallCords) > 0 and len(WallCords) < 2:
        pygame.draw.line(screen, (155,155,255), (WallCords[0][0], WallCords[0][1]), xy)
    elif len(WallCords) == 2:
        Walls.append(WallObject(vector2(WallCords[0][0], WallCords[0][1]), vector2(WallCords[1][0], WallCords[1][1])))
        WallCords = []


    for x in range(0,len(Walls)):
        pygame.draw.line(screen, (255,255,255), Walls[x].StartPoint.AsTuple(), Walls[x].EndPoint.AsTuple())

    for x in range(0,len(Lights)):
        pygame.draw.rect(screen, (255,155,255), ((Lights[x].pos.x - 5, Lights[x].pos.y - 5), (15,15)))



    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                Lights.append(LightObject(vector2(xy[0], xy[1]), 8))
                print(xy)
            if event.button == pygame.BUTTON_RIGHT:
                WallCords.append(xy)
                print(xy)
        if event.type == pygame.KEYUP:
            if event.key== pygame.K_RETURN:
                print(Lights)
                RenderBrights()

    #pygame.draw.rect(screen, (255,255,255), ((x,y),(1,1)))
    #pygame.draw.rect(screen, (Col3), ((PosX,PosY),(WidthX,HeightY)))

    pygame.display.update()
    pygame.draw.rect(screen, (0,0,0), ((0,0), (size[0],size[1])))