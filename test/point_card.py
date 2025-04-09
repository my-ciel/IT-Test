# point_card.py
class PointCard:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def charge(self, amount):
        self.balance += amount

    def use(self, amount):
        if self.balance > amount:  
            self.balance -= amount
        else:
            raise ValueError("포인트 부족")

    def get_balance(self):
        return self.balance
