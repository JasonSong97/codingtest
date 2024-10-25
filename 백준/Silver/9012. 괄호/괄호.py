# 자료구조 :
# 시간복잡도 : 1초=1억,
# 힌트 :
import sys

input = sys.stdin.readline
T = int(input())

answer = []
for _ in range(T):
    temp = input().rstrip()
    stk = []
    isVPS = True
    for t in temp:
        if t == '(':
            stk.append(t)
        else:  # )
            if stk:
                stk.pop()
            else:
                isVPS = False
                stk.append(t)
    if stk:
        isVPS = False
    answer.append(isVPS)

for a in answer:
    if a:
        print('YES')
    else:
        print("NO")
