class Component:
    def __init__(self, part_id):
        self.part_id = part_id
    
    def get_info(self):
        return f"Part ID: {self.part_id}"

class Product(Component):  # Multilevel
    def __init__(self, part_id, name, price):
        super().__init__(part_id)
        self.name = name
        self.price = price
    
    def display(self):
        print(f"{self.name} (${self.price}) - {self.get_info()}")

class Electronics(Product):  # Hierarchical branch
    def __init__(self, part_id, name, price, warranty):
        super().__init__(part_id, name, price)
        self.warranty = warranty
    
    def check_warranty(self):
        print(f"{self.name} has {self.warranty} warranty")

class Clothing(Product):  # Hierarchical branch
    def __init__(self, part_id, name, price, size):
        super().__init__(part_id, name, price)
        self.size = size
    
    def get_size(self):
        print(f"{self.name} available in size {self.size}")

phone = Electronics("P001", "iPhone", 999, "2 years")
shirt = Clothing("C001", "T-Shirt", 25, "M")
phone.display()         # iPhone ($999) - Part ID: P001
phone.check_warranty()  # iPhone has 2 years warranty
