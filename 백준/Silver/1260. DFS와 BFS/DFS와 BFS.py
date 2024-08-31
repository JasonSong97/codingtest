# 아이디어: 양방향
# 자료구조: DFS(stack, 재귀) BFS(queue)
# 시간복잡도: 
from collections import deque
import sys

input = sys.stdin.readline
N, M, V = map(int, input().split())

# 편하게 작업하기 위해 +1 추가
adj = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
  y, x = map(int, input().split())
  adj[y][x] = adj[x][y] = 1  # 양방향 그래프
# adj에는 양방향으로 대칭 + 데이터 포함

# 00000
# 00111
# 01001
# 01001
# 01110

bfsVisit = [False] * (N + 1)
dfsVisit = [False] * (N + 1)

bfsAnswer = []
dfsAnswer = []


def dfs(now):
  dfsVisit[now] = True  # 방문완료!
  dfsAnswer.append(now)  # 방문한 노드 저장

  for nxt in range(N + 1):  # 내가 어디를 방문할 수 있을까?
    if adj[now][nxt] and not dfsVisit[nxt]:  # 방문하지 않았고, 데이터가 존재하는 곳!
      dfs(nxt)


def bfs(first):
  dq = deque()  # queue 선언
  dq.append(first)  # 현재 위치 넣기
  bfsVisit[first] = True  # 방문했습니다!
  bfsAnswer.append(first)  # 방문한 위치 저장

  while dq:  # dq가 있는 동안 while문 수행
    now = dq.popleft()

    for nxt in range(N + 1):  # 어디를 방문할 수 있을까?
      if adj[now][nxt] and not bfsVisit[nxt]:  # 데이터가 있고, 방문하지 않은 곳!
        dq.append(nxt)
        bfsVisit[nxt] = True
        bfsAnswer.append(nxt)

# 탐색하자
dfs(V)
bfs(V)

# 출력
for d in dfsAnswer:
  print(d, end=' ')
print()
for b in bfsAnswer:
  print(b, end=' ')
