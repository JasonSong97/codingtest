d = []
for i in range(11):
     d.append([])
     for j in range(11):
          d[i].append(0)

for i in range(10):
     data = input().split()
     for j in range(10):
          d[i + 1][j + 1] = int(data[j])

x, y = 2, 2

