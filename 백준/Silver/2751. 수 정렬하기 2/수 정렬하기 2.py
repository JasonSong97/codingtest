import sys

input = sys.stdin.readline

N = int(input())
data = [int(input()) for _ in range(N)]

for d in sorted(data):
  print(d)