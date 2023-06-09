# 1
from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline
N, x = map(int, input().split()) # 7 2

data = list(map(int, input().split())) # 1 1 2 2 2 2 3

def countByRange(data, leftValue, rightValue):
    rightIndex = bisect_right(data, rightValue)
    leftIndex = bisect_left(data, leftValue)
    return rightIndex - leftIndex

answer = countByRange(data, x, x)

print(answer if answer != 0 else -1)

# 2
import sys

input = sys.stdin.readline

N, x = map(int, input().split())
data = list(map(int, input().split()))

def count(data, target):
     leftIndex = leftBinarySearch(data, target, 0, N-1)
     if leftIndex == None:
          return 0
     rightIndex = rightBinarySearch(data, target, 0, N-1)
     return rightIndex - leftIndex + 1

def leftBinarySearch(data, target, start, end):
     if start > end: # 끝까지 했는데 안나온 경우
          return None
     
     mid = (start + end) // 2
     if (mid == 0 or data[mid - 1] < target) and data[mid] == target: # 가장 왼쪽에 해당하는 것만 찾기
          return mid
     elif data[mid] >= target:
          return leftBinarySearch(data, target, start, mid -1)
     else:
          return leftBinarySearch(data, target, mid + 1, end)

def rightBinarySearch(data, target, start, end):
     if start > end: # 끝까지 했는데 안나온 경우
          return None
     
     mid = (start + end) // 2
     if (mid == N - 1 or target < data[mid + 1]) and data[mid] == target: # 가장 오른쪽에 해당하는 것만 찾기
          return mid
     elif data[mid] > target:
          return rightBinarySearch(data, target, start, mid -1)
     else:
          return rightBinarySearch(data, target, mid + 1, end)

answer = count(data, x)
print(answer if answer != 0 else -1)