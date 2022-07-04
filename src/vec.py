class Vec2():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def normalise(self):
        dist = self.magnitude()
        self.x /= dist
        self.y /= dist
        return self
    
    def squaredMagnitude(self):
        return self.x**2 + self.y**2
    
    def magnitude(self):
        return ((self.x*self.x)+(self.y*self.y))**0.5
    
    
    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)
    
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self
    
    def __mul__(self, other):
        return Vec2(self.x*other, self.y*other)
    
    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    
class Vec3():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def normalise(self):
        dist = self.magnitude()
        self.x /= dist
        self.y /= dist
        self.z /= dist
        return self
    
    def squaredMagnitude(self):
        return self.x**2 + self.y**2 + self.z**2
    
    def magnitude(self):
        return ((self.x**2)+(self.y**2)+(self.z**2))**0.5
    
    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    
    def cross(self, other):
        return Vec3((self.y*other.z)-(self.z*other.y), (self.z*other.x)-(self.x*other.z), (self.x*other.y)-(self.y*other.z))
    
    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self
    
    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self
    
    def __mul__(self, other):
        return Vec3(self.x*other, self.y*other, self.z*other)
    
    def __imul__(self, other):
        self.x *= other
        self.y *= other
        self.z *= other
        return self
    
    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"    
    