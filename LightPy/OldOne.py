import pygame, math
import threading
import pygame.gfxdraw

pygame.init()

size = [600,600]

cx = 0
cy = 0


lights = {1:(200,190,1)  ,  2:(315,225,1)  ,  3:(250,325,1)}

walls = {1:(300,200,300,250),2:(300,200,400,200),3:(215,310,275,310), 4:(500,200,500,250),5:(100,200,100,250)}

print(lights[1][2])




col = 0

a = (300,200)
b = (300,250)




def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)



def dist(x1,y1,x2,y2):
 return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def calCol():
 global col
 SomethingInWay = False
 for light in lights:
  for wall in walls:
    SomethingInWay = intersect((walls[wall][0], walls[wall][1]) , (walls[wall][2], walls[wall][3]), (lights[light][0], lights[light][1]), (cx,cy))
    if SomethingInWay == False:
        col = col +  ((255 / (dist(cx,cy,lights[light][0],lights[light][1]) + 0.1)) * lights[light][2])



quality = 3

screen = pygame.display.set_mode(size)
pygame.display.set_caption("HQ Light Rendering")
f = []
# pygame.draw.circle(surface, color, center, 0)

done = False
clock = pygame.time.Clock()

br = 0
e = False
z = 0

while not done:
    
    # This limits the while loop to a max of x times per second.
    clock.tick()
    # Leave this out and we will use all CPU we can.

 
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONUP:
          xy = pygame.mouse.get_pos()
          print(xy)
          #br = lights[1][2]
          #lights[1] = {xy[0],xy[1],br}
          #print(lights[1])
          #quality = 0
          #quality = 6
          #screen.fill((0,0,0))
    
    
    for x in range(quality):
     cy = 0
     cx = 0
     for x in range(size[1]):
      if cy == size[1]:
       break
      for x in range(size[0]):

       #for light in lights:
        #for wall in walls:
        #  if intersect((walls[wall][0], walls[wall][1]) , (walls[wall][2], walls[wall][3]), (lights[light][0], lights[light][1]), (cx,cy)) == True:
        #    pass
        #  else:
        #    col = col +  ((255 / (dist(cx,cy,lights[light][0],lights[light][1]) + 0.1)) * lights[light][2])
        
        calCol()
        col = round(col)

        #col = col +  ((255 / (dist(cx,cy,lights[x][0],lights[x][1]) + 0.1)) * lights[x][2])

        if col >= 255:
          col = 255
        if col <= 0:
          col = 0


        pygame.draw.circle(screen,(col,col,col),(cx,cy),quality - 1)
        col = 0
        cx = cx + quality

      cx = 0
      z = 0
      cy = cy + quality
      for x in walls:
       pygame.draw.line(screen,(255,255,255),(walls[x][0],walls[x][1]),(walls[x][2],walls[x][3]))
      pygame.display.update()
     print("update",quality,"   ")
     
     quality = quality - 1
     
     if quality == 0:
       break
    
    
   