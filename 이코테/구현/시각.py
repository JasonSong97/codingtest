# 푼 날짜
# 2023/8/27

import sys

input = sys.stdin.readline

N = int(input())

answer = 0
for hour in range(N + 1):
  for minute in range(60):
    for second in range(60):
      if '3' in str(hour) + str(minute) + str(second):
        answer += 1

print(answer)