#Single Inheritance
class Car:
    def __init__(self,mileage,model,enginetype):
        self.mileage=mileage
        self.model=model
        self.enginetype=enginetype

    def cardetails(self):
        print(f"The mileage of the car is {self.mileage} model is {self.model} enginetype is {self.enginetype}")
        
class Tesla(Car):
    def __init__(self,mileage,model,enginetype,is_self_driving):
        super().__init__(mileage,model,enginetype)
        self.is_self_driving=is_self_driving

    def selfdriving(self):
        print(f"Tesla supports self driving : {self.is_self_driving}")

tesla=Tesla(200,"sedan","electric",True)
tesla.selfdriving()
tesla.cardetails()