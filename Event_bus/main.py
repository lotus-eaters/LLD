from datetime import datetime

from event_bus.AsyncEventBus import AsyncEventBus

from events.order_events import OrderPlacedEvent, PaymentSuccessEvent, UserRegisteredEvent

from listeners.listeners import EmailListener, InventoryListener, AnalyticsListener, WalletListener

def main():
	bus=AsyncEventBus(max_workers=4)

	email=EmailListener()
	inventory=InventoryListener()
	analytics=AnalyticsListener()
	wallet=WalletListener()

	bus.subscribe(OrderPlacedEvent,inventory)

	bus.subscribe(OrderPlacedEvent,analytics)

	bus.subscribe(PaymentSuccessEvent,wallet)

	bus.subscribe(OrderPlacedEvent,email)

	bus.subscribe(UserRegisteredEvent,email)

	order_event = OrderPlacedEvent( order_id="ORD-101", customer_name="Alice", amount=2500.0, created_at=datetime.now())
	bus.publish(order_event) 
	
	payment_event = PaymentSuccessEvent( payment_id="PAY-101", order_id="ORD-101", amount=2500.0 ) 
	bus.publish(payment_event) 

	user_event=UserRegisteredEvent(user_id="USER-101",username="alice",email="alice@example.com")
	bus.publish(user_event)

	bus.unsubscribe( OrderPlacedEvent, inventory ) 
	bus.shutdown() 

if __name__ == "__main__": 
	main()
