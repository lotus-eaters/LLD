"""
STRATEGY DESIGN PATTERN
========================
Problem (from the doc):
    Discount rules change often and multiply:
        Loyalty-based discount, coupon-based discount, seasonal discount...
    Requirements:
        - pick behavior at RUNTIME (by a key, e.g. "MONSOON15")
        - add new strategies without touching existing code (OCP)
        - avoid a big if/elif ladder inside Cart
 
Fix:
    Each discount rule is its own class implementing a common
    `DiscountStrategy` interface (just one method: apply(order)).
    A `PricingRegistry` maps string keys -> strategy instances.
    `Cart` doesn't know or care HOW a discount is computed -- it just
    looks the strategy up and calls .apply().
 
Note: this is basically Factory's sibling. Factory picks WHICH OBJECT
to build; Strategy picks WHICH ALGORITHM to run. Here they look almost
identical in shape (both are "registry + key lookup") -- the difference
is intent: Factory returns something you'll call several methods on,
Strategy returns something that does ONE unit of behavior right now.
"""

from abc import ABC,abstractmethod
from dataclasses import dataclass, field
from typing import List,Dict 

@dataclass
class OrderDetails:
    amount:float=0
    user_type:str=""
    coupon:List[str]=field(default_factory=list)

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self,orderdetails:OrderDetails):
        pass

class CouponDiscount(DiscountStrategy):
    def apply(self,orderdetails:OrderDetails)->float:
        if "SAVE10" in orderdetails.coupon:
            return orderdetails.amount*0.90
        return orderdetails.amount

class SeasonalDiscount(DiscountStrategy):
    def apply(self,orderdetails:OrderDetails)->float:
        if "MONSOON15" in orderdetails.coupon:
            return orderdetails.amount*0.85
        return orderdetails.amount

class LoyaltyDiscount(DiscountStrategy):
    def apply(self,orderdetails:OrderDetails)->float:
        if orderdetails.user_type=="GOLD" or "LOYALTY15" in orderdetails.coupon:
            return orderdetails.amount*0.85
        return orderdetails.amount

class NoDiscount(DiscountStrategy):
    def apply(self,orderdetails:OrderDetails)->float:
        return orderdetails.amount

class PricingRegistry:
    def __init__(self):
        self._strategies:Dict[str,DiscountStrategy]={}

    def add_to_registry(self,key:str,strategy:DiscountStrategy)->None:
        self._strategies.setdefault(key,strategy)

    def remove_from_registry(self,key:str):
        self._strategies.pop(key,None)

    def get_pricing_strategy(self,key:str)->DiscountStrategy:
        strategy = self._strategies.get(key)
        if strategy is None:
            raise ValueError(f"No strategy registered for key {key}")
        return strategy

class Cart:
    def __init__(self,registry:PricingRegistry):
        self._registry=registry

    def calculate(self,strategy_key:str,orderdetails:OrderDetails)->float:
        return self._registry.get_pricing_strategy(strategy_key).apply(orderdetails)


if __name__=="__main__":
    pricingreg = PricingRegistry()
    pricingreg.add_to_registry("MONSOON15",SeasonalDiscount())
    pricingreg.add_to_registry("SAVE10",CouponDiscount())
    cart=Cart(pricingreg)
    orderdetails=OrderDetails(1000,"GOLD",coupon=["LOYALTY15","SAVE10","MONSOON15"])
    print("MONSOON15 ->",cart.calculate("MONSOON15",orderdetails))
    print("SAVE10 ->",cart.calculate("SAVE10",orderdetails))




