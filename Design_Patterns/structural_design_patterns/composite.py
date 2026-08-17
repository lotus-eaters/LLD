"""
COMPOSITE DESIGN PATTERN
=========================
Problem:
    An e-commerce site sells product BUNDLES (e.g. "Gaming Bundle" =
    Console + Games + Controllers). The shopping cart / order pipeline
    shouldn't need to know "is this one product or a bundle of many?" --
    it should just be able to call .price() and .description() on
    whatever it's holding.
 
Fix:
    Both a single `Item` and a `ProductBundle` (which CONTAINS many
    Products, including other bundles) implement the same `Product`
    interface. The cart code treats them identically -- that's the
    whole point of Composite: uniform treatment of leaf vs container.
 
Note: this reuses the same `Product` interface from decorator.py --
in the Java doc, Composite's Item/ProductBundle literally implement
`org.example.structural.decorator.Product`. Same idea here.
"""

from abc import ABC,abstractmethod
from typing import List

class Product(ABC):
	@abstractmethod
	def description(self)->str:
		pass

	@abstractmethod
	def price(self)->str:
		pass

class Item(Product):
	def __init__(self,price:float,description:str):
		self._price=price
		self._description=description

	def description(self)->str:
		return self._description

	def price(self)->float:
		return self._price


class ProductBundle(Product):
	def __init__(self,description:str):
		self._description=description
		self._prodlist:List[Product]=[]

	def add_to_prodlist(self,prod:Product):
		self._prodlist.append(prod)

	def description(self)->str:
		for prod in self._prodlist:
			print(prod.description())
		return self._description

	def price(self)->float:
		for prod in self._prodlist:
			return sum(prod.price() for prod in self._prodlist)

if __name__=="__main__":
	ps5=Item(50000,"PS5")
	ps5_controller=Item(3200,"PS5 Controller")
	fifa=Item(2500,"FIFA Game")

	summer_bonanza_bundle=ProductBundle("Summer Gaming Bundle")
	summer_bonanza_bundle.add_to_prodlist(ps5)
	summer_bonanza_bundle.add_to_prodlist(ps5_controller)
	summer_bonanza_bundle.add_to_prodlist(fifa)

	print(f"{summer_bonanza_bundle.description()} now selling at {summer_bonanza_bundle.price()}")
 
	# Nested bundles work too -- a "Mega Bundle" containing another bundle --
	# because ProductBundle IS a Product.
	mega_bundle = ProductBundle("Mega Family Bundle")
	mega_bundle.add_to_prodlist(summer_bonanza_bundle)
	mega_bundle.add_to_prodlist(Item(15000, "Extra Controller Pack"))
	print(f"\n{mega_bundle.description()} now selling at {mega_bundle.price()}")
