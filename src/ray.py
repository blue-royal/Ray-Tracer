from cmath import pi
from numpy import arccos
from colour import *
class Ray:
    def __init__(self, startPos, dirVec):
        self.pos = startPos
        self.dir = dirVec.normalise()
        self.colour = self.getColour()
        
    def getColour(self):
        # say the light is at 2, 5, 1
        light = Vec3(0, 1, 0)
        # use a sphere at 0, 0, 2 of radius 0.5
        center = Vec3(0.1, 0, 1.13)
        rad = 1
        return self.checkSphereCollision(center, rad, light)
    
    
    def checkSphereCollision(self, center, rad, light):
        
        b = self.dir.dot(self.pos - center)
        c = (self.pos - center).magnitude()**2 - rad**2
        discriminant = b**2-(4*c)
        if discriminant >= 0:
            ans1 = -b + discriminant**0.5
            ans2 = -b - discriminant**0.5
            if ans1 < 0 and ans2 < 0:
                return Colour(0, 0, 200)
            elif ans1 < 0 and ans2 >= 0:
                closestHit = ans2
            elif ans1 >= 0 and ans2 < 0:
                closestHit = ans1
            elif ans1 > ans2:
                closestHit = ans2
            elif ans1 < ans2:
                closestHit = ans1
            collisionPoint = self.pos + (self.dir * closestHit)
            normal = collisionPoint - center
            toLight = collisionPoint - light
            angle = arccos(normal.dot(toLight) / (normal.magnitude() * toLight.magnitude()))
            scalar = (0.5*pi)/angle
            
            
            
            b = toLight.dot(collisionPoint - center)
            c = (self.pos - center).magnitude()**2 - rad**2
            if b**2-(4*c) > 0:
                scalar = 0.1
            
            return Colour(100, 100, 200) * scalar
        return Colour(0, 0, 200)
    
    def checkTriangleCollisions(self):
        # define triangle points
        points = [Vec3(-1, 1, 2), Vec3(1, 1, 3), Vec3(0, -1, 1)]
        normal = (points[2]-points[0]).cross(points[1]-points[0])
        
