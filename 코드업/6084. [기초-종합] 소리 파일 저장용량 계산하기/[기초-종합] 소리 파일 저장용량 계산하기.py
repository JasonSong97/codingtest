h, b, c, s = map(int, input().split())

x = h * b * c * s / 8 / 1024 / 1024
print(format(x, '.1f' ) + ' MB')