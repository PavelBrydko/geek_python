class Road:

    _length = 0
    _width = 0

    def __init__ (self, mass, centimeter):
        self.mass = mass
        self.centimeter = centimeter
        self.index = Road._length * Road._width * mass * centimeter / 100


Road._length = 20
Road._width = 5000

a = Road(25, 5)
print(a.index)

