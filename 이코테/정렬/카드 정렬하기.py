import sys
import heapq

input = sys.stdin.readline
N = int(input())

answer = 0
heap = []
for i in range(N):
    data = int(input())
    heapq.heappush(heap, data)

while len(heap) != 1:
     first = heapq.heappop(heap)
     second = heapq.heappop(heap)

     sum = (first + second)
     answer += sum
     heapq.heappush(heap, sum)

print(answer)


