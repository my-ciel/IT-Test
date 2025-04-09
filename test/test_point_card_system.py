# test_point_card_system.py
import unittest
from point_card import PointCard
from point_card_system import PointCardSystem

class TestPointCardSystem(unittest.TestCase):

    def test_total_points_and_card_count(self):
        system = PointCardSystem()

        card1 = PointCard("홍길동", 100)
        card2 = PointCard("김영희", 150)

        card1.charge(50)      
        card2.use(30)         

        system.add_card(card1)
        system.add_card(card2)

        self.assertEqual(system.get_card_count(), 2)
        self.assertEqual(system.get_total_points(), 270)  

if __name__ == "__main__":
    unittest.main()
