from pygame import Color
from vec import Vec3

class Colour(Vec3):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
    
    def mod(self):
        self.x %= 255
        self.y %= 255
        self.z %= 255
        return self
    
    def clamp(self):
        self.x = Colour.clampNum(self.x, 0, 255)
        self.y = Colour.clampNum(self.y, 0, 255)
        self.z = Colour.clampNum(self.z, 0, 255)
        
    def get(self):
        return (self.z, self.y, self.z)
    
    @staticmethod
    def clampNum(num, min, max):
        if num < min:
            return min
        elif num > max:
            return max
        else:
            return num