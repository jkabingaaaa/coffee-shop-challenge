import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_name_is_valid(self):
        customer = Customer("Alice")
        assert customer.name == "Alice"
        
        with pytest.raises(TypeError):
            Customer(123)
            
        with pytest.raises(ValueError):
            Customer("")
            
        with pytest.raises(ValueError):
            Customer("ThisNameIsWayTooLong")
    
    def test_has_orders(self):
        customer = Customer("Bob")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.0)
        assert order in customer.orders()
    
    def test_has_coffees(self):
        customer = Customer("Charlie")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Cappuccino")
        Order(customer, coffee1, 4.5)
        Order(customer, coffee2, 5.5)
        assert coffee1 in customer.coffees()
        assert coffee2 in customer.coffees()
    
    def test_create_order(self):
        customer = Customer("Dave")
        coffee = Coffee("Mocha")
        order = customer.create_order(coffee, 6.0)
        assert order in Order.all
        assert order.customer == customer
        assert order.coffee == coffee