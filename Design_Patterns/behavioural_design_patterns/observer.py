"""
OBSERVER (PUBLISHER-SUBSCRIBER) DESIGN PATTERN
================================================
Problem (from the doc):
    An order status change needs to notify MULTIPLE independent systems:
        Email, SMS, WhatsApp/push notification, (later: analytics, etc.)
    Requirements:
        - async processing (don't block the order update on notification delivery)
        - loose coupling (OrderService has ZERO knowledge of who's listening)
        - dynamic subscription (add/remove listeners at runtime)
 
Fix:
    OrderService publishes an OrderEvent to an EventBus.
    EventBus holds a list of OrderListener subscribers and fans the
    event out to all of them, each on its own thread (so a slow email
    provider doesn't block SMS delivery).
 
Java used CopyOnWriteArrayList (safe iteration while another thread
subscribes) + a fixed thread pool. Python equivalent: a plain list is
fine for subscribe (single GIL-protected append), and
ThreadPoolExecutor for the fan-out.
"""

from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor
from typing import List
from dataclasses import dataclass

@dataclass
class OrderEvent:
	order_id:str
	order_status:str

class OrderListener(ABC):
	@abstractmethod
	def on_order_updated(self,orderevent:OrderEvent)->None:
		pass

class EmailNotifier(OrderListener):
	def on_order_updated(self,orderevent:OrderEvent)->None:
		print(f"Notifed via Email for order id {orderevent.order_id} status {orderevent.order_status}")

class SMSNotifier(OrderListener):
	def on_order_updated(self,orderevent:OrderEvent)->None:
		print(f"Notifed via SMS for order id {orderevent.order_id} status {orderevent.order_status}")

class WhatsAppNotifier(OrderListener):
	def on_order_updated(self,orderevent:OrderEvent)->None:
		print(f"Notifed via WhatsApp for order id {orderevent.order_id} status {orderevent.order_status}")

class EventBus:
	def __init__(self,max_workers:int=5):
		self._listener : List[OrderListener] = []
		self._executor=ThreadPoolExecutor(max_workers=max_workers)

	def subscribe(self,listener:OrderListener):
		self._listener.append(listener)

	def publish(self,orderevent:OrderEvent):
		for listener in self._listener:
			self._executor.submit(listener.on_order_updated, orderevent)

	def shutdown(self):
		self._executor.shutdown(wait=True)

class OrderService:
	def __init__(self,eventbus:EventBus):
		self._eventbus=eventbus

	def update_status(self,order_id: str, status: str) -> None:
		print(f"Order {order_id} updated to {status}")
		self._eventbus.publish(OrderEvent(order_id, status))

if __name__ == "__main__":
    import time
 
    event_bus = EventBus()
 
    event_bus.subscribe(SMSNotifier())
    event_bus.subscribe(EmailNotifier())
    event_bus.subscribe(WhatsAppNotifier())
 
    order_service = OrderService(event_bus)
 
    for status in ["ORDER_PLACED", "PAYMENT_SUCCESS", "PACKED", "SHIPPED", "OUT_FOR_DELIVERY", "DELIVERED"]:
        order_service.update_status("ORD-1001", status)
 
    time.sleep(0.5)  # let async notifications finish before shutdown, for clean demo output
    event_bus.shutdown()
    print("All notifications processed")
 
    # Adding an analytics listener later: ju