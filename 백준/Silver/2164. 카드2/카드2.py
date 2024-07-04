from collections import deque

N = int(input())

data = deque()
for i in range(N):
  data.append(i + 1)

while len(data) > 1:
  data.popleft()
  temp = data.popleft()
  data.append(temp)

print(data.popleft())
