import heapq as hq
import sys

input = sys.stdin.readline

minHeap = []
maxHeap = []
for _ in range(int(input())):
  x = int(input())
  if x:
    if x > 0:
      hq.heappush(minHeap, x)
    else:
      hq.heappush(maxHeap, -x)
  else:
    if minHeap:
      if maxHeap:
        if minHeap[0] < abs(-maxHeap[0]):
          print(hq.heappop(minHeap))
        else:
          print(-hq.heappop(maxHeap))
      else:
        print(hq.heappop(minHeap))
    else:
      if maxHeap:
        print(-hq.heappop(maxHeap))
      else:
        print(0)  