# 푼 날짜
# 23/10/1

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
answer = 0

while True:
     if n == 1:
          break

     if n % k == 0:
          n = n / k;
     else:
          n -= 1
          
     answer += 1


print(answer)