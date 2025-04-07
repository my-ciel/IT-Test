class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if not isinstance(amount, int):
            raise TypeError("출금 금액은 정수여야 합니다.")
        if amount <= 0:
            raise ValueError("출금 금액은 1원 이상이어야 합니다.")
        if amount > self.balance:
            raise ValueError("잔액 부족으로 출금이 불가합니다.")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance


