from LightPy import *

# Old One
# ((255 / (dist(cx,cy,lights[light][0],lights[light][1]) + 0.1)) * lights[light][2])


# Old One as text
#( (255 / ( dist(CurrentX, CurrentY, LightX, LightY) + 0.001) ) * Brightness)

# New one:
# ( 255 / ( dist(Point.AsTuple(), Light.pos.AsTuple()) + 0.001) ) * Light.Brightness

def CalcBrightnessFromPoint(Point:vector2, Light:LightObject):
    return ( 255 / (dist(Point.AsTuple(), Light.pos.AsTuple()) + 0.001)) * Light.Brightness

def CalcBrightSheet(Lights:list, Walls:list, size:tuple):
    FinishedTable = []
    for y in range(0,size[1]):
        FinishedTable.append([])
        for x in range(0,size[0]):
            brt = 0
            for l in range(0, len(Lights)):
                if(not IntersectAtPoint(Lights[l].pos,vector2(x,y),Walls)):
                    brt += CalcBrightnessFromPoint(vector2(x,y),Lights[l])
                brt = clamp(brt,0,255)
            FinishedTable[y].append(brt)
                
    return FinishedTable