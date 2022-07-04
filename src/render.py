from math import tan
from PIL import Image
from colour import *
from ray import *

class Render:
    defaultName = 1
    def __init__(self, imageName=str(defaultName), grid=[[Colour(255, 255, 255)]*100]*100):
        self.grid = grid
        name = imageName
        if name == str(Render.defaultName):
            Render.defaultName += 1
        self.savePath = f"images\\{name}.png"
    
    def export(self):
        self.image = Image.new("RGB", size = [len(self.grid),len(self.grid[0])])
        dat = []
        for row in self.grid:
            for colour in row:
                dat.append(colour.get())
        
        self.image.putdata(dat)
        self.image.save(self.savePath)
    
    def show(self):
        self.image.show()


class Grid:
    def __init__(self):
        self.size = 400
        self.grid = [[Colour(0, 0, 0) for i in range(self.size)] for j in range(self.size)]
        FOV = pi/8
        start = tan(FOV/2)
        step = start/(self.size/2)
        for i, col in enumerate(self.grid):
            print(f"Row {i} complete")
            for j in range(len(col)):
                pixelPos = Vec3(-start, start, 0) + Vec3(step*i, step*-j, 0)
                self.grid[i][j] = Ray(pixelPos, pixelPos-Vec3(0, 0, -1)).colour
                
        

    