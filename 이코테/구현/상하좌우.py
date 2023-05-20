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