import sys
input = sys.stdin.readline

setData = set()
for _ in range(10):
    temp = int(input())
    setData.add(temp % 42)

print(len(setData))