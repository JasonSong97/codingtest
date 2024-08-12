import sys

sys.setrecursionlimit(10**6) # 제한 풀기

input = sys.stdin.readline

N, M = map(int, input().split())

# 인접행렬 생성
m = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
  y, x = map(lambda x: x - 1, map(int, input().split()))
  m[x][y] = m[y][x] = 1  # 양방향

answer = 0
chk = [False] * N


def dfs(now):
  for nxt in range(N):
    if m[now][nxt] and not chk[nxt]:
      chk[nxt] = True
      dfs(nxt)


for i in range(N):
  if not chk[i]:
    answer += 1
    chk[i] = True
    dfs(i)

print(answer)
