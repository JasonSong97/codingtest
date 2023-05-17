import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
ball = list(map(int, sys.stdin.readline().rstrip().split()))
answer = 0
array = [0] * 11

for x in ball:
    array[x] += 1

for i in range(1, m + 1):
    n -= array[i]
    answer += array[i] * n

print(answer)
