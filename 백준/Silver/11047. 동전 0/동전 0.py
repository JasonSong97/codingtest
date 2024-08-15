import sys

input = sys.stdin.readline

N, M = map(int, input().split())

coin = [int(input()) for _ in range(N)]
coin.reverse()

answer = 0
for c in coin:
  if c <= M:
    answer += (M // c)
    M %= c
  else:
    continue

print(answer)
