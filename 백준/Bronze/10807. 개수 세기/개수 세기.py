import sys

input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
v = int(input())

answer = 0
for i in range(len(data)):
  if data[i] == v:
    answer += 1
print(answer)