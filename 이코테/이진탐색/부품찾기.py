import sys

input = sys.stdin.readline

# 1 이진탐색
N = int(input())                                                                                                                                                                                   
nList = list(map(int, input().split()))
M = int(input())
mList = list(map(int, input().split())) 


nList.sort() # 2 3 7 8 9
mList.sort() # 5 7 9

def binarySearch(array, target, start, end):
    while start <= end:
         mid = (start + end) // 2

         if array[mid] == target:
              return mid
         elif array[mid] > target:
              end = mid - 1
         else:
              start = mid + 1
    return None

for target in mList:
     result = binarySearch(nList, target, 0, len(nList) - 1)
     if result != None:
          print("yes", end = " ")
     else:
          print("no", end = " ")


# 2 계수 정렬 -> 1,000,000 넘지 않을 때 사용
N = int(input())
array = [0] * 1000001

for i in input().split():
     array[int(i)] = 1

M = int(input())
x = list(map(int, input().split()))

for i in x:
     if array[i] == 1:
          print("yes", end = "")
     else:
          print("no", end = " ")


# 3 집합 자료형
N = int(input())
array = set(map(int, input().split())) # 중복 제거

M = int(input())
x = list(map(int, input().split()))

for i in x:
     if i in array:
          print("yes", end = " ")
     else:
          print("no", end = " ")