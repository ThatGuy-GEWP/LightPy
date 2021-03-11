import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, math
import threading, multiprocessing
from multiprocessing import Process
from LightPy import *

global FinalSheet

FinalSheet = []

def RenderThread1(Sizex,Sizey,Lights,Walls,Q,ID):
    Size = (Sizex,Sizey)
    print("StartCalc")
    FinalList = CalcBrightSheet(Lights,Walls,Size)
    Q.put(1)
    print("Finished, POG")

def RenderBrights(RenderBuffer, size, Lights, Walls):

    ThreadAmmount = 32
    ThreadStep = math.floor(size[1] / ThreadAmmount)
    Threads = []
    Q = multiprocessing.Queue()

    FinalSheet = []

    for x in range(ThreadAmmount):
        Threads.append(Process(target=RenderThread1, args=(size[0], ThreadStep*(x+1),Lights,Walls,Q,x)))

    for x in range(0, len(Threads)):
        Threads[x].start()

    for x in range(0, len(Threads)):
        print("Joining Thread", x)
        Threads[x].join()
        print("get")
        Q.get_nowait()
        print("got")


    print("All Joined")

    print(FinalSheet)

    for y in range(size[1]):
        for x in range(size[0]):
            brt = FinalSheet[y][x]
            pygame.draw.rect(RenderBuffer, (brt,brt,brt), ((x,y), (1,1)))




if __name__ == "__main__":
    pygame.init()
    size = [600,600]
    Lights = []
    Walls = []
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("LightPy V1")
    render = pygame.surface.Surface(size)
    renderBuffer = pygame.surface.Surface(size)
    Quality = 5
    done = False
    clock = pygame.time.Clock()
    WallCords = []

    while not done:
        screen.blit(render,(0,0))
        xy = pygame.mouse.get_pos()
    
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
                    RenderBrights(renderBuffer, size, Lights, Walls)
    
        #pygame.draw.rect(screen, (255,255,255), ((x,y),(1,1)))
        #pygame.draw.rect(screen, (Col3), ((PosX,PosY),(WidthX,HeightY)))
    
        pygame.display.update()
        pygame.draw.rect(screen, (0,0,0), ((0,0), (size[0],size[1])))