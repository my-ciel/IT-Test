from bank_account import BankAccount

# 계좌생성  
acc = BankAccount("홍길동", 1000)

# 입금 
new_balance = acc.deposit(500)
print(f"[입금] 입금 후 잔액: {new_balance}")

# 출금 
try:
    new_balance = acc.withdraw(5000)
    print(f"[출금] 출금 후 잔액: {new_balance}")
except ValueError as e:
    print(f"[출금 오류] {e}")

