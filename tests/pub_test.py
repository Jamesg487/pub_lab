import unittest
from src.pub import Pub
from src.drinks import Drinks
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.50, self.pub.till)

    def test_customer_buys_drink(self):
        customer = Customer("Julie", 79.00)
        drink1 = Drinks("mojito", 9.00)
        self.pub.increase_till(drink1.price)
        customer.decrease_wallet(drink1.price)
        self.assertEqual(70.00, customer.wallet)
        self.assertEqual(109.00, self.pub.till)