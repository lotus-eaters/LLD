#Multiple Inheritence
#When a class inherits from more than one base class

class Animal:
    def __init__(self,type):
        self.type=type
    def animalType(self):
        print(f"This type of animal is {self.type}")

class Pet:
    def __init__(self,category):
        self.category=category

class Dog(Animal,Pet):
    def __init__(self,type,category,name):
        Animal.__init__(self,type)
        Pet.__init__(self,category)
        self.name=name
    
    def details(self):
        print(f'AnimalType: {self.type} Category: {self.category} Name : {self.name}')

dog = Dog("Mammal","Domestic","Titan")
dog.details()
dog.animalType()
