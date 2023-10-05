# 푼 날짜
# 23/10/5

import sys

input = sys.stdin.readline
N = int(input())
data = list(map(int, input().split()))

data.sort() # 1 5 7 9

print(data[(N - 1) // 2])