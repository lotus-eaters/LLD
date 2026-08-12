from abc import ABC,abstractmethod

class Product(ABC):
	@abstractmethod
	def description(self)->str:
		pass

	@abstractmethod
	def price(self)->str:
		pass

class Tshirt(Product):
	def __init__(self,description:str="Medium sized white colored",price:float=100.00):
		self._description=description
		self._price=price

	def description(self)->str:
		return self._description

	def price(self)->float:
		return self._price

class ProductDecorator(Product,ABC):
	def __init__(self,product:Product):
		self._product=product

class GiftWrap(ProductDecorator):
	def description(self)->str:
		return f"{self._product.description()} + gift wrapped"

	def price(self)->float:
		return self._product.price() + 10.0

class ExtendedWarranty(ProductDecorator):
	def description(self)->str:
		return f"{self._product.description()} + extended warranty"

	def price(self)->float:
		return self._product.price()+ 20.0

class Personalization(ProductDecorator):
	def __init__(self,product:Product,tag_name:str):
		super().__init__(product)
		self._tag_name=tag_name

	def description(self)->str:
		return f"{self._product.description()} + personalized tag + {self._tag_name}"

	def price(self)->float:
		return self._product.price()+ 50.0

if __name__ == "__main__":
    tshirt: Product = Tshirt("Medium sized, white colored", 1000.00)
    tshirt = GiftWrap(tshirt)
    tshirt = ExtendedWarranty(tshirt)
 
    print(f"{tshirt.description()} has the total price of : {tshirt.price()}")
 
    # A completely different combination -- zero new classes needed.
    engraved_gift: Product = Personalization(GiftWrap(Tshirt("Black hoodie", 2000.00)), "For Mom")
    print(f"{engraved_gift.description()} has the total price of : {engraved_gift.price()}")
