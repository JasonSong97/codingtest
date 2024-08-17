# 1초 = 1억
from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

# 입력받기
N = int(input())
nList = list(map(int, input().split()))
M = int(input())
mList = list(map(int, input().split()))

# 이분탐색을 위한 정렬 NlogN -> 500000 * 223 1천만 연산(가능)
nList.sort()

for m in mList:
    rightIndex = bisect_right(nList, m) #오른쪽에 존재하는 index + 1
    leftIndex = bisect_left(nList, m) #왼쪽에 존재하는 index

    gapCount = rightIndex - leftIndex
    if gapCount == 0:
        print(0, end=' ')
    else:
        print(gapCount, end=' ')