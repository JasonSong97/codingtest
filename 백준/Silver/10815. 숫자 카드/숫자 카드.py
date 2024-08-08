from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))

nList.sort()
for m in mList:
  if (bisect_right(nList, m) - bisect_left(nList, m)) != 0:
    print(1, end=' ')
  else:
    print(0, end=' ')
