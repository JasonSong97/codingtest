# 1초 = 1억
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)] # 오름차순으로 주어짐
coin.reverse()

answer = 0
for c in coin: # 큰 수 -> 작은 수
    if K >= c:
        answer += (K // c)
        K %= c
    else: # K < c
        continue

print(answer)