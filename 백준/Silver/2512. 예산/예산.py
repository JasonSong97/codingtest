import sys

input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
goal = int(input())
# 110 120 140 150

data.sort()

start = 0
end = max(data)  # 150
mid = (start + end) // 2  # 75

answer = 0

def isPossible(mid):
  return sum(min(d, mid) for d in data) <= goal

while start <= end:
  if isPossible(mid): # sum <= goal
    start = mid + 1
    answer = mid
  else: # sum > goal
    end = mid - 1
      
  mid = (start + end) // 2
print(answer)
