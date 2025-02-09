import sys

input = sys.stdin.readline

data = list(map(int, input().split()))

sum = 0

for i in range(len(data)):
    sum += (data[i] * data[i])

print(sum % 10)