import sys
input = sys.stdin.readline

m, n = map(int, input().split())
board = [input() for _ in range(m)]

# 검은색 시작일 경우 기준으로 설정
color = {0 : "B", 1 : "W"}

paint_list = []
# 시작점 찾기
for x_start in range(m - 7):
    for y_start in range(n - 7):
        paint = 0 # 색칠 개수
        paint_w, paint_b = 0, 0 # 흰색, 검은색 시작 경우
        for x in range(x_start, x_start + 8):
            for y in range(y_start, y_start + 8):
                    if board[x][y] != color[(x + y)%2]: # 검은색 시작일 때 틀린 경우
                        paint_b += 1            
                    else: # 흰색 시작일 때 틀린 경우
                        paint_w += 1
        paint = min(paint_b, paint_w)                
        paint_list.append(paint)

print(min(paint_list))