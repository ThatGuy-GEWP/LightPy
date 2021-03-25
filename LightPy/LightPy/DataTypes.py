from LightPy import *

#Stuff here is mostly for readability in other scripts.

class vector2():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def SetPos(self, targX, targY):
        self.x = x
        self.y = y
    def AsTuple(self):
        return (self.x,self.y)

class LightObject():
    def __init__(self, pos:vector2, Brightness):
        self.pos = pos
        self.Brightness = Brightness

class WallObject():
    def __init__(self, StartPoint:vector2, EndPoint:vector2):
        self.StartPoint = StartPoint
        self.EndPoint = EndPoint
