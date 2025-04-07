import unittest
from bank_account import BankAccount

class TestBankAccountIntegration(unittest.TestCase):

    def setUp(self):
        # 계좌 생성 (초기 잔액: 1000원)
        self.acc = BankAccount("홍길동", 1000)

    def test_deposit_then_withdraw_should_result_correct_balance(self):
        """입금 후 출금 → 잔액 정확성 검증"""
        self.acc.deposit(3000)
        self.assertEqual(self.acc.get_balance(), 4000)

        self.acc.withdraw(1000)
        self.assertEqual(self.acc.get_balance(), 3000)

    def test_withdraw_more_than_balance_should_raise_value_error(self):
        """잔액 초과 출금 시 ValueError 예외 발생 + 잔액 유지"""
        self.acc.deposit(1000)
        self.assertEqual(self.acc.get_balance(), 2000)

        with self.assertRaises(ValueError) as context:
            self.acc.withdraw(3000)

        self.assertEqual(str(context.exception), "잔액 부족으로 출금이 불가합니다.")
        self.assertEqual(self.acc.get_balance(), 2000)

if __name__ == '__main__':
    unittest.main()

