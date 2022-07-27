from vec import Vec3

class Colour(Vec3):
    def __init__(self, r, g, b):
        super().__init__(int(r), int(g), int(b))
        self.r = self.x
        self.g = self.y
        self.b = self.z
    
    def mod(self):
        self.x %= 255
        self.y %= 255
        self.z %= 255
        return self
    
    def clamp(self):
        self.x = Colour.clampNum(self.x, 0, 255)
        self.y = Colour.clampNum(self.y, 0, 255)
        self.z = Colour.clampNum(self.z, 0, 255)
        
    # ensures that no colours of light are greater than the colour that the object currently emits
    def emit(self, other):
        rCol = other.x if self.x > other.x else self.x
        gCol = other.y if self.y > other.y else self.y
        bCol = other.z if self.z > other.z else self.z
        return Colour(rCol, gCol, bCol)
        
    def get(self):
        return (self.z, self.y, self.z)
    
    def __mul__(self, other):
        return Colour(self.x*other, self.y*other, self.z*other)

    def __add__(self, other):
        return Colour(self.x + other.x, self.y + other.y, self.z + other.z)
    
    @staticmethod
    def clampNum(num, min, max):
        if num < min:
            return min
        elif num > max:
            return max
        else:
            return num
        
    @staticmethod
    def average(colours):
        total = Colour(0, 0, 0)
        for element in colours:
            total = total + element
    
        return Colour(total.r/len(colours), total.g/len(colours), total.b/len(colours))