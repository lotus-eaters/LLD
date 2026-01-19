# "Derived or child classes must be substitutable for their base or parent classes". 
# This principle ensures that any class that is the child of a parent class should be usable 
# in place of its parent without any unexpected behaviour.

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self._width=width
        self._height=height
    def set_width(self,width):
        self._width=width
    def set_height(self,height):
        self._height=height
    def get_area(self):
        return self._width*self._height

class Square(Shape):
    def __init__(self,width):
        self._width=width
    
    def set_width(self,width):
        self._width=width
    
    def get_area(self):
        return self._width*self._width

def get_total_area(shapes):
    total=0
    for shape in shapes:
        total+=shape.get_area()
    return total

shapes = [
    Rectangle(5, 4),   # Area: 20
    Square(3),         # Area: 9
    Rectangle(2, 6)    # Area: 12
]

print(get_total_area(shapes))

# In simple terms: If class B inherits from class A, you should be able to use B anywhere you use A, 
# and everything should still work correctly.

# A subclass should extend the parent class, not break its behavior or contracts.