import pytest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee:
    def test_name_is_valid(self):
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"
        
        with pytest.raises(TypeError):
            Coffee(123)
            
        with pytest.raises(ValueError):
            Coffee("A")
            
        with pytest.raises(AttributeError):
            coffee.name = "New Name"
    
    def test_has_orders(self):
        coffee = Coffee("Espresso")
        customer = Customer("Eve")
        order = Order(customer, coffee, 3.5)
        assert order in coffee.orders()
    
    def test_has_customers(self):
        coffee = Coffee("Americano")
        customer1 = Customer("Frank")
        customer2 = Customer("Grace")
        Order(customer1, coffee, 4.0)
        Order(customer2, coffee, 4.5)
        assert customer1 in coffee.customers()
        assert customer2 in coffee.customers()
    
    def test_num_orders(self):
        coffee = Coffee("Flat White")
        assert coffee.num_orders() == 0
        customer = Customer("Hank")
        Order(customer, coffee, 5.0)
        assert coffee.num_orders() == 1
    
    def test_average_price(self):
        coffee = Coffee("Macchiato")
        assert coffee.average_price() == 0
        customer = Customer("Ivy")
        Order(customer, coffee, 4.0)
        Order(customer, coffee, 6.0)
        assert coffee.average_price() == 5.0