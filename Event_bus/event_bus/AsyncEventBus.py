from concurrent.futures import ThreadPoolExecutor
from threading import Lock

from events import order_events

from .interface import EventBus

class AsyncEventBus(EventBus):
	def __init__(self,max_workers=4):
		self.listeners={}
		self.executor=ThreadPoolExecutor(max_workers=max_workers)
		self.lock=Lock()

	def subscribe(self,event_type,listener):
		with self.lock:
			if event_type not in self.listeners:
				self.listeners[event_type]=set()

			self.listeners[event_type].add(listener)

	def unsubscribe(self,event_type,listener):
		with self.lock:
			if event_type not in self.listeners:
				return
			self.listeners[event_type].discard(listener)

	def publish(self,event):
		event_type=type(event)
		with self.lock:
			listeners=set(self.listeners.get(event_type,set()))

		for listener in listeners:
			self.executor.submit(self._notify_listener,listener,event)

	def _notify_listener(self,listener,event):
		try:
			listener.on_event(event)
		except Exception as e:
			print(f"[EventBus] listener {listener.__class__.__name__} failed: {e}")

	def shutdown(self):
		self.executor.shutdown(wait=True)


