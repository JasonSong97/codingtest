import sys

input = sys.stdin.readline

N, C = map(int, input().split())
house = []
for i in range(N):
  house.append(int(input()))

house.sort()


def binarySearch(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2  # 4

    value = array[0]  # 첫번쨰 원소
    wifiCount = 1
    for i in range(1, N):
      if value + mid <= array[i]:
        wifiCount += 1
        value = array[i] # 초기화

    if wifiCount >= target:
      answer = mid
      start = mid + 1
    else:
      end = mid - 1

  return answer


start = house[0]
end = house[-1] - house[0]
answer = binarySearch(house, C, start, end)
print(answer)
