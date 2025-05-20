from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from order import Order
    from coffee import Coffee

class Customer:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value
    
    def orders(self) -> List[Order]:
        from order import Order
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self) -> List[Coffee]:
        from coffee import Coffee
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee: Coffee, price: float) -> Order:
        from order import Order
        return Order(self, coffee, price)