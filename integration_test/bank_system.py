from bank_account import BankAccount  

class BankSystem:
    def __init__(self):
        self.accounts = []

    def add_account(self, account: BankAccount):
        self.accounts.append(account)
     
    def get_total_balance(self):
        if hasattr(self, '_cached_total'):
         return self._cached_total
        total = 0
        for acc in self.accounts:
          total += acc.get_balance()
        self._cached_total = total  
        return total


 