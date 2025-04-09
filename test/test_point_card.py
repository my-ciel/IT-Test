# test_point_card.py
import unittest
from point_card import PointCard

class TestPointCard(unittest.TestCase):

    def test_charge(self):
        card = PointCard("홍길동", 100)
        card.charge(50)
        self.assertEqual(card.get_balance(), 150)

    def test_use_success(self):
        card = PointCard("홍길동", 100)
        card.use(30)
        self.assertEqual(card.get_balance(), 70)

    def test_use_exact_balance(self):  
        card = PointCard("홍길동", 100)
        card.use(100)
        self.assertEqual(card.get_balance(), 0)

    def test_use_fail(self):
        card = PointCard("홍길동", 100)
        with self.assertRaises(ValueError):
            card.use(150)

if __name__ == "__main__":
    unittest.main()
