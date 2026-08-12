from abc import ABC, abstractmethod
from typing import Type

# ========================================
# INTERFACE (Abstract Product + Creator)
# ========================================
class Dialog(ABC):
    """Abstract Product + Creator Interface"""
    
    @abstractmethod
    def create_button(self) -> 'Button':
        """Factory Method"""
        pass
    
    def render(self):
        """Uses factory method"""
        button = self.create_button()
        button.on_click(self.close_dialog)
        print(f"Rendering {self.__class__.__name__} with {button.__class__.__name__}")

    @abstractmethod
    def close_dialog(self):
        pass

# ========================================
# CONCRETE PRODUCTS (Button implementations)
# ========================================
class Button(ABC):
    @abstractmethod
    def on_click(self, dialog):
        pass

class WindowsButton(Button):
    def on_click(self, dialog):
        print("WindowsButton: Click! Closing dialog.")

class HtmlButton(Button):
    def on_click(self, dialog):
        print("HtmlButton: <button>Click!</button> Closing dialog.")

# ========================================
# CONCRETE CREATORS (Use their own products)
# ========================================
class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()  # Factory method

    def close_dialog(self):
        print("WindowsDialog: Closing Windows dialog")

class WebDialog(Dialog):
    def create_button(self) -> Button:
        return HtmlButton()  # Factory method

    def close_dialog(self):
        print("WebDialog: Closing web dialog")

# ========================================
# USAGE (Client uses abstract Dialog)
# ========================================
def main():
    print("=== Factory Method Demo ===\n")
    
    # Client configures via config
    config = {
        'windows': WindowsDialog,
        'web': WebDialog
    }
    
    dialogs = ['windows', 'web']
    
    for dialog_type in dialogs:
        dialog_class = config[dialog_type]
        dialog = dialog_class()  # Polymorphic creation
        
        dialog.render()  # Uses factory internally
        print("-" * 40)

if __name__ == "__main__":
    main()

from abc import ABC, abstractmethod
from typing import Dict, Type

# 1. Product Interface (What factory creates)
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

# 2. Concrete Products
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height

# 3. Factory (Magic!)
class ShapeFactory:
    _creators: Dict[str, Type[Shape]] = {
        'circle': Circle,
        'rectangle': Rectangle
    }
    
    @classmethod
    def create_shape(cls, shape_type: str, **kwargs) -> Shape:
        creator = cls._creators.get(shape_type.lower())
        if not creator:
            raise ValueError(f"Unknown shape: {shape_type}")
        return creator(**kwargs)

# 4. Usage (No import hell!)
def main():
    # Client doesn't know Circle/Rectangle details
    circle = ShapeFactory.create_shape('circle', radius=5)
    rect = ShapeFactory.create_shape('rectangle', width=4, height=6)
    
    print(f"Circle area: {circle.area():.2f}")    # 78.54
    print(f"Rectangle area: {rect.area():.2f}")   # 24.00

if __name__ == "__main__":
    main()
