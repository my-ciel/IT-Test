import unittest
from bank_account import BankAccount  

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.acc = BankAccount("홍길동", 1000)

    def test_account_creation(self):
        self.assertEqual(self.acc.get_balance(), 1000)

    def test_deposit(self):
        result = self.acc.deposit(500)
        self.assertEqual(result, 1500)

    def test_withdraw(self):
        result = self.acc.withdraw(300)
        self.assertEqual(result, 700)

    def test_withdraw_too_much(self):
        with self.assertRaises(ValueError):
            self.acc.withdraw(5000)

    def test_get_balance(self):
        self.assertEqual(self.acc.get_balance(), 1000)

if __name__ == '__main__':
    unittest.main()
