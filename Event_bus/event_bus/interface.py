from abc import ABC, abstractmethod

class EventBus(ABC):
	@abstractmethod
	def subscribe(self,event_type,listener):
		pass

	@abstractmethod
	def unsubscribe(self,event_type,listener):
		pass

	@abstractmethod
	def publish(self,event):
		pass

	@abstractmethod
	def shutdown(self):
		pass
