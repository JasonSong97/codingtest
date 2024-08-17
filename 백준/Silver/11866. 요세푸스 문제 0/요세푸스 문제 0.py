# 2초 = 2억
# 1 ~ N 원형
# K는 (<= N)
# K번째 사람 제거

# 1 2 3 4 5 6 7
# 1|  2 3 4 5 6 7 1
# 2|  3 4 5 6 7 1 2
# 3|  4 5 6 7 1 2   <-
# 4|  5 6 7 1 2 4
# 5|  6 7 1 2 4 5

from collections import deque
import sys

input = sys.stdin.readline

dq = deque()
N, K = map(int, input().split())

# dq에 원소 넣기
for i in range(1, N + 1):
    dq.append(i)

answer = []
while dq:
    # 2번 뒤로 보내기
    for _ in range(K - 1):
        dq.append(dq.popleft())

    # 3번째 요소 pop
    answer.append(dq.popleft())

# 출력
print('<', end='')
for i in range(N):
    if i == (N - 1):
        print(answer[i], end='')
    else:
        print(answer[i], end=', ')
print('>', end='')