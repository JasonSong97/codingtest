import sys

input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))

# array.sort(reverse=True) # 오름차순 내림차순 -> 이것만 가능
array = sorted(array, reverse=True) # 정렬 기준 -> 정렬

for i in range(N):
    print(array[i], end=" ")