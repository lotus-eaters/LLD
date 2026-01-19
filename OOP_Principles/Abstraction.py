from abc import ABC, abstractmethod
class Vehicle(ABC):
	@abstractmethod
	def accelerate(self):
		pass
	@abstractmethod
	def brake(self):		
		pass
	def startengine(self):
		print('engine started')
class Car(Vehicle):	
    def accelerate(self):
        print('car accelerated')
    def brake(self):
        print('car braked')
myCar = Car()
myCar.startEngine()
myCar.accelerate()
myCar.brake()