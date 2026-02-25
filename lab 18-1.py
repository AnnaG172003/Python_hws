class Rectangle:
    def __init__(self, width, height): #initialize the width and height
        self.width = width
        self.height = height
        #adding the two rectangles
    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)
    #method area returns the area
    def area(self):
        return self.width * self.height

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(7,4)
rect_3= rect_1 + rect_2

print(rect_3.width, rect_3.height)
print(rect_3.area())
