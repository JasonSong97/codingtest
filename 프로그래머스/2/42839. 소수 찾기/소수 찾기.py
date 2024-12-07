from itertools import permutations
import math


def solution(numbers):
    numberList = list(numbers)
    temp = set()
    for i in range(1, len(numberList) + 1):
        for p in permutations(numberList, i):
            temp.add(int("".join(p)))
            
    if 0 in temp:
        temp.remove(0)
    if 1 in temp:
        temp.remove(1)
        
    answer = 0
    for t in enumerate(temp):
        target = int(math.sqrt(t[1])) + 1
        flag = True
        for i in range(2, target):
            if t[1] % i == 0:
                flag = False
        if flag == True:
            answer += 1
        
        
    return answer