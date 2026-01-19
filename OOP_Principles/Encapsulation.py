#Encapsulation using setters and getters
# Encapsulation is the process of combining data and methods for working with the data into a single unit 
# called a class. It makes it possible to hide a class's implementation details from outside users who 
# engage with the class via its public interface.
# * Class as a Unit of Encapsulation: Classes include information (attributes) and actions (methods) 
# associated with a particular entity or concept. The class's public methods allow users to interact with 
# it without having to understand the inner workings of those methods.

# * Access Modifiers: Access modifiers that regulate the visibility of class members (attributes and 
# methods), such as public, private and protected, are used to enforce encapsulation. Private members 
# can only be reached from within the classroom, whilst public members can be reached from outside.

class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age=age
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name

person=Person("Mrunalini",15)
person.get_age()
person.get_name()
person.set_age(20)
person.get_age()