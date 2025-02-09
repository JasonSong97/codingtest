import sys

input = sys.stdin.readline

n, x = map(int, input().split())
data = list(map(int, input().split()))
answer = []

for i in range(n):
    if data[i] < x:
        answer.append(data[i])

for j in range(len(answer)):
    print(answer[j], end=" ")