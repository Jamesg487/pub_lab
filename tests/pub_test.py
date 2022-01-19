import unittest
from src.pub import Pub
from src.drinks import Drinks
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.customer = Customer("Julie", 79.00, 25)
        self.drink1 = Drinks("mojito", 9.00)
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.50, self.pub.till)

    def test_customer_buys_drink(self):
        self.pub.check_age(self.customer.age, self.drink1.price)
        self.customer.decrease_wallet(self.drink1.price)
        # self.pub.increase_till(self.drink1.price)
        # self.customer.decrease_wallet(self.drink1.price)
        self.assertEqual(70.00, self.customer.wallet)
        self.assertEqual(109.00, self.pub.till)

    def test_customer_not_of_age(self):
        customer = Customer("Dave", 50.00, 14)
        age_check = self.pub.check_age(customer.age, self.drink1.price)
        self.assertEqual("Not old enough", age_check)
        self.assertEqual(50.00, customer.wallet)
        self.assertEqual(100.00, self.pub.till)


        