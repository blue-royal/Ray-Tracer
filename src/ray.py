from math import pi, sqrt
from numpy import arccos
from colour import *
class Ray:
    def __init__(self, startPos, dirVec):
        self.pos = startPos
        self.dir = dirVec.normalise()
        self.getColour()
        
    def getColour(self):
        self.colour = Colour(0, 0, 255)
        # say the light is at 2, 5, 1
        light = Vec3(0, 1, 7)
        # use a sphere at 0, 0, 2 of radius 0.5
        objects = [Sphere(Vec3(-0.8, 0.5, 1), 0.5, Colour(200, 200, 250)), Plane(-1, Colour(200, 200, 100)), Sphere(Vec3(0.4, 0.4, 1.6), 0.8, Colour(0, 200, 100), True)]
        minDist = float("inf")
        for object in objects:
            dist, sphereColour = object.checkCollision(self, light)
            if dist < minDist:
                self.colour = sphereColour
                minDist = dist
    

class Sphere():
    def __init__(self, center, radius, colour, reflective=False):
        self.center = center
        self.radius =  radius
        self.colour = colour
        self.reflective = reflective
        
    def checkCollision(self, ray, light): # returns a colour and distance along ray
        b = 2 * ray.dir.dot(ray.pos - self.center)
        c = (ray.pos - self.center).magnitude()**2 - self.radius**2
        discriminant = b**2-(4*c)
        if discriminant >= 0:
            ans1 = (-b + sqrt(discriminant)) / 2
            ans2 = (-b - sqrt(discriminant)) / 2
            minClip = 0.01
            if ans1 < minClip and ans2 < minClip:
                return (float("inf"), Colour(0, 0, 255))
            elif ans1 < minClip and ans2 >= minClip:
                closestHit = ans2
            elif ans1 >= minClip and ans2 < minClip:
                closestHit = ans1
            elif ans1 >= ans2:
                closestHit = ans2
            elif ans1 < ans2:
                closestHit = ans1
            collisionPoint = ray.pos + (ray.dir * closestHit)
            normal = (collisionPoint - self.center).normalise()
            toLight = collisionPoint - light
            angle = arccos(normal.dot(toLight) / (normal.magnitude() * toLight.magnitude()))
            scalar = 1/(angle+1)
            if self.reflective:
                reflection = ray.dir - (normal * (normal.dot(ray.dir)*2))
                return (closestHit, Ray(collisionPoint, reflection).colour)

            return (closestHit, self.colour * scalar)
        return (float("inf"), Colour(0, 0, 255))

class Plane():
    def __init__(self, y, colour):
        self.y = y
        self.colour = colour
        
    def checkCollision(self, ray, light):
        dist = (self.y - ray.pos.y)/ray.dir.y
        if dist > 0:
            normal = Vec3(0, 0, 1)
            toLight = light - (ray.pos + (ray.dir * dist))
            angle = arccos(normal.dot(toLight) / (normal.magnitude()*toLight.magnitude()))
            scalar = 1/(angle+1)
            return (dist, self.colour * scalar)
        else:
            return (float("inf"), Colour(0, 0, 255))
        
