class Coffee:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters")
        if hasattr(self, '_name'):
            raise AttributeError("Coffee name cannot be changed after initialization")
        self._name = value
    
    def orders(self):
        from order import Order  # Local import
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})  # No import needed
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        if not self.orders():
            return 0
        return sum(order.price for order in self.orders()) / len(self.orders())