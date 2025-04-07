# app.py
from flask import Flask, request, Response
from bank_account import BankAccount
from bank_system import BankSystem
import json

app = Flask(__name__)
system = BankSystem()

# 테스트용 계좌 등록
acc = BankAccount("홍길동", 1000)
system.add_account(acc)

@app.route("/deposit", methods=["POST"])
def deposit():
    amount = int(request.form.get("amount", 0))
    acc.deposit(amount)
    response_data = {
        "message": f"{amount}원 입금 완료",
        "잔액": acc.get_balance()
    }
    return Response(
        json.dumps(response_data, ensure_ascii=False),
        content_type='application/json; charset=utf-8'
    )

@app.route("/balance", methods=["GET"])
def balance():
    response_data = {"잔액": acc.get_balance()}
    return Response(
        json.dumps(response_data, ensure_ascii=False),
        content_type='application/json; charset=utf-8'
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

