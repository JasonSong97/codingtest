import sys

input = sys.stdin.readline

n = int(input())
people = list(map(int, input().split()))
group = 0
count = 0

people.sort()

for i in people:
    count += 1
    if count >= i:
        group += 1
        count = 0

print(group)