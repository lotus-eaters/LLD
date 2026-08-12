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


