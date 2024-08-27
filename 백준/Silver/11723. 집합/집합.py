import sys

input = sys.stdin.readline

data = set()
for _ in range(int(input())):
    command = input().split()
    a = command[0]

    if a == 'add':
        data.add(int(command[1]))
    elif a == 'check':
        if int(command[1]) in data:
            print(1)
        else:
            print(0)
    elif a == 'remove':
        # remove는 없는 경우 에러 터짐
        # discart는 에러 안 터짐
        data.discard(int(command[1]))
    elif a == 'toggle':
        if int(command[1]) in data:
            data.remove(int(command[1]))
        else:
            data.add(int(command[1]))
    elif a == 'all':
        data = set(range(1, 21))  # 변경띠
    elif a == 'empty':
        data.clear()
