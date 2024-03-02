w, h, b = map(int, input().split())

x = w * h * b / 8 / 1024 / 1024

print(format(x, '.2f') + ' MB')