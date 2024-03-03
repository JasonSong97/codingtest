a, m, d, n = map(int, input().split())
x = a
for _ in range(2, n + 1):
    x = (x * m) + d
print(x)