import sys

input = sys.stdin.readline

N, M = map(int, input().split()) # 4, 6
data = list(map(int, input().split())) # 19 15 10 17

data.sort() # 10 15 17 19


def binarySearch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2 # 14

        sum = 0
        answer = 0
        for cut in array:
            if mid < cut:
               sum += (cut - mid)

        if sum == target:
            return mid
        elif sum > target: # 9 > 6
            answer = mid # 기록
            start = mid + 1
        else:
            end = mid - 1
            
answer = binarySearch(data, M, data[0], data[N - 1])
print(answer)

# 2
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0

while(start <= end):
    total = 0
    mid = (start+end)//2

    for x in array:
        if x > mid:
            total += x - mid

    if total < m:          
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)