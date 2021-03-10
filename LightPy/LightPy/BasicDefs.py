import math
from LightPy.DataTypes import *

# No idea what this one does lmao
def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

# Return true if line segments AB and CD intersect
def intersect(A:tuple,B:tuple,C:tuple,D:tuple):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

# Return Dist from TwoPoints
def dist(point1:tuple, point2:tuple):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def clamp(value, Min, Max):
    return max(Min, min(value, Max))

def IntersectAtPoint(Point1:vector2, Point2:vector2, Walls):
    result = False
    if type(Walls) != list:
        Walls = [Walls]
    for x in range(0,len(Walls)):
        result = intersect(Point1.AsTuple(), Point2.AsTuple(), Walls[x].StartPoint.AsTuple(), Walls[x].EndPoint.AsTuple())
        if(result == True):
            return result
    return result
    