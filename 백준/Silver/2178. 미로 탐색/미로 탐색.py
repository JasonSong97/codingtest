from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [input() for _ in range(N)]

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

chk = [[False] * M for _ in range(N)]
chk[0][0] = True

def isValidCoord(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs():
    dq = deque()
    dq.append((0, 0, 1))
    
    while dq:
        y, x, d = dq.popleft()

        if y == N - 1 and x == M - 1:
            return d
        
        nd = d + 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if isValidCoord(ny, nx) and not chk[ny][nx] and board[ny][nx] == '1':
                chk[ny][nx] = True
                dq.append((ny, nx, nd))


            
print(bfs())