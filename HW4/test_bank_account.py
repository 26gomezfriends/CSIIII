import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)

    def tearDown(self):
        self.account = None

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 100)

    def test_deposit_positive_amount(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_withdraw_positive_amount(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(150)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-20)

if __name__ == '__main__':
    unittest.main()
