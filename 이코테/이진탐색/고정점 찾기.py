import sys

input = sys.stdin.readline
N = int(input())
data = list(map(int, input().split())) # -15 -6 1 3 7

def binarySearch(data, start, end):
    while start <= end:
        mid = (start + end) // 2

        if data[mid] == mid:
            return mid
        elif data[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return None 

answer = binarySearch(data, 0, N - 1)
print(answer if answer != None else -1)