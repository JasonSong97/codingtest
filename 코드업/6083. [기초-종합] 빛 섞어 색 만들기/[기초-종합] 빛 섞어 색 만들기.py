r, g, b = map(int, input().split())
count = 0
for i in range(r):
    for j in range(g):
        for h in range(b):
            count += 1
            print(i, j, h)
print(count)
