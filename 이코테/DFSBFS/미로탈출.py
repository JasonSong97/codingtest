from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for _ in range(N):
     graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
     queue = deque()
     queue.append((x, y))

     while queue:
          x, y = queue.popleft()
          for i in range(4):
               nx = x + dx[i]
               ny = y + dy[i]
          
               if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue
               if graph[nx][ny] == 0:
                    continue
               if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1 # 누적합
                    queue.append((nx, ny))
              
     return graph[N - 1][M - 1] # Index 때문에 -1 함(최단거리 출력)

print(bfs(0, 0))