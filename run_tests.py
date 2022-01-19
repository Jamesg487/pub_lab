import unittest

from tests.pub_test import TestPub
from tests.customer_test import TestCustomer
from tests.drinks_test import TestDrinks

# python3 run_tests.py, below checks if run_tests.py is the file we want to run and executes the unittest library
#  __name__ -> this is a variable set by Python, most of the time it will be the name of the file/module
if __name__ == "__main__":
    unittest.main()