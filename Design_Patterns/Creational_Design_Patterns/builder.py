"""
BUILDER DESIGN PATTERN
=======================
Problem:
    `Order` has a LOT of fields (orderId, userId, createdAt, orderStatus,
    baseAmount, finalPrice, emi, deliveryType, bankOfferApplicable,
    couponCode, size...). Some are mandatory, most are optional.

    A giant constructor like:
        Order(orderId, userId, createdAt, orderStatus, baseAmount,
              finalPrice, emi, deliveryType, bankOfferApplicable,
              couponCode, size)
    becomes unreadable and error-prone (which boolean was which again?).

Fix:
    Build the object step-by-step with named, chainable methods:
        order = (Order.builder()
                       .order_id("ORD123")
                       .size("M")
                       .emi(True)
                       .coupon_code("SAVE10")
                       .build())

The Java version used Lombok's `@Builder` to auto-generate this.
Python has no direct Lombok equivalent, so we hand-roll a small
OrderBuilder class -- this is actually the *real* mechanics Lombok
generates for you under the hood in Java.
"""

from dataclasses import dataclass, field


@dataclass
class Order:
    order_id: str = ""
    user_id: str = ""
    created_at: int = 0
    order_status: str = ""
    base_amount: float = 0.0
    final_price: float = 0.0
    emi: bool = False
    delivery_type: str = ""
    bank_offer_applicable: bool = False
    coupon_code: str = ""
    size: str = ""

    def show_order_details(self) -> None:
        print(
            f"Order has {self.final_price} "
            f"{self.order_id} {self.order_status} {self.bank_offer_applicable}"
        )

    @staticmethod
    def builder() -> "OrderBuilder":
        return OrderBuilder()


class OrderBuilder:
    """
    Hand-rolled equivalent of what Lombok's @Builder generates.
    Every setter returns `self` so calls can be chained (fluent API),
    and .build() is the only place the real Order gets constructed.
    """

    def __init__(self):
        self._order = Order()

    def order_id(self, order_id: str) -> "OrderBuilder":
        self._order.order_id = order_id
        return self

    def user_id(self, user_id: str) -> "OrderBuilder":
        self._order.user_id = user_id
        return self

    def created_at(self, created_at: int) -> "OrderBuilder":
        self._order.created_at = created_at
        return self

    def order_status(self, order_status: str) -> "OrderBuilder":
        self._order.order_status = order_status
        return self

    def base_amount(self, base_amount: float) -> "OrderBuilder":
        self._order.base_amount = base_amount
        return self

    def final_price(self, final_price: float) -> "OrderBuilder":
        self._order.final_price = final_price
        return self

    def emi(self, emi: bool) -> "OrderBuilder":
        self._order.emi = emi
        return self

    def delivery_type(self, delivery_type: str) -> "OrderBuilder":
        self._order.delivery_type = delivery_type
        return self

    def bank_offer_applicable(self, bank_offer_applicable: bool) -> "OrderBuilder":
        self._order.bank_offer_applicable = bank_offer_applicable
        return self

    def coupon_code(self, coupon_code: str) -> "OrderBuilder":
        self._order.coupon_code = coupon_code
        return self

    def size(self, size: str) -> "OrderBuilder":
        self._order.size = size
        return self

    def build(self) -> Order:
        return self._order


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    order = (
        Order.builder()
        .order_id("ORD1001")
        .user_id("USR55")
        .order_status("CONFIRMED")
        .base_amount(2000)
        .final_price(1800)
        .emi(True)
        .delivery_type("EXPRESS")
        .bank_offer_applicable(True)
        .coupon_code("SAVE10")
        .size("M")
        .build()
    )
    order.show_order_details()

    # --------------------------------------------------------------
    # Pythonic shortcut worth knowing for interviews:
    # Since Python has keyword arguments + @dataclass defaults,
    # for SIMPLE cases you often don't need a hand-rolled builder at all:
    quick_order = Order(order_id="ORD1002", size="L", emi=False)
    quick_order.show_order_details()
    # The real Builder pattern earns its place when construction needs
    # VALIDATION, STEP ORDERING, or building DIFFERENT REPRESENTATIONS
    # from the same steps (e.g. director classes) -- not just "many fields".