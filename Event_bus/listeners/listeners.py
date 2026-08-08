from events.order_events import OrderPlacedEvent,PaymentSuccessEvent,UserRegisteredEvent
from .base import EventListener

class EmailListener(EventListener[OrderPlacedEvent]):

	def on_event(self,event: OrderPlacedEvent):
		if isinstance(event,OrderPlacedEvent):
			self.handle_order_placed(event)
		elif isinstance(event,PaymentSuccessEvent):
			self.handle_payment_success(event)
		elif isinstance(event,UserRegisteredEvent):
			self.handle_user_registered(event)

	def handle_order_placed(self,event:OrderPlacedEvent):
		print(f"[Email] Order Confirmation Sent for {event.order_id}")

	def handle_payment_success(self,event:PaymentSuccessEvent):
		print(f"[Email] Payment Confirmation Sent for {event.payment_id}")

	def handle_user_registered(self,event:UserRegisteredEvent):
		print(f"[Email] User sucessful registeration confirmation sent to {event.email}")

class InventoryListener(EventListener[OrderPlacedEvent]):
	def on_event(self,event: OrderPlacedEvent):
		print(f"[Inventory] Inventory Updated for {event.order_id}")

class AnalyticsListener(EventListener[OrderPlacedEvent]):
	def on_event(self,event:OrderPlacedEvent):
		print(f"[Analytics] Recording order for {event.order_id}")

class WalletListener(EventListener[PaymentSuccessEvent]):
	def on_event(self,event:PaymentSuccessEvent):
		print(f"[Wallet] Updating Wallet for {event.payment_id}")
