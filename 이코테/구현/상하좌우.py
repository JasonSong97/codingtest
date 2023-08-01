# 1
import sys

n = int(sys.stdin.readline())
data = list(sys.stdin.readline().split())

x, y = 1, 1

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for way in data:
     for i in range(len(move)):
          if move[i] == way:
               nx = x + dx[i]
               ny = y + dy[i]
     
     if nx < 1 or ny < 1 or nx > n or ny > n:
          continue

     x = nx
     y = ny

print(x, y)

# 2
import sys

input = sys.stdin.readline

N = int(input())

# 방향에 대한 정의 -> 방향 벡터 사용 (L R U D)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
directions = ['L', 'R', 'U', 'D']

x, y = 1, 1 # 현재 위치

goal = list(input().split())

for way in goal:
  for i in range(4):
    if way == directions[i]:
      nx = x + dx[i]
      ny = y + dy[i]

      if 1 <= nx <= N and 1 <= ny <= N:
        x = nx
        y = ny

print(x, y)