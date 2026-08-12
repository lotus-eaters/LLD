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



