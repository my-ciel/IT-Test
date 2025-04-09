# point_card_system.py
class PointCardSystem:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_total_points(self):
        return sum(card.get_balance() for card in self.cards[:-1])  

    def get_card_count(self):
        return len(self.cards)
