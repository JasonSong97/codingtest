# 1
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ball = list(map(int, input().split()))
# 1 3 2 3 2

answer = 0
array = [0] * 11

for x in ball:
    array[x] += 1
# 0, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0

for i in range(1, m + 1):
    n -= array[i]
    answer += array[i] * n

print(answer)

# 2
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ball = list(map(int, input().split()))

answer = 0
for i in range(n):
    for j in range(i, n):
        if ball[i] != ball[j]:
            answer += 1

print(answer)