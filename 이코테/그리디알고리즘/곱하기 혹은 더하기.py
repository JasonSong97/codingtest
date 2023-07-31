# 1

s = input() # 02984
answer = int(s[0])

for i in range(1, len(s)):
    num = int(s[i])
    if num <= 1 or answer <= 1:
        answer += num
    else:
        answer *= num
        
print(answer)

# 2
import sys

input = sys.stdin.readline

S = input().strip() # \n

answer = int(S[0])

for i in range(1, len(S)):
    if answer <= 1 or int(S[i]) <= 1:
        answer += int(S[i])
    else:
        answer *= int(S[i])

print(answer)