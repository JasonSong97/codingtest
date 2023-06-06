# 1
S = input()
value = 0
answer = []

for s in S:
    if s.isalpha():
        answer.append(s)
    else:
        value += int(s)

answer.sort()
if value != 0:
    answer.append(str(value))

print(''.join(answer))

# 2
S = input()

answer = []
value = 0
for i in range(len(S)):
  if 48 <= ord(S[i]) <= 57:
    value += int(S[i])
  else:
    answer.append(S[i])

answer.sort()
answer += str(value)

print(''.join(answer))