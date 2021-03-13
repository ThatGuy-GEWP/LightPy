import math, numba
from LightPy.DataTypes import *
from numba import jit

# No idea what this one does lmao
@jit(nopython=True)
def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

# Return true if line segments AB and CD intersect
@jit(nopython=True)
def intersect(A:tuple,B:tuple,C:tuple,D:tuple):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

# Return Dist from TwoPoints
@jit(nopython=True)
def dist(point1:tuple, point2:tuple):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

@jit(nopython=True)
def clamp(value, Min, Max):
    return max(Min, min(value, Max))

def IntersectAtPoint(Point1:tuple, Point2:tuple, Walls):
    result = False
    for x in range(0,len(Walls)):
        result = intersect(Point1, Point2, Walls[x][0], Walls[x][1])
        if(result == True):
            return result
    return result
    

clamp(0,0,1)
ccw((0,0),(0,0),(0,0))
intersect((0,0),(0,0),(0,0),(0,0))
