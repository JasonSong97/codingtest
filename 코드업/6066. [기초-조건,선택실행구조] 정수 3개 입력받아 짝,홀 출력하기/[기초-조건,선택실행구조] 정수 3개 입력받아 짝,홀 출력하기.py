data = list(map(int, input().split()))

for d in data:
    if d % 2 == 0:
        print("even")
    else:
        print("odd")