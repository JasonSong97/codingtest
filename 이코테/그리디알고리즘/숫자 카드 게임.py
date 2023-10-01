# 푼 날짜
# 23/10/1

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
result = 0

for i in range(n):
     data = list(map(int, input().split()))
     minData = min(data)
     
     result = max(result, minData)

print(result)