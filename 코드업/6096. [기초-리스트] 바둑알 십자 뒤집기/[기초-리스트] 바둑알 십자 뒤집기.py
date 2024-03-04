d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

for i in range(19):
    data = input().split()
    for j in range(19):
        d[i + 1][j + 1] = int(data[i])

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    
    for i in range(1, 20):
        if d[x][i] == 0:
            d[x][i] = 1
        else:
            d[x][i] = 0
        
        if d[i][y] == 0:
            d[i][y] = 1
        else:
            d[i][y] = 0
    

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=" ")
    print()