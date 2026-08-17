
"""
ADAPTER DESIGN PATTERN
=======================
Problem (from the doc):
    Your system expects a uniform contract:
        pay(amount)
    But every real provider SDK has its own incompatible method name:
        phonePe.makePayment()
        paytm.paytmKaro()
        paypal.sendPayment()
 
    You can't change the provider SDKs (they're third-party / legacy),
    and you don't want CheckoutService branching on "which provider is this".
 
Fix:
    Wrap each incompatible SDK behind an Adapter that implements YOUR
    common `PaymentProcessor` interface. CheckoutService only ever talks
    to `PaymentProcessor` -- it has no idea Paytm's real method is
    called `paytm_karo()`.
 
Note: the doc's Paytm class is ALSO a Singleton (it has its own
getPaytmInstance() with double-checked locking) -- so this demo
deliberately combines Adapter + Singleton, which is common in real
integrations: "the SDK client is a shared singleton resource, and I
adapt its quirky interface to my own contract."
"""

from abc import ABC,abstractmethod
import threading

class PaymentProcesser(ABC):
	@abstractmethod
	def pay(self,amount:float)->None:
		pass

class Paytm:
	_instance=None
	_lock=threading.Lock()

	def __new__(cls):
		if cls._instance is None:
			with cls._lock:
				if cls._instance is None:
					cls._instance=super().__new__(cls)
					cls._instance._initialized=False
		return cls._instance

	def __init__(self):
		if not self._initialized:
			print("Intializing Paytm Gateway")
			self._initialized=True

	def paytm_karo(self,amount:float):
		print(f"Paid {amount} via Paytm")

class PhonePe:
	_instance=None
	_lock=threading.Lock()

	def __new__(cls):
		if cls._instance is None:
			with cls._lock:
				if cls._instance is None:
					cls._instance=super().__new__(cls)
					cls._instance._initialized=False
		return cls._instance

	def __init__(self):
		if not self._initialized:
			print("Intializing PhonePe Gateway")
			self._initialized=True

	def payment_phonepe(self,amount:float):
		print(f"Paid {amount} via PhonePe")

class PaytmProcessor(PaymentProcesser):
	def __init__(self):
		self._paytm=Paytm()
	def pay(self,amount:float):
		self._paytm.paytm_karo(amount)

class PhonePeProcessor(PaymentProcesser):
	def __init__(self):
		self._phonepe=PhonePe()
	def pay(self,amount:float):
		self._phonepe.payment_phonepe(amount)



if __name__=='__main__':
	phonepe_client : PaymentProcesser = PaytmProcessor()
	paytm_client : PhonePeProcessor = PhonePeProcessor()

	phonepe_client.pay(1000)
	paytm_client.pay(2000)


