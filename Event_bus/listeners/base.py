from abc import ABC,abstractmethod
from typing import TypeVar,Generic
from events.base import Event

T=TypeVar("T", bound=Event)

class EventListener(Generic[T],ABC):
	@abstractmethod
	def on_event(self,event:T):
		pass




