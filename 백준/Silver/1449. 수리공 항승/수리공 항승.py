import sys

input = sys.stdin.readline

n, l = map(int, input().split())
position = list(map(int, input().split()))

check = [False] * 1001
for p in position:
  check[p] = True

answer = 0
nowPosition = 0
while nowPosition < 1001:
  if check[nowPosition] == True:
    answer += 1
    nowPosition += l
  else:
    nowPosition+= 1

print(answer)