from collections import deque

d = deque()

n = int(input())
for i in range(1, n + 1):
  d.append(i)

while len(d) > 1:
  d.popleft()
  d.append(d.popleft())

print(d[0])