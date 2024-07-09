from collections import deque

dq = deque()

for i in range(1, int(input()) + 1):
  dq.append(i)


while (len(dq) > 1):
  dq.popleft()
  temp = dq.popleft()
  dq.append(temp)

print(dq.pop())