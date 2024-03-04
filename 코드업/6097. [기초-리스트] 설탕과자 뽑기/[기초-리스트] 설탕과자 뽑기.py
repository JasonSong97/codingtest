h, w = map(int, input().split())

d = []
for i in range(h):
     d.append([])
     for j in range(w):
          d[i].append(0)

n = int(input())
for _ in range(n):
     l, direction, x, y = map(int, input().split())
     
     if direction == 0:
          for i in range(l):
               d[x - 1][y - 1 + i] = 1
     else:
          for i in range(l):
               d[x - 1 + i][y - 1] = 1

for i in range(h):
     for j in range(w):
          print(d[i][j], end=" ")
     print()