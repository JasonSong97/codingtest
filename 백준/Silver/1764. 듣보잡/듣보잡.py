# 2초 = 2억
# 1 <= N, M <= 50만
from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
data1 = [input().rstrip() for _ in range(N)]
data2 = [input().rstrip() for _ in range(M)]

data1.sort() # 최악 NlogN -> 500000 * 707

answer = 0
answerData = []
for d2 in data2:
  leftIndex = bisect_left(data1, d2)
  rightIndex = bisect_right(data1, d2)
  if (rightIndex - leftIndex) == 0:
      continue
  else: # 0이 아닌 경우, 존재하는 것
      answer += 1
      answerData.append(d2)

print(answer)
for a in sorted(answerData):
  print(a)