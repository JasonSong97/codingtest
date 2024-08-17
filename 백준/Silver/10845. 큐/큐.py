from collections import deque
import sys

input = sys.stdin.readline

dq = deque()
answer = []
for _ in range(int(input())):
    temp = input().rstrip().split() # 이 부분에서 temp는 리스트로 바뀜
    if temp[0] == 'push':
        dq.append(temp[1])
    elif temp[0] == 'front':
        if dq:
            answer.append(dq[0])
        else:
            answer.append(-1)
    elif temp[0] == 'back':
        if dq:
            answer.append(dq[-1])
        else:
            answer.append(-1)
    elif temp[0] == 'empty':
        if dq:
            answer.append(0)
        else:
            answer.append(1)
    elif temp[0] == 'size':
        answer.append(len(dq))
    elif temp[0] == 'pop':
        if dq:
            answer.append(dq.popleft())
        else:
            answer.append(-1)

for a in answer:
    print(a)