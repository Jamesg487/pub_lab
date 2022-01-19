import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Anders", 200.00)

    def test_customer_has_name(self):
        self.assertEqual("Anders", self.customer.name)
    
    def test_customer_wallet(self):
        self.assertEqual(200.00, self.customer.wallet)

    def test_decrease_wallet(self):
        self.customer.decrease_wallet(4.00)
        self.assertEqual(196.00, self.customer.wallet)
    