import unittest
from bank_account import BankAccount
from bank_system import BankSystem

class TestBankSystem(unittest.TestCase):
    def test_total_balance_updates_after_transactions(self):
        acc1 = BankAccount("홍길동", 1000)
        acc2 = BankAccount("김철수", 2000)
        system = BankSystem()

        system.add_account(acc1)
        system.add_account(acc2)

        # 초기 잔액 확인
        self.assertEqual(acc1.get_balance(), 1000)
        self.assertEqual(acc2.get_balance(), 2000)
        self.assertEqual(system.get_total_balance(), 3000)

        # acc1 입금 500
        acc1.deposit(500)
        self.assertEqual(acc1.get_balance(), 1500)

        # 총합 
        self.assertEqual(system.get_total_balance(), 3500)

if __name__ == '__main__':
    unittest.main()
