# 1초=1억
# x넣기 -> 가장 작은 값 출력 -> 해당 값 제거
# 파이썬은 min heap 항상 -> max heap은 직접 구현 필요

import heapq as hq
import sys

input = sys.stdin.readline

data = []
for _ in range(int(input())):
    temp = int(input())
    if temp == 0: # 0인 경우
        if data: # not empty
            print(hq.heappop(data))
        else: # empty
            print(0)
    else: # 0아닌 경우
        hq.heappush(data, temp)