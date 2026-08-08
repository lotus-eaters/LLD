from dataclasses import dataclass
from datetime import datetime
from .base import Event

@dataclass
class OrderPlacedEvent(Event):
    order_id:str
    customer_name:str
    amount:float
    created_at:datetime = datetime.now()

@dataclass
class PaymentSuccessEvent(Event):
    payment_id:str
    order_id:str
    amount:float

@dataclass
class UserRegisteredEvent(Event):
    user_id:str
    username:str
    email:str
    created_at:datetime = datetime.now()
