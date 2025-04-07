import unittest
import calculator  # calculator.py 모듈을 import

class TestCalculator(unittest.TestCase):

    # TC001: 일반적인 정수 덧셈
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    # TC002: 음수와 양수의 덧셈
    def test_add_negative_and_positive(self):
        self.assertEqual(calculator.add(-5, 10), 5)

    # TC003: 일반적인 정수 뺄셈
    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 4), 6)

    # TC004: 음수 결과가 나오는 뺄셈
    def test_subtract_result_negative(self):
        self.assertEqual(calculator.subtract(0, 5), -5)

    # TC005: 일반적인 곱셈
    def test_multiply(self):
        self.assertEqual(calculator.multiply(7, 6), 42)

    # TC006: 0 곱셈 테스트
    def test_multiply_by_zero(self):
        self.assertEqual(calculator.multiply(0, 999), 0)

    # TC007: 일반적인 정수 나눗셈
    def test_divide_whole_number(self):
        self.assertEqual(calculator.divide(8, 2), 4.0)

    # TC008: 실수 결과가 나오는 나눗셈
    def test_divide_float_result(self):
        self.assertAlmostEqual(calculator.divide(7, 2), 3.5)

    # TC009: 음수가 포함된 나눗셈
    def test_divide_with_negative(self):
        self.assertEqual(calculator.divide(-10, 2), -5.0)

    # TC010: 0으로 나눌 경우 예외 처리
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
