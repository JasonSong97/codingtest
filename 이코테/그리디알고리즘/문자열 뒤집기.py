S = input()
answer0 = 0
answer1 = 0

if S[0] == '1':
    answer0 += 1
else:
    answer1 += 1

for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        if S[i + 1] == '1':
            answer0 += 1
        else:
            answer1 += 1
           


print(min(answer0, answer1))
