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
