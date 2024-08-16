# 1초 1억
# 최단거리 bfs queue
# 2 <= N M <= 100
# 1, 1 출발

# board에 주어지는 데이터를 넣는다.
# 방문 유무 체크를 위한 chk 2차원 배열을 동일하게 만들어준다.

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().rstrip() for _ in range(N)]  # 숫자X 문자O
chk = [[False] * M for _ in range(N)]  # 동일한 2차원 체크사이즈

# 상하좌우 -> y는 밑으로 가야 증가 x는 오른쪽으로 이동 시 증가
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

# 방문유무 체크
def isValidCoord(y, x):
  return 0 <= y < N and 0 <= x < M

# bfs
def bfs():
  dq = deque()
  dq.append((0, 0, 1))  # 첫번째 위치 1, 1 넣기 + 카운트1 올려버리기
  chk[0][0] = True

  while dq:  # 큐가 없을때까지 진행
    
    # 1개의 요소를 pop하고 4방으로 넓이 탐색 시전
    y, x, d = dq.popleft()
    
    # 목표인곳에 도착 시 현재 d return 하고 끝
    if y == N - 1 and x == M - 1:  
      return d

    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]
      nd = d + 1

      # 범위해당 + 방문한적 없음 + 지도에 0 아님
      if isValidCoord(ny, nx) and not chk[ny][nx] and board[ny][nx] != '0':
        dq.append((ny, nx, nd))
        chk[ny][nx] = True


print(bfs())
