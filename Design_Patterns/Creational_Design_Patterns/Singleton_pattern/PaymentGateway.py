import threading

class PaymentGateway:
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
			print("Initializing payment gateway")
			self._initialized=True
	def pay(self, amount:float):
		print(f"Amount paid {amount}")
	def refund(self, amount:float):
		print(f"Refunded Amount: {amount}")

if __name__=="__main__":
	from concurrent.futures import ThreadPoolExecutor

	def get_getway():
		gateway=PaymentGateway()
		print(f"{threading.current_thread().name} -> {id(gateway)}")

	with ThreadPoolExecutor(max_workers=10) as executor:
		for _ in range(100):
			executor.submit(get_getway())

	print(f"\n All threads identical? {id(PaymentGateway())}=={id(PaymentGateway())}")