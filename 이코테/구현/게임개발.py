# 푼 날짜
# 2023/8/27

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
x, y, direction = map(int, input().split())

# 지도 정보
oceanMap = []
for i in range(N):
  oceanMap.append(list(map(int, input().split())))

# 방문 여부 정보
visitMap = [[0] * M for _ in range(N)]

# 현재위치 표시
visitMap[x][y] = 1

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turnLeft():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

visitCount = 1
turnTime = 0
while True:
  turnLeft()
  nx = x + dx[direction]
  ny = y + dy[direction]
  
  if visitMap[nx][ny] == 0 and oceanMap[nx][ny] == 0:  # 방문하지 않은 경우
    visitMap[nx][ny] = 1
    x, y = nx, ny
    visitCount += 1
    turnTime = 0
    continue
  else:  # 방문한 경우
    turnTime += 1

  if turnTime == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]

    if oceanMap[nx][ny] == 1:  # 뒤가 바다
      break
    else:
      x, y = nx, ny
    turnTime = 0

print(visitCount)
