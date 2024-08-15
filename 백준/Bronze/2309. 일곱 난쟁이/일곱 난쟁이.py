from itertools import combinations
import sys

input = sys.stdin.readline

data = [int(input()) for _ in range(9)]
for c in combinations(data, 7):
  if sum(c) == 100:
    for i in sorted(c):
      print(i)
    break