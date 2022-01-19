import unittest
from src.drinks import Drinks

class TestDrinks(unittest.TestCase):

    def setUp(self):
        self.drinks = Drinks("beer", 6.00)

    def test_drink_has_name(self):
        self.assertEqual("beer", self.drinks.name)

    def test_drink_has_price(self):
        self.assertEqual(6.00, self.drinks.price)