# 1초 1억
# x좌표가 증가하는 순, x가 같은 경우 y가 증가하는 순
import sys

input = sys.stdin.readline

N = int(input())

point = []
for _ in range(N):
    x, y = map(int, input().split())
    point.append((x, y))

# NlogN -> 100000 * 100 -> 10000000 -> 1억 미만이라서 가능
point.sort(key=lambda x: (x, y)) 

for p in point:
    print(p[0], p[1])