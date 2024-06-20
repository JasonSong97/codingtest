import sys

input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

result = list(str(A * B * C))
data = [0] * 10
for i in range(len(result)):
    data[int(result[i])] += 1

for i in range(len(data)):
  print(data[i])