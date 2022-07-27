from math import tan
import time
from PIL import Image
from colour import *
from ray import *
import threading

class Grid:
    def __init__(self):
        self.size = 400
        self.samples = 3
        self.grid = [[Colour(0, 0, 0) for i in range(self.size)] for j in range(self.size)]
        self.FOV = pi/2
        self.start = tan(self.FOV/2)
        self.step = (self.start/(self.size/2))/self.samples

    def evaluateRow(self, rowNum, numOfRows):
        for n in range(numOfRows):
            for i in range(len(self.grid[rowNum+n])):
                cols = []
                for k in range(self.samples):
                    pixelPos = Vec3(-self.start, self.start, 0) + Vec3(self.step*(self.samples*i+k), self.step*-(self.samples*(rowNum+n)+k), 0)
                    cols.append(Ray(pixelPos, pixelPos-Vec3(0, 0, -1)).colour)
                colour = Colour.average(cols)
                self.grid[rowNum+n][i] = colour
            print(f"Row {rowNum+n} complete")
            
                
    def evaluateGrid(self):
        for i, col in enumerate(self.grid):
            print(f"Row {i} complete")
            for j in range(len(col)):
                cols = []
                for k in range(self.samples):
                    pixelPos = Vec3(-self.start, self.start, 0) + Vec3(self.step*(self.samples*i+k), self.step*-(self.samples*j+k), 0)
                    cols.append(Ray(Vec3(0, 0, 0), pixelPos-Vec3(0, 0, -1)).colour)
                colour = Colour.average(cols)
                self.grid[j][i] = colour

class Render:
    defaultName = 1
    def __init__(self, imageName=str(defaultName)):
        start1 = time.time()
        gridObj = Grid()
        # numOfThreads = 10
        # threads = []
        # for row in range(0, gridObj.size, numOfThreads):
        #     threads.append(threading.Thread(target=gridObj.evaluateRow, args=(row, numOfThreads,)))
        #     threads[-1].start()
        # for thread in threads:
        #     thread.join()
        # time1 = time.time() - start1
        start2 = time.time()
        gridObj.evaluateGrid()
        time2 = time.time()-start2
        
        # print(time1)
        print(time2)
        
    
        
        self.grid = gridObj.grid
        
        
        
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



                
        

    