import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)
 
answer = data[0] * (k * (m // k)) + data[1] * (m - (k * (m // k)))
print(answer)

