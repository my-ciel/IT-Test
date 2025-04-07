from bank_account import BankAccount
from bank_system import BankSystem

# 계좌 생성
acc1 = BankAccount("홍길동A", 1000)
acc2 = BankAccount("홍길동B", 2000)

# 뱅크 시스템에 등록
system = BankSystem()
system.add_account(acc1)
system.add_account(acc2)

# 초기 상태 출력
print("초기 상태")
print("홍길동A 계좌 잔액:", acc1.get_balance())
print("홍길동B 계좌 잔액:", acc2.get_balance())
print("통합 잔액:", system.get_total_balance())
print()

# 홍길동A 계좌에 입금
acc1.deposit(500)

# 변경된 상태 출력
print("입금 후 상태 (홍길동A계좌 +500)")
print("홍길동A 계좌 잔액:", acc1.get_balance())  
print("홍길동B 계좌 잔액:", acc2.get_balance())  
print("통합 잔액:", system.get_total_balance())  
print()
