import pygame, math, numba
import numpy as np

from numba import jit
from LightPy import *

#CONTROLS:
# Left Click: Place Ligt
# Right Click: Wall Placement
# Enter: Start Render


size = [600,600]
Lights = []
Walls = []
WallCords = []
clock = pygame.time.Clock()
done = False


pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("LightPy V1 - Stable Branch")

ico = pygame.surface.Surface((50,50));
pygame.draw.rect(ico, (155,155,155), ((0,0), (50,50)))
pygame.display.set_icon(ico)




render = pygame.surface.Surface(size)

def RenderBrights():
    Ls = np.array(Lights)
    Ws = np.array(Walls)


    Brights = CalcBrightSheet(Ls, Ws, size)
    Brights = np.array(Brights)

    for y in range(0,size[1]):
        for x in range(0,size[0]):
            brtFn = (Brights[y][x], Brights[y][x], Brights[y][x])
            pygame.draw.rect(render, brtFn, ((x,y),(1,1))) # Draw onto Render, so we dont have to redraw every frame. only once and save the result

while not done:
    xy = pygame.mouse.get_pos()
    screen.blit(render,(0,0)) # Blit Custom surface nammed Render onto screen.

    # This limits the while loop to a max of x times per second.
    clock.tick(0)
    # Leave it empty or as 0 and we will use all the CPU we can.
    # MAXIMUM POWAAAA!!!

    if len(WallCords) > 0 and len(WallCords) < 2:
        pygame.draw.line(screen, (155,155,255), (WallCords[0][0], WallCords[0][1]), xy) # Starts Drawing Lines for wall creation
    elif len(WallCords) == 2:
        Walls.append([(WallCords[0][0], WallCords[0][1]),(WallCords[1][0], WallCords[1][1])])
        WallCords = []


    for x in range(0,len(Walls)):
        pygame.draw.line(screen, (255,255,255), Walls[x][0], Walls[x][1]) # Draws All Walls as lines

    for x in range(0,len(Lights)):
        pygame.draw.rect(screen, (255,155,255), ((Lights[x].pos.x - 5, Lights[x].pos.y - 5), (15,15))) # Draws All Lights as colored Boxes



    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT: #On Left click, place a light object at mouse pos.
                Lights.append(LightObject(vector2(xy[0], xy[1]), 8))
                print(xy)
            if event.button == pygame.BUTTON_RIGHT: #On Right click, place a wall point, once two points are placed, it makes a wall.
                WallCords.append(xy)
                print(xy)

        if event.type == pygame.KEYUP:
            if event.key== pygame.K_RETURN: #On Enter or "return" pressed, Render.
                RenderBrights()

    #pygame.draw.rect(screen, (255,255,255), ((x,y),(1,1))) ~ Refrence stuff because i frequently forget pygame functions
    #pygame.draw.rect(screen, (Col3), ((PosX,PosY),(WidthX,HeightY))) ~ Refrence stuff because i frequently forget pygame functions

    pygame.display.update() #When Called, Anything drawn to the screen surface gets rendered to the window
    pygame.draw.rect(screen, (0,0,0), ((0,0), (size[0],size[1]))) # Clear screen surface, and since we dont update after, the screen keeps the current frame