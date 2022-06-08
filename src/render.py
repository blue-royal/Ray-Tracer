from PIL import Image
from colour import *
from random import randrange

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
        self.width = 0
        self.height = 0
        
        
img = Render("newTest", [[Colour(randrange(0, 255), randrange(0, 255), randrange(0, 255)) for i in range(500)] for j in range(500)])
img.export()
img.show()
    