import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for i in range(N):
     graph.append(list(map(int, input())))

def dfs(row, column):
     if row <= -1 or row >= N or column <= -1 or column >= M:
          return False
     if graph[row][column] == 0:
          graph[row][column] = 1

          # 상하좌우 DFS 탐색
          dfs[row + 1][column]
          dfs[row - 1][column]
          dfs[row][column + 1]
          dfs[row][column - 1]
          return True
     return False

result = 0
for row in range(N):
     for column in range(M):
          # 각 칸들을 DFS로 순회, 이미 방문처리가 되어있으면 False 반환
          if dfs(row, column) == True:
               result += 1

print(result)