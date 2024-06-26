import unittest
from accountant import Accountant

class TestAccountant(unittest.TestCase):
    """Tests for the class Accountant."""

    def test_initial_balance(self):
        #default balance should be 0
        acc = Accountant()
        self.assertEqual(acc.balance, 0)

        #Test non-default balance
        acc = Accountant(100)
        self.assertEqual(acc.balance,100)

unittest.main()