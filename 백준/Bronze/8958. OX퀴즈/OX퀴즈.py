import sys
input = sys.stdin.readline

answer = []
for _ in range(int(input())):
    temp = input()
    
    point = 0
    tempSum = 0
    for t in temp: # OOOXXXOXOOX
        if t == 'O':
            point += 1
        else:
            tempSum += (point * (2 + (point - 1))) // 2
            point = 0
    answer.append(tempSum)

for a in answer:
    print(a)













