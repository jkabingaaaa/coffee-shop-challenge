import pytest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder:
    def test_init(self):
        customer = Customer("Jack")
        coffee = Coffee("Cold Brew")
        order = Order(customer, coffee, 4.5)
        assert order in Order.all
    
    def test_customer_property(self):
        customer = Customer("Karen")
        coffee = Coffee("Pour Over")
        order = Order(customer, coffee, 5.5)
        assert order.customer == customer
        
        with pytest.raises(TypeError):
            order.customer = "Not a customer"
    
    def test_coffee_property(self):
        customer = Customer("Liam")
        coffee = Coffee("Irish Coffee")
        order = Order(customer, coffee, 7.0)
        assert order.coffee == coffee
        
        with pytest.raises(TypeError):
            order.coffee = "Not a coffee"
    
    def test_price_property(self):
        customer = Customer("Mia")
        coffee = Coffee("Turkish Coffee")
        order = Order(customer, coffee, 8.0)
        assert order.price == 8.0
        
        with pytest.raises(TypeError):
            Order(customer, coffee, "not a float")
            
        with pytest.raises(ValueError):
            Order(customer, coffee, 0.5)
            
        with pytest.raises(ValueError):
            Order(customer, coffee, 10.5)
            
        with pytest.raises(AttributeError):
            order.price = 9.0