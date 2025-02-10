import sys
input = sys.stdin.readline

answer = ''
answerList = []
for _ in range(int(input())):
    num, letter = input().split()
    for l in letter:
        answer += l * int(num)
    answerList.append(answer)
    answer = ''
for a in answerList:
    print(a)