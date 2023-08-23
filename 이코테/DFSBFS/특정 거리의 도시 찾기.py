from collections import deque
import sys

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# 정보 입력 start -> end
for _ in range(M):
  start, end = map(int, input().split())
  graph[start].append(end)

# 최단 거리 초기화
distance = [-1] * (N + 1)
distance[X] = 0 # 처음 시작점이니까 0

queue = deque([X])
while queue:
  now = queue.popleft()
  
  for nextNode in graph[now]: # 시작점에서 1개씩 꺼냄
    if distance[nextNode] == -1: # 방문하지 않은 도시
      # 최단거리 갱신
      distance[nextNode] = distance[now] + 1
      queue.append(nextNode)

answer = False
for i in range(1, N + 1):
  if distance[i] == K:
    print(i)
    answer = True

if answer == False:
  print(-1)