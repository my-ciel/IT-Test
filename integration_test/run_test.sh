#!/bin/bash

echo "Bank System 테스트 시작..."

# 1. 테스트 실행
python3 /home/ubuntu/integration_test/tc100.py > /home/ubuntu/integration_test/result_tc100.log 2>&1
python3 /home/ubuntu/integration_test/tc101.py > /home/ubuntu/integration_test/result_tc101.log 2>&1

# 2. 결과 출력
echo ""
echo "TC100 결과:"
tail -n 5 result_tc100.log

echo ""
echo "TC101 결과:"
tail -n 5 result_tc101.log

# 3. 전체 성공 여부 판단
if grep -q "FAILED" result_tc100.log || grep -q "FAILED" result_tc101.log; then
    echo ""
    echo "일부 테스트 실패!"
    exit 1
else
    echo ""
    echo "모든 테스트 성공!"
    exit 0
fi
