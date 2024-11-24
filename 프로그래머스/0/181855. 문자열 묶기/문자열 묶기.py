def solution(strArr):
    answer = 0
    temp = [0] * 31
    
    for s in strArr:
        temp[len(s)] += 1
    
    return max(temp)