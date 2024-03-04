# 0으로 구성된 지도 그리기
d = []
for i in range(11):
     d.append([])
     for j in range(11):
          d[i].append(0)

# 지도에 입력값 넣기
for i in range(10):
     data = input().split()
     for j in range(10):
          d[i + 1][j + 1] = int(data[j])

# 개미의 위치
x, y = 2, 2

while True:
     # 체크
     if d[x][y] == 0:
          d[x][y] = 9
     elif d[x][y] == 2:
          d[x][y] = 9
          break

     if (d[x][y + 1] == 1 and d[x + 1][y] == 1) or (x == 9 and y == 9):
          break

     if d[x][y + 1] != 1:
          y += 1
     elif d[x + 1][y] != 1:
          x += 1
          
for i in range(1, 11) :
    for j in range(1, 11) :
        print(d[i][j], end=' ')
    print()