#!/bin/bash

echo "[1] 테스트 시작 중..."
python3 /home/ubuntu/unit_test/test_bank_account.py > /home/ubuntu/it_test/testbank_result.log 2>&1

if [ $? -eq 0 ]; then
  echo "[2] 테스트 통과!"
else
  echo "[2] 테스트 실패. 로그를 확인하세요."
fi
