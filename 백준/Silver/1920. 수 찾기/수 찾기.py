# 1초 = 1억
from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

N = int(input())
nList = list(map(int, input().split()))
M = int(input())
mList = list(map(int, input().split()))

nList.sort() # NlogN 

for m in mList:
    rightIndex = bisect_right(nList, m)
    leftIndex = bisect_left(nList, m)
    
    count = rightIndex - leftIndex
    if count == 0:
        print(0)
    else:
        print(1)