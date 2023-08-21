import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

appleMap = [[0] * (N + 1) for _ in range(N + 1)]


for _ in range(K):
    a, b = map(int, input().split())
    appleMap[a][b] = 1

plans = []
L = int(input())
for _ in range(L):
    X, C = map(str, input().split())
    plans.append((int(X), C))

# 처음에는 오른쪽을 보고 있으므로 (동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4

    return direction

def simulate():
    x, y = 1, 1
    appleMap[x][y] = 2
    direction = 0 # 바라본느 방향
    time = 0 # 몇 초?
    index = 0 # 다음에 회전할 정보
    q = [(x, y)]

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 범위에 있어? + 방문 안했어?
        if 1<=nx and nx<=N and 1<=ny and ny<=N and appleMap[nx][ny] != 2:
            if appleMap[nx][ny] == 0: # 사과 없음
                appleMap[nx][ny] = 2
                q.append((nx, ny))
                # 꼬리 0으로 만들기
                px, py = q.pop(0)
                appleMap[px][py] = 0

            if appleMap[nx][ny] == 1: # 사과 있음
                appleMap[nx][ny] = 2
                q.append((nx, ny))
        else: # 벽이야? 범위에 없어?
            time += 1
            break
        
        x, y = nx, ny
        time += 1
        if index < L and time == plans[index][0]:
            direction = turn(direction, plans[index][1])
            index += 1

    return time

print(simulate())