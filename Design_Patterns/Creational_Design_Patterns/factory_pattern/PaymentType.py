"""
FACTORY DESIGN PATTERN
=======================
Problem (from the doc):
    CheckoutService.pay(paymentType) turns into a giant if/else ladder:
        if paymentType == 'CARD': payViaCard(...)
        elif paymentType == 'NETBANKING': payViaNB(...)
        elif ... (grows forever)
    -> violates Open/Closed Principle, tightly couples CheckoutService
       to every concrete payment implementation.
 
Fix:
    CheckoutService only depends on an abstract `Payment` type.
    A `PaymentFactory` keeps a REGISTRY (map) of PaymentType -> constructor,
    so adding a new payment method never touches CheckoutService or the
    factory's core logic -- you just register a new class.
 
Java used `Class.forName(...)` to force static-block registration.
Python doesn't need that trick: importing the module runs its top-level
code, which is where each class registers itself. We do the same thing,
just via normal imports instead of reflection.
""" 
from abc import ABC, abstractmethod
from typing import Dict,Callable
from enum import Enum,auto

class PaymentType(Enum):
	UPI=auto()
	WALLET=auto()
	CREDITCARD=auto()

class Payment(ABC):
	@abstractmethod
	def pay(self,amount:float):
		pass

class PaymentFactory:
	_registry : Dict[PaymentType,Callable[[],Payment]] = {}

	@classmethod
	def register(cls,paymentType:PaymentType,supplier:Callable[[],Payment])->None:
		cls._registry[paymentType]=supplier

	@classmethod
	def create(cls,paymentType:PaymentType):
		supplier=cls._registry.get(paymentType)
		if supplier is None:
			print("Invalid Payment Type, Retry")
		return supplier()

class UPIPayment(Payment):
	def pay(self,amount:float):
		print(f"Paid via UPI: {amount}")

PaymentFactory.register(PaymentType.UPI,UPIPayment)

class WalletPayment(Payment):
	def pay(self,amount:float):
		print(f"Paid via Wallet: {amount}")

PaymentFactory.register(PaymentType.WALLET,WalletPayment)

class CreditCardPayment(Payment):
	def pay(self,amount:float):
		print(f"Paid via CreditCard: {amount}")

PaymentFactory.register(PaymentType.CREDITCARD,CreditCardPayment)

if __name__=="__main__":
	wallet=PaymentFactory.create(PaymentType.WALLET)
	wallet.pay(300)
	credit=PaymentFactory.create(PaymentType.CREDITCARD)
	credit.pay(2000)
	upi=PaymentFactory.create(PaymentType.UPI)
	upi.pay(500)