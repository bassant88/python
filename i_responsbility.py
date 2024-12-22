class Area:
    def calculate_area(self):
        pass

# واجهة للرسم
class Draw:
    def draw(self):
        pass

class Circle(Area, Draw):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def draw(self):
        print("Drawing a circle")
class Rectangle(Area, Draw):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def draw(self):
        print("Drawing a rectangle")
class Triangle(Area):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height
