#Polymorphism better example with instance methods and instance variables
class Shape:
    def area():
        return "Return the area of the shape"

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side

def print_area(Shape):
    return f"The area is {Shape.area()}"
sq=Square(4)
print_area(sq)